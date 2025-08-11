# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Data Frame
===============================================================================


Example:
    >>> from techminer2.database.metrics.records_by_year import DataFrame

    >>> # Create, configure, and run the generator:
    >>> generator = (
    ...     DataFrame()
    ...     #
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = generator.run()
    >>> df.head()
          OCC  cum_OCC  ...  mean_local_citations  mean_local_citations_per_year
    year                ...
    2015    1        1  ...              5.000000                           1.00
    2016    7        8  ...              1.142857                           0.29
    2017   10       18  ...              2.600000                           0.87
    2018   17       35  ...              1.588235                           0.79
    2019   15       50  ...              0.133333                           0.13
    <BLANKLINE>
    [5 rows x 11 columns]



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_load_the_database(self):
        return internal__load_filtered_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_2_select_columns(self, data_frame):
        columns = ["year", "global_citations", "local_citations"]
        data_frame = data_frame[columns]
        data_frame = data_frame.assign(OCC=1)
        data_frame["year"] = data_frame["year"].astype(int)
        return data_frame

    # -------------------------------------------------------------------------
    def _step_3_group_by_year_and_sort(self, data_frame):
        data_frame = data_frame.groupby("year", as_index=True).sum()
        data_frame = data_frame.sort_index(ascending=True, axis=0)
        return data_frame

    # -------------------------------------------------------------------------
    def _step_4_compute_cumulated_documents(self, data_frame):
        data_frame = data_frame.assign(cum_OCC=data_frame.OCC.cumsum())
        data_frame.insert(1, "cum_OCC", data_frame.pop("cum_OCC"))
        return data_frame

    # -------------------------------------------------------------------------
    def _step_5_compute_citable_years(self, data_frame):
        current_year = data_frame.index.max()
        data_frame = data_frame.assign(
            citable_years=current_year - data_frame.index + 1
        )
        return data_frame

    # -------------------------------------------------------------------------
    def _step_6_compute_global_citations(self, data_frame):
        data_frame = data_frame.assign(
            mean_global_citations=data_frame.global_citations / data_frame.OCC
        )
        data_frame = data_frame.assign(
            cum_global_citations=data_frame.global_citations.cumsum()
        )
        data_frame = data_frame.assign(
            mean_global_citations_per_year=data_frame.mean_global_citations
            / data_frame.citable_years
        )
        data_frame.mean_global_citations_per_year = (
            data_frame.mean_global_citations_per_year.round(2)
        )
        return data_frame

    # -------------------------------------------------------------------------
    def _step_7_compute_local_citations(self, data_frame):
        data_frame = data_frame.assign(
            mean_local_citations=data_frame.local_citations / data_frame.OCC
        )
        data_frame = data_frame.assign(
            cum_local_citations=data_frame.local_citations.cumsum()
        )
        data_frame = data_frame.assign(
            mean_local_citations_per_year=data_frame.mean_local_citations
            / data_frame.citable_years
        )
        data_frame.mean_local_citations_per_year = (
            data_frame.mean_local_citations_per_year.round(2)
        )
        return data_frame

    # -------------------------------------------------------------------------
    def _step_8_reorder_columns(self, data_frame):
        data_frame = data_frame[
            [
                "OCC",
                "cum_OCC",
                "citable_years",
                "global_citations",
                "cum_global_citations",
                "mean_global_citations",
                "mean_global_citations_per_year",
                "local_citations",
                "cum_local_citations",
                "mean_local_citations",
                "mean_local_citations_per_year",
            ]
        ]
        return data_frame

    # -------------------------------------------------------------------------
    def run(self):

        data_frame = self._step_1_load_the_database()
        data_frame = self._step_2_select_columns(data_frame)
        data_frame = self._step_3_group_by_year_and_sort(data_frame)
        data_frame = self._step_4_compute_cumulated_documents(data_frame)
        data_frame = self._step_5_compute_citable_years(data_frame)
        data_frame = self._step_6_compute_global_citations(data_frame)
        data_frame = self._step_7_compute_local_citations(data_frame)
        data_frame = self._step_8_reorder_columns(data_frame)

        return data_frame


#
