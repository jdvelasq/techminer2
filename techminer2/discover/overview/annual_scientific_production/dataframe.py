"""
DataFrame
===============================================================================

Smoke tests:
    >>> from techminer2.discover.overview.annual_scientific_production import DataFrame
    >>> df = (
    ...     DataFrame()
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
    >>> df
             OCC  cum_OCC  ...  mean_local_citations  mean_local_citations_per_year
    PUBYEAR                ...
    2015       6        6  ...              0.000000                           0.00
    2016      18       24  ...              0.055556                           0.01
    2017      19       43  ...              0.105263                           0.01
    2018      18       61  ...              0.111111                           0.02
    2019      19       80  ...              0.631579                           0.11
    2020      20      100  ...              0.700000                           0.14
    2021      20      120  ...              0.450000                           0.11
    2022      20      140  ...              0.650000                           0.22
    2023      20      160  ...              1.100000                           0.55
    2024      20      180  ...              0.600000                           0.60
    <BLANKLINE>
    [10 rows x 11 columns]



"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_filtered_main_data

PUBYEAR = CorpusField.PUBYEAR.value
CIT_COUNT_GLOBAL = CorpusField.CIT_COUNT_GLOBAL.value
CIT_COUNT_LOCAL = CorpusField.CIT_COUNT_LOCAL.value


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_load_the_database(self):
        return load_filtered_main_data(params=self.params)

    # -------------------------------------------------------------------------
    def _step_2_select_columns(self, data_frame):
        columns = [PUBYEAR, CIT_COUNT_GLOBAL, CIT_COUNT_LOCAL]
        data_frame = data_frame[columns]
        data_frame = data_frame.assign(OCC=1)
        data_frame[PUBYEAR] = data_frame[PUBYEAR].astype(int)
        return data_frame

    # -------------------------------------------------------------------------
    def _step_3_group_by_year_and_sort(self, data_frame):
        data_frame = data_frame.groupby(PUBYEAR, as_index=True).sum()
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
            mean_global_citations=data_frame[CIT_COUNT_GLOBAL] / data_frame.OCC
        )
        data_frame = data_frame.assign(
            cum_global_citations=data_frame[CIT_COUNT_GLOBAL].cumsum()
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
            mean_local_citations=data_frame[CIT_COUNT_LOCAL] / data_frame.OCC
        )
        data_frame = data_frame.assign(
            cum_local_citations=data_frame[CIT_COUNT_LOCAL].cumsum()
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
                CIT_COUNT_GLOBAL,
                "cum_global_citations",
                "mean_global_citations",
                "mean_global_citations_per_year",
                CIT_COUNT_LOCAL,
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
