# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
RPYS (Reference Publication Year Spectroscopy) Frame
===============================================================================


>>> from techminer2.rpys import rpys_frame
>>> rpys_frame(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... ).head()
      Num References  Median
1957               1    -1.0
1958               0     0.0
1959               0     0.0
1960               0     0.0
1961               0     0.0

"""
import pandas as pd  #  type: ignore

from .._core.read_filtered_database import read_filtered_database


def rpys_frame(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    references = read_filtered_database(
        root_dir=root_dir,
        database="references",
        year_filter=(None, None),
        cited_by_filter=(None, None),
        sort_by=None,
    )

    references = references[["year"]]
    references = references.dropna()
    references_by_year = references["year"].value_counts()

    year_min = references_by_year.index.min()
    year_max = references_by_year.index.max()
    years = list(range(year_min, year_max + 1))

    indicator = pd.DataFrame(
        {
            "Num References": 0,
        },
        index=years,
    )

    indicator.loc[references_by_year.index, "Num References"] = references_by_year
    indicator = indicator.sort_index(axis=0, ascending=True)
    indicator["Median"] = indicator["Num References"].rolling(window=5).median().fillna(0)

    indicator["Median"] = indicator["Median"] - indicator["Num References"]

    return indicator
