"""
Collaboration Indicators
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2.bibliometrix.collaboration_indicators import collaboration_indicators
>>> collaboration_indicators("countries", directory=directory).head()
                OCC  single_publication  multiple_publication  mp_ratio
countries                                                              
United Kingdom   16                  10                     6      0.38
Australia        13                   4                     9      0.69
Germany          11                   3                     8      0.73
United States    10                   6                     4      0.40
Hong Kong         8                   2                     6      0.75

>>> from pprint import pprint
>>> pprint(sorted(collaboration_indicators("countries", directory=directory).columns.to_list()))
['OCC', 'mp_ratio', 'multiple_publication', 'single_publication']


"""


import numpy as np

from ..read_records import read_records


def collaboration_indicators(
    column,
    directory="./",
    database="documents",
):
    """Collaboration indicators."""

    documents = read_records(
        directory=directory, database=database, use_filter=(database == "documents")
    )
    documents = documents.assign(OCC=1)
    documents["single_publication"] = documents[column].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0
    )
    documents["multiple_publication"] = documents[column].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0
    )

    # ----< remove explode >-------------------------------------------------------------
    exploded = documents[
        [
            column,
            "OCC",
            "single_publication",
            "multiple_publication",
            "article",
        ]
    ].copy()
    exploded[column] = exploded[column].str.split(";")
    exploded = exploded.explode(column)
    exploded[column] = exploded[column].str.strip()
    # ------------------------------------------------------------------------------------

    indicators = exploded.groupby(column, as_index=False).agg(
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

    indicators = indicators.set_index(column)
    indicators = indicators.sort_values(by=["OCC"], ascending=False)

    return indicators
