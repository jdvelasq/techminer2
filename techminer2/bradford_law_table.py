# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _bradford_law_table:

Bradford's Law Table
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> print(tm2p.bradford_law_table(
...     root_dir=root_dir,
... ).to_markdown())
|    |   Num Sources | %       |   Acum Num Sources | % Acum   |   Documents published |   Tot Documents published |   Num Documents | Tot Documents   |   Bradford's Group |
|---:|--------------:|:--------|-------------------:|:---------|----------------------:|--------------------------:|----------------:|:----------------|-------------------:|
|  0 |             6 | 13.04 % |                  6 | 13.04 %  |                     2 |                        12 |              12 | 23.08 %         |                  1 |
|  1 |            40 | 86.96 % |                 46 | 100.0 %  |                     1 |                        40 |              52 | 100.0 %         |                  3 |


"""
import numpy as np
import pandas as pd

from ._read_records import read_records


def bradford_law_table(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records["num_documents"] = 1

    sources = records.groupby("source_title", as_index=True).agg(
        {
            "num_documents": np.sum,
        }
    )
    sources = sources[["num_documents"]]
    sources = sources.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(sources), 2)) + " %" for a in sources]
    sources = pd.DataFrame(
        {
            "Num Sources": sources.tolist(),
            "%": w,
            "Documents published": sources.index,
        }
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
        lambda w: str(round(w / sources["Num Documents"].max() * 100, 2))
        + " %"
    )

    bradford1 = int(len(records) / 3)
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
