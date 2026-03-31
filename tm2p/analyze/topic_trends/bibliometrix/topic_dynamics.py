"""
Dataframe
===============================================================================

Smoke tests:
    >>> from tm2p import Field
    >>> from tm2p.analyze.topic_trends.bibliometrix.topic_dynamics import TopicDynamics
    >>> df = (
    ...     TopicDynamics()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .having_items_per_year(5)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    YEAR                            OCC  global_citations  year_q1  year_med  year_q3  rn  height  width
    AUTHKW_RAW
    biometric 001:00001               1                 1     2015      2015     2015   0    0.15      1
    fast identity online 001:00001    1                 1     2015      2015     2015   1    0.15      1
    fido 001:00001                    1                 1     2015      2015     2015   2    0.15      1
    password 001:00001                1                 1     2015      2015     2015   3    0.15      1
    pki 001:00001                     1                 1     2015      2015     2015   4    0.15      1


    >>> df = (
    ...     TopicDynamics()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .having_items_per_year(5)
    ...     .having_items_in(
    ...         [
    ...             "fintech",
    ...             "blockchain",
    ...             "artificial intelligence",
    ...         ]
    ...     )
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    YEAR                               OCC  global_citations  year_q1  year_med  year_q3  rn    height  width
    AUTHKW_RAW
    blockchain 011:02023                11              2023     2018      2020     2022   0  0.172569      5
    fintech 117:25478                  117             25478     2018      2021     2023   0  0.970000      6
    artificial intelligence 008:01915    8              1915     2020      2020     2023   1  0.150000      4


"""

import numpy as np

from tm2p._intern import ParamsMixin
from tm2p.analyze.trends import Trends


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

        self.terms_by_year["year_q1"] = year_q1
        self.terms_by_year["year_med"] = year_med
        self.terms_by_year["year_q3"] = year_q3

    # ---------------------------------------------------------------------------
    def internal__extract_total_occurrences_and_citations(self):

        self.terms_by_year = self.terms_by_year.assign(
            OCC=self.terms_by_year.index.map(
                lambda x: int(x.split(" ")[-1].split(":")[0])
            )
        )
        self.terms_by_year = self.terms_by_year.assign(
            global_citations=self.terms_by_year.index.map(
                lambda x: int(x.split(" ")[-1].split(":")[1])
            )
        )
        self.terms_by_year = self.terms_by_year[
            ["OCC", "global_citations", "year_q1", "year_med", "year_q3"]
        ]

        self.terms_by_year = self.terms_by_year.sort_values(
            by=["year_med", "OCC", "global_citations"],
            ascending=[True, False, False],
        )

    # ---------------------------------------------------------------------------
    def internal__select_top_terms_per_year(self):

        self.terms_by_year = self.terms_by_year.assign(
            rn=self.terms_by_year.groupby(["year_med"]).cumcount()
        ).sort_values(["year_med", "rn"], ascending=[True, True])

        self.terms_by_year = self.terms_by_year.query(
            f"rn < {self.params.items_per_year}"
        )

    # ---------------------------------------------------------------------------
    def internal__compute_bar_height_and_width(self):

        min_occ = self.terms_by_year.OCC.min()
        max_occ = self.terms_by_year.OCC.max()

        self.terms_by_year = self.terms_by_year.assign(
            height=0.15
            + 0.82 * (self.terms_by_year.OCC - min_occ) / (max_occ - min_occ)
        )

        self.terms_by_year = self.terms_by_year.assign(
            width=self.terms_by_year.year_q3 - self.terms_by_year.year_q1 + 1
        )

        self.terms_by_year = self.terms_by_year.sort_values(
            ["year_q1", "width", "height"], ascending=[True, True, True]
        )

    # ---------------------------------------------------------------------------
    def run(self):
        self.internal__compute_top_terms_by_year()
        self.internal__compute_percentiles_per_term_by_year()
        self.internal__extract_total_occurrences_and_citations()
        self.internal__select_top_terms_per_year()
        self.internal__compute_bar_height_and_width()
        return self.terms_by_year


#
