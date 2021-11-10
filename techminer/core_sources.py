"""
Core sources report
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> core_sources(directory)
    Num Sources        %  Acum Num Sources   % Acum  Documents published  \\
0             2   0.31 %                 2   0.31 %                   25   
1             1   0.15 %                 3   0.46 %                   22   
2             1   0.15 %                 4   0.62 %                   18   
3             1   0.15 %                 5   0.77 %                   16   
4             2   0.31 %                 7   1.08 %                   15   
5             2   0.31 %                 9   1.39 %                   14   
6             1   0.15 %                10   1.54 %                   13   
7             1   0.15 %                11   1.69 %                   11   
8             1   0.15 %                12   1.85 %                   10   
9             3   0.46 %                15   2.31 %                    9   
10            6   0.92 %                21   3.24 %                    8   
11           10   1.54 %                31   4.78 %                    7   
12            5   0.77 %                36   5.55 %                    6   
13           14   2.16 %                50    7.7 %                    5   
14           30   4.62 %                80  12.33 %                    4   
15           32   4.93 %               112  17.26 %                    3   
16          105  16.18 %               217  33.44 %                    2   
17          432  66.56 %               649  100.0 %                    1   
-
    Tot Documents published  Num Documents Tot Documents  Bradford's Group  
0                        50             50        3.84 %                 1  
1                        22             72        5.53 %                 1  
2                        18             90        6.92 %                 1  
3                        16            106        8.15 %                 1  
4                        30            136       10.45 %                 1  
5                        28            164       12.61 %                 1  
6                        13            177        13.6 %                 1  
7                        11            188       14.45 %                 1  
8                        10            198       15.22 %                 1  
9                        27            225       17.29 %                 1  
10                       48            273       20.98 %                 1  
11                       70            343       26.36 %                 1  
12                       30            373       28.67 %                 1  
13                       70            443       34.05 %                 2  
14                      120            563       43.27 %                 2  
15                       96            659       50.65 %                 2  
16                      210            869       66.79 %                 3  
17                      432           1301       100.0 %                 3  
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
                "document_id",
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
