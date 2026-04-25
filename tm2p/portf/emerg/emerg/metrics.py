"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit
    >>> from tm2p.portfolio.emergence.emergence import Metrics
    >>> df = (
    ...     Metrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     # EMERGENCE:
    ...     .using_emergence_baseline_periods(3)
    ...     .using_emergence_recent_periods(3)
    ...     .using_emergence_novelty_threshold(0.15)
    ...     .using_emergence_min_total_records(7)
    ...     .using_emergence_min_active_periods(3)
    ...     .using_emergence_ratio_threshold(0.5)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE


"""

import numpy as np

from tm2p._intern import ParamsMixin
from tm2p.enum import UnitOrderBy
from tm2p.portf.perf_metric.annual.metrics import Metrics as TrendMetricsDataFrame
from tm2p.portf.perf_metric.main import Metrics as GeneralMetricsDataFrame
from tm2p.portf.perf_metric.trend import Trends


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def _step_1_compute_term_occurrences_by_year(self):

        return (
            Trends()
            .update(**self.params.__dict__)
            #
            .using_cumulative_sum(False)
            #
            .having_top_n_units(None)
            .having_units_ordered_by(UnitOrderBy.OCC)
            .having_unit_occurrence_between(None, None)
            .having_unit_global_citation_between(None, None)
            .having_units_in(None)
            #
            .run()
        )

    def _step_2_compute_base_indicators(self, occurrences_by_year):
        #
        baseline_periods = self.params.emergence_baseline_periods
        recent_periods = self.params.emergence_recent_periods
        #
        data_frame = occurrences_by_year.sum(axis=1).to_frame()
        data_frame.columns = ["OCC"]
        data_frame["OCC_BASELINE"] = occurrences_by_year.iloc[:, :baseline_periods].sum(
            axis=1
        )
        data_frame["OCC_RECENT"] = occurrences_by_year.iloc[:, -recent_periods:].sum(
            axis=1
        )
        data_frame["NONZERO_YEARS"] = (occurrences_by_year > 0).sum(axis=1)
        #
        return data_frame

    def _step_3_compute_records_by_bas_period(self):
        baseline_periods = self.params.emergence_baseline_periods
        return (
            TrendMetricsDataFrame()
            .update(**self.params.__dict__)
            .run()
            .OCC[:baseline_periods]
            .sum()
        )

    def run(self):

        occurrences_by_year = self._step_1_compute_term_occurrences_by_year()
        data_frame = self._step_2_compute_base_indicators(occurrences_by_year)
        records_by_base_period = self._step_3_compute_records_by_bas_period()
        data_frame["selected"] = True

        #
        # Threshold: The term  appear in 15% or less of the base period records
        #
        novelty_threshold = self.params.emergence_novelty_threshold
        data_frame["selected"] = data_frame["selected"] & (
            data_frame["OCC_BASELINE"] / records_by_base_period <= novelty_threshold
        )

        #
        # Threshold: The term appears in at least 'total_records_threshold' records
        #
        total_records_threshold = self.params.emergence_min_total_records
        data_frame["selected"] = data_frame["selected"] & (
            data_frame["OCC"] >= total_records_threshold
        )

        #
        # Threshold: The term appears in at leat 'periods_with_at_least_one_record' periods
        #
        periods_with_at_least_one_record = self.params.emergence_min_active_periods
        data_frame["selected"] = data_frame["selected"] & (
            data_frame["NONZERO_YEARS"] >= periods_with_at_least_one_record
        )

        #
        # Threshold: The growth reate of the terms must be 'ratio_threshold' times
        # of the growth rate of the dataset
        #

        cum_occurrences_by_year = (
            Trends()
            .update(**self.params.__dict__)
            #
            .using_cumulative_sum(True)
            #
            .having_top_n_units(None)
            .having_units_ordered_by(UnitOrderBy.OCC)
            .having_unit_occurrence_between(None, None)
            .having_unit_global_citation_between(None, None)
            .having_units_in(None)
            #
            .run()
        )

        n_columns = cum_occurrences_by_year.columns.max()

        data_frame["PO"] = cum_occurrences_by_year.where(
            cum_occurrences_by_year > 0, np.inf
        ).min(axis=1)

        data_frame["PF"] = cum_occurrences_by_year.max(axis=1)

        data_frame["NP"] = n_columns - cum_occurrences_by_year.where(
            cum_occurrences_by_year > 0, np.inf
        ).idxmin(axis=1)

        data_frame["GROWTH_RATE"] = 100.0 * (
            np.power(
                data_frame["PF"].astype(float) / data_frame["PO"].astype(float),
                1.0 / data_frame["NP"].astype(float),
            )
            - 1
        )

        global_growth_rate = (
            GeneralMetricsDataFrame()
            .update(**self.params.__dict__)
            .run()
            .loc[("GENERAL", "Annual growth rate %"), "VALUE"]
        )

        data_frame["GROWTH_RATE_RATIO"] = data_frame["GROWTH_RATE"].map(
            lambda x: x / global_growth_rate
        )

        ratio_threshold = self.params.emergence_ratio_threshold
        data_frame["selected"] = data_frame["selected"] & (
            data_frame["GROWTH_RATE_RATIO"] >= ratio_threshold
        )

        # n_years = max(self.records.year) - min(self.records.year) + 1
        # po_ = len(self.records.year[self.records.year == min(self.records.year)])
        # return round(100 * (np.power(self.n_records / po_, 1 / n_years) - 1), 2)

        #
        # NOTE: Used in the first versions of the package
        # Threshold: The ratio of records containing the term in the active period to
        # those in the base period must be at least 'ratio_threshold':1
        #
        # data_frame["selected"] = data_frame["selected"] & (
        #     data_frame["OCC_recent"] / data_frame["OCC_baseline"] >= ratio_threshold
        # )

        return data_frame[data_frame.selected].drop(columns=["selected"])
