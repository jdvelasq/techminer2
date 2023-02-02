"""
Collaboration Indicators by Topic
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.indicators.collaboration_indicators_by_topic("countries", directory=directory).head()
                OCC  global_citations  ...  multiple_publication  mp_ratio
countries                              ...                                
United Kingdom    7               199  ...                     3      0.43
Australia         7               199  ...                     3      0.43
United States     6                59  ...                     2      0.33
Ireland           5                55  ...                     1      0.20
China             5                27  ...                     3      0.60
<BLANKLINE>
[5 rows x 6 columns]

>>> from pprint import pprint
>>> pprint(sorted(techminer.indicators.collaboration_indicators_by_topic("countries", directory=directory).columns.to_list()))
['OCC',
 'global_citations',
 'local_citations',
 'mp_ratio',
 'multiple_publication',
 'single_publication']


"""


import numpy as np

from ..._read_records import read_records


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
            "global_citations",
            "local_citations",
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
            "global_citations": np.sum,
            "local_citations": np.sum,
            "single_publication": np.sum,
            "multiple_publication": np.sum,
        }
    )
    indicators["mp_ratio"] = [
        round(mp / nd, 2)
        for nd, mp in zip(indicators.OCC, indicators.multiple_publication)
    ]

    indicators = indicators.set_index(criterion)
    indicators = indicators.sort_values(
        by=["OCC", "global_citations", "local_citations"],
        ascending=[False, False, False],
    )

    return indicators
