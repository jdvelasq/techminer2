"""
Collaboration Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> collaboration_indicators("countries", directory=directory).head()
                num_documents  ...  mp_ratio
countries                      ...          
china                      43  ...      0.53
united kingdom             41  ...      0.54
indonesia                  22  ...      0.05
united states              22  ...      0.68
australia                  18  ...      0.78
<BLANKLINE>
[5 rows x 4 columns]

"""


import numpy as np

from ._read_records import read_filtered_records


def collaboration_indicators(
    column,
    sep="; ",
    directory="./",
):
    documents = load_filtered_documents(directory)
    documents = documents.assign(num_documents=1)
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
            "num_documents",
            "single_publication",
            "multiple_publication",
            "record_no",
        ]
    ].copy()
    exploded[column] = exploded[column].str.split(";")
    exploded = exploded.explode(column)
    exploded[column] = exploded[column].str.strip()
    # ------------------------------------------------------------------------------------

    indicators = exploded.groupby(column, as_index=False).agg(
        {
            "num_documents": np.sum,
            "single_publication": np.sum,
            "multiple_publication": np.sum,
        }
    )
    indicators["mp_ratio"] = [
        round(mp / nd, 2)
        for nd, mp in zip(indicators.num_documents, indicators.multiple_publication)
    ]

    indicators = indicators.set_index(column)
    indicators = indicators.sort_values(by=["num_documents"], ascending=False)

    return indicators
