"""
Collaboration Indicators
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2._indicators.collaboration_indicators_by_topic import collaboration_indicators_by_topic
>>> collaboration_indicators_by_topic("countries", directory=directory).head()
                OCC  single_publication  multiple_publication  mp_ratio
countries                                                              
United Kingdom   16                  10                     6      0.38
Australia        13                   4                     9      0.69
Germany          11                   3                     8      0.73
United States    10                   6                     4      0.40
Hong Kong         8                   2                     6      0.75

>>> from pprint import pprint
>>> pprint(sorted(collaboration_indicators_by_topic("countries", directory=directory).columns.to_list()))
['OCC', 'mp_ratio', 'multiple_publication', 'single_publication']


"""


import numpy as np

from .._read_records import read_records


def collaboration_indicators_by_topic(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Collaboration indicators."""

    documents = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    documents = documents.assign(OCC=1)
    documents["single_publication"] = documents[criterion].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0
    )
    documents["multiple_publication"] = documents[criterion].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0
    )

    # ----< remove explode >-------------------------------------------------------------
    exploded = documents[
        [
            criterion,
            "OCC",
            "single_publication",
            "multiple_publication",
            "article",
        ]
    ].copy()
    exploded[criterion] = exploded[criterion].str.split(";")
    exploded = exploded.explode(criterion)
    exploded[criterion] = exploded[criterion].str.strip()
    # ------------------------------------------------------------------------------------

    indicators = exploded.groupby(criterion, as_index=False).agg(
        {
            "OCC": np.sum,
            "single_publication": np.sum,
            "multiple_publication": np.sum,
        }
    )
    indicators["mp_ratio"] = [
        round(mp / nd, 2)
        for nd, mp in zip(indicators.OCC, indicators.multiple_publication)
    ]

    indicators = indicators.set_index(criterion)
    indicators = indicators.sort_values(by=["OCC"], ascending=False)

    return indicators
