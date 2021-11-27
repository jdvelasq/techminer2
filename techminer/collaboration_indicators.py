"""
Collaboration indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> collaboration_indicators("countries", directory=directory).head()
                num_documents  ...  mp_ratio
countries                      ...          
china                     123  ...      0.49
united states             119  ...      0.46
united kingdom             91  ...      0.56
indonesia                  54  ...      0.09
australia                  52  ...      0.62
<BLANKLINE>
[5 rows x 4 columns]

"""


import numpy as np
import pandas as pd

from .utils import explode, load_filtered_documents


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

    exploded = explode(
        documents[
            [
                column,
                "num_documents",
                "single_publication",
                "multiple_publication",
                "record_no",
            ]
        ],
        column=column,
        sep=sep,
    )
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
