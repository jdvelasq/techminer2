"""
Core sources
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> core_sources(directory)
    Num Sources        %  ...  Tot Documents Bradford's Group
0             1   0.22 %  ...         1.82 %                1
1             2   0.43 %  ...         4.48 %                1
2             2   0.43 %  ...          6.9 %                1
3             1   0.22 %  ...         7.99 %                1
4             4   0.86 %  ...        11.86 %                1
5             8   1.72 %  ...        18.64 %                1
6             2   0.43 %  ...         20.1 %                1
7            10   2.15 %  ...        26.15 %                1
8            21   4.52 %  ...        36.32 %                2
9            27   5.81 %  ...        46.13 %                2
10           58  12.47 %  ...        60.17 %                2
11          329  70.75 %  ...        100.0 %                3
<BLANKLINE>
[12 rows x 9 columns]

"""

import numpy as np
import pandas as pd

from .utils import explode, load_filtered_documents


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
