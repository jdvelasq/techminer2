"""
Core Sources
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> core_sources(directory)
   Num Sources        %  ...  Tot Documents Bradford's Group
0            1   1.49 %  ...         5.32 %                1
1            2   2.99 %  ...        13.83 %                1
2            4   5.97 %  ...         26.6 %                1
3            9  13.43 %  ...        45.74 %                2
4           51  76.12 %  ...        100.0 %                3
<BLANKLINE>
[5 rows x 9 columns]

>>> from pprint import pprint
>>> columns = core_sources(directory).columns.to_list()
>>> pprint(columns)
['Num Sources',
 '%',
 'Acum Num Sources',
 '% Acum',
 'Documents published',
 'Tot Documents published',
 'Num Documents',
 'Tot Documents',
 "Bradford's Group"]

"""

import numpy as np
import pandas as pd

from ._read_records import read_records
from .explode import explode


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
    documents = read_records(
        directory=directory, database="documents", use_filter=False
    )

    documents["num_documents"] = 1
    documents = explode(
        documents[
            [
                "source_title",
                "num_documents",
                "record_no",
            ]
        ],
        "source_title",
        sep="; ",
    )

    sources = documents.groupby("source_title", as_index=True).agg(
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
