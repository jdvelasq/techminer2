"""
Collaboration indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> collaboration_indicators(directory, "countries").head()
                num_documents  single_publication  multiple_publication  \\
countries                                                                 
united states             187                 105                    82   
china                     186                  95                    91   
united kingdom            148                  68                    80   
indonesia                  85                  77                     8   
india                      78                  53                    25   
.
                mp_ratio  
countries                 
united states       0.44  
china               0.49  
united kingdom      0.54  
indonesia           0.09  
india               0.32

"""


import numpy as np
import pandas as pd

from .utils import explode, load_filtered_documents


def collaboration_indicators(
    directory,
    column,
    sep="; ",
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
