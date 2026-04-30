"""
Dataframe
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.emerg.topic_trend.bibliometrix import TopicDynamics
    >>> df = (
    ...     TopicDynamics()
    ...     #
    ...     # FIELD:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     .having_top_n_units_per_year(5)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)    
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
    YEAR                             OCC   GCS  YEAR_Q1  YEAR_MED  YEAR_Q3  rn    HEIGHT  WIDTH
    CONCEPT_NORM                                                                               
    neural network 0056:000412        56   412     2022      2023     2024   3  0.150000      3
    controllers 0067:001148           67  1148     2022      2023     2024   2  0.158061      3
    cloud 0076:001385                 76  1385     2022      2023     2024   1  0.164656      3
    learning algorithms 0094:001714   94  1714     2022      2023     2025   0  0.177846      4
    edge ai 0118:001164              118  1164     2023      2025     2025   3  0.195433      3


    >>> df = (
    ...     TopicDynamics()
    ...     #
    ...     # FIELD:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     .having_top_n_units_per_year(5)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
from tm2p.portfolio.perform_metr.trend import Trends

GCS = "GCS"
WIDTH = "WIDTH"
HEIGHT = "HEIGHT"
YEAR_Q1 = "YEAR_Q1"
YEAR_MED = "YEAR_MED"
YEAR_Q3 = "YEAR_Q3"


class TopicDynamics(
    ParamsMixin,
):
    """:meta private:"""

    # ---------------------------------------------------------------------------
    def internal__compute_top_terms_by_year(self):
        self.terms_by_year = (
            Trends()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .update(term_counters=True)
            .run()
        )

    # ---------------------------------------------------------------------------
    def internal__compute_percentiles_per_term_by_year(self):

        year_q1 = []
        year_med = []
        year_q3 = []

        for _, row in self.terms_by_year.iterrows():
            sequence = []
            for item, year in zip(row, self.terms_by_year.columns):
                if item > 0:
                    sequence.extend([year] * int(item))

            year_q1.append(int(round(np.percentile(sequence, 25))))
            year_med.append(int(round(np.percentile(sequence, 50))))
            year_q3.append(int(round(np.percentile(sequence, 75))))

        self.terms_by_year["YEAR_Q1"] = year_q1
        self.terms_by_year["YEAR_MED"] = year_med
        self.terms_by_year["YEAR_Q3"] = year_q3

    # ---------------------------------------------------------------------------
    def internal__extract_total_occurrences_and_citations(self):

        self.terms_by_year = self.terms_by_year.assign(
            OCC=self.terms_by_year.index.map(
                lambda x: int(x.split(" ")[-1].split(":")[0])
            )
        )
        self.terms_by_year = self.terms_by_year.assign(
            GCS=self.terms_by_year.index.map(
                lambda x: int(x.split(" ")[-1].split(":")[1])
            )
        )
        self.terms_by_year = self.terms_by_year[
            ["OCC", "GCS", "YEAR_Q1", "YEAR_MED", "YEAR_Q3"]
        ]

        self.terms_by_year = self.terms_by_year.sort_values(
            by=["YEAR_MED", "OCC", "GCS"],
            ascending=[True, False, False],
        )

    # ---------------------------------------------------------------------------
    def internal__select_top_terms_per_year(self):

        self.terms_by_year = self.terms_by_year.assign(
            rn=self.terms_by_year.groupby(["YEAR_MED"]).cumcount()
        ).sort_values(["YEAR_MED", "rn"], ascending=[True, True])

        self.terms_by_year = self.terms_by_year.query(
            f"rn < {self.params.top_n_units_per_year}"
        )

    # ---------------------------------------------------------------------------
    def internal__compute_bar_height_and_width(self):

        min_occ = self.terms_by_year.OCC.min()
        max_occ = self.terms_by_year.OCC.max()

        self.terms_by_year = self.terms_by_year.assign(
            HEIGHT=0.15
            + 0.82 * (self.terms_by_year.OCC - min_occ) / (max_occ - min_occ)
        )

        self.terms_by_year = self.terms_by_year.assign(
            WIDTH=self.terms_by_year.YEAR_Q3 - self.terms_by_year.YEAR_Q1 + 1
        )

        self.terms_by_year = self.terms_by_year.sort_values(
            ["YEAR_Q1", "WIDTH", "HEIGHT"], ascending=[True, True, True]
        )

    # ---------------------------------------------------------------------------
    def run(self):
        self.internal__compute_top_terms_by_year()
        self.internal__compute_percentiles_per_term_by_year()
        self.internal__extract_total_occurrences_and_citations()
        self.internal__select_top_terms_per_year()
        self.internal__compute_bar_height_and_width()
        return self.terms_by_year
