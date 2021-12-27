"""
Core Sources
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> core_sources(directory)
   Num Sources        %  ...  Tot Documents Bradford's Group
0            1   0.69 %  ...         6.05 %                1
1            1   0.69 %  ...        10.48 %                1
2            1   0.69 %  ...        13.71 %                1
3            1   0.69 %  ...        16.53 %                1
4            2   1.38 %  ...        20.56 %                1
5            9   6.21 %  ...        35.08 %                2
6            6   4.14 %  ...        42.34 %                2
7           19   13.1 %  ...        57.66 %                2
8          105  72.41 %  ...        100.0 %                3
<BLANKLINE>
[9 rows x 9 columns]

"""

import numpy as np
import pandas as pd

from .common.explode import explode
from .documents_api.load_filtered_documents import load_filtered_documents


def core_sources(directory="./"):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """
    documents = load_filtered_documents(directory)
    documents["num_documents"] = 1
    documents = explode(
        documents[
            [
                "source_name",
                "num_documents",
                "record_no",
            ]
        ],
        "source_name",
        sep="; ",
    )

    sources = documents.groupby("source_name", as_index=True).agg(
        {
            "num_documents": np.sum,
        }
    )
    sources = sources[["num_documents"]]
    sources = sources.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(sources), 2)) + " %" for a in sources]
    sources = pd.DataFrame(
        {"Num Sources": sources.tolist(), "%": w, "Documents published": sources.index}
    )

    sources = sources.sort_values(["Documents published"], ascending=False)
    sources["Acum Num Sources"] = sources["Num Sources"].cumsum()
    sources["% Acum"] = [
        str(round(100 * a / sum(sources["Num Sources"]), 2)) + " %"
        for a in sources["Acum Num Sources"]
    ]

    sources["Tot Documents published"] = (
        sources["Num Sources"] * sources["Documents published"]
    )
    sources["Num Documents"] = sources["Tot Documents published"].cumsum()
    sources["Tot Documents"] = sources["Num Documents"].map(
        lambda w: str(round(w / sources["Num Documents"].max() * 100, 2)) + " %"
    )

    bradford1 = int(len(documents) / 3)
    bradford2 = 2 * bradford1

    sources["Bradford's Group"] = sources["Num Documents"].map(
        lambda w: 3 if w > bradford2 else (2 if w > bradford1 else 1)
    )

    sources = sources[
        [
            "Num Sources",
            "%",
            "Acum Num Sources",
            "% Acum",
            "Documents published",
            "Tot Documents published",
            "Num Documents",
            "Tot Documents",
            "Bradford's Group",
        ]
    ]

    sources = sources.reset_index(drop=True)

    return sources
