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


>>> from techminer2.pkgs.rpys import RPYSDataFrame
>>> (
...     RPYSDataFrame()
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .build()
... ).head()
      Num References  Median
2015               1    -1.0
2016               7    -7.0
2017              10   -10.0
2018              17   -17.0
2019              15    -5.0



"""
import pandas as pd  # type: ignore

from ...database.internals.io import internal__load_filtered_database
from ...internals.mixins import ParamsMixin


class RPYSDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        references = internal__load_filtered_database(params=self.params)

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
        indicator["Median"] = (
            indicator["Num References"].rolling(window=5).median().fillna(0)
        )

        indicator["Median"] = indicator["Median"] - indicator["Num References"]

        return indicator
