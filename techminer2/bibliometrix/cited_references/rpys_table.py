# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
RPYS (Reference Publication Year Spectroscopy)
===============================================================================

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> tm2.rpys_table(root_dir=root_dir).head()
      Num References  Median
1937               1    -1.0
1938               0     0.0
1939               0     0.0
1940               0     0.0
1941               0     0.0

"""


import pandas as pd

from ...._read_records import read_records


def rpys_table(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Reference Publication Year Spectroscopy."""

    references = read_records(
        root_dir=root_dir,
        database="references",
        year_filter=(None, None),
        cited_by_filter=(None, None),
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

    indicator.loc[
        references_by_year.index, "Num References"
    ] = references_by_year
    indicator = indicator.sort_index(axis=0, ascending=True)
    indicator["Median"] = (
        indicator["Num References"].rolling(window=5).median().fillna(0)
    )

    indicator["Median"] = indicator["Median"] - indicator["Num References"]
    return indicator
