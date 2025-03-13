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


>>> from techminer2.packages.rpys import RPYSDataFrame
>>> (
...     RPYSDataFrame()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .run()
... ).head()
      Num References  Median
2015               1    -1.0
2016               7    -7.0
2017              10   -10.0
2018              17   -17.0
2019              15    -5.0



"""
import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_filtered_records_from_database


class RPYSDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        references = internal__load_filtered_records_from_database(params=self.params)

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
