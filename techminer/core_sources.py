"""
Core sources
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> core_sources(directory)
    Num Sources        %  ...  Tot Documents Bradford's Group
0             1   0.13 %  ...          1.7 %                1
1             1   0.13 %  ...         3.15 %                1
2             1   0.13 %  ...         4.55 %                1
3             1   0.13 %  ...         5.88 %                1
4             1   0.13 %  ...          7.1 %                1
5             1   0.13 %  ...         8.19 %                1
6             2   0.26 %  ...        10.13 %                1
7             1   0.13 %  ...        11.04 %                1
8             2   0.26 %  ...        12.73 %                1
9             1   0.13 %  ...        13.52 %                1
10            3   0.39 %  ...        15.71 %                1
11            2   0.26 %  ...        17.04 %                1
12            3   0.39 %  ...        18.86 %                1
13            2   0.26 %  ...        19.95 %                1
14           11   1.41 %  ...        25.29 %                1
15           10   1.29 %  ...        29.53 %                1
16            9   1.16 %  ...        32.81 %                1
17           20   2.57 %  ...        38.87 %                2
18           34   4.37 %  ...        47.12 %                2
19           40   5.14 %  ...         54.4 %                2
20          120  15.42 %  ...        68.95 %                3
21          512  65.81 %  ...        100.0 %                3
<BLANKLINE>
[22 rows x 9 columns]


"""

import numpy as np
import pandas as pd

from .utils import explode, load_filtered_documents


def core_sources(directory):
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
