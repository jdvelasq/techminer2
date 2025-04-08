# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Data Frame
===============================================================================

>>> from techminer2.database.metrics.performance import DataFrame
>>> (
...     DataFrame()
...     #
...     # FIELD:
...     .with_field("raw_author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     #
...     .run()
... )
                      rank_occ  rank_gcs  ...  m_index                      counters
raw_author_keywords                       ...
FINTECH                      1         1  ...     7.75               FINTECH 31:5168
INNOVATION                   2         2  ...     1.75            INNOVATION 07:0911
FINANCIAL_SERVICES           3         4  ...     1.00    FINANCIAL_SERVICES 04:0667
FINANCIAL_INCLUSION          4         5  ...     0.75   FINANCIAL_INCLUSION 03:0590
FINANCIAL_TECHNOLOGY         5        15  ...     1.00  FINANCIAL_TECHNOLOGY 03:0461
CROWDFUNDING                 6        23  ...     1.00          CROWDFUNDING 03:0335
MARKETPLACE_LENDING          7        25  ...     1.50   MARKETPLACE_LENDING 03:0317
BUSINESS_MODELS              8         3  ...     1.00       BUSINESS_MODELS 02:0759
CYBER_SECURITY               9        21  ...     1.00        CYBER_SECURITY 02:0342
CASE_STUDY                  10        22  ...     0.67            CASE_STUDY 02:0340
<BLANKLINE>
[10 rows x 17 columns]



"""
from ...._internals.mixins import ParamsMixin
from ..._internals.io import (
    internal__load_filtered_records_from_database,
    internal__load_user_stopwords,
)

SELECTED_COLUMNS = {
    "OCC": [
        "OCC",
        "global_citations",
        "local_citations",
        "_name_",
    ],
    #
    "global_citations": [
        "global_citations",
        "local_citations",
        "OCC",
        "_name_",
    ],
    # -------------------------------------------
    "local_citations": [
        "local_citations",
        "global_citations",
        "OCC",
        "_name_",
    ],
}


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_load_the_database(self):
        self.data_frame = internal__load_filtered_records_from_database(
            params=self.params
        )

    # -------------------------------------------------------------------------
    def step_02_select_metric_fields(self):
        self.data_frame = (
            self.data_frame[
                [
                    self.params.field,
                    "global_citations",
                    "local_citations",
                    "year",
                ]
            ]
            .dropna()
            .copy()
        )

    # -------------------------------------------------------------------------
    def step_03_explode_data_frame(self):

        # Explode terms in field
        data_frame = self.data_frame.copy()
        data_frame[self.params.field] = data_frame[self.params.field].str.split("; ")
        data_frame = data_frame.explode(self.params.field)

        # Add calculated columns to compute impact metrics
        # Sorts the data frame
        data_frame = data_frame.sort_values(
            [self.params.field, "global_citations", "local_citations"],
            ascending=[True, False, False],
        )

        data_frame = data_frame.assign(
            position=data_frame.groupby(self.params.field).cumcount() + 1
        )

        data_frame = data_frame.assign(
            position2=data_frame.position.map(lambda w: w * w)
        )

        data_frame = data_frame.reset_index(drop=True)

        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def step_04_compute_initial_performance_metrics(self):
        self.data_frame["OCC"] = 1
        grouped = self.data_frame.groupby(self.params.field).agg(
            {
                "OCC": "sum",
                "global_citations": "sum",
                "local_citations": "sum",
                "year": "min",
            }
        )
        grouped = grouped.rename(columns={"year": "first_publication_year"})
        grouped["last_year"] = self.data_frame.year.max()
        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_05_compute_derived_performance_metrics(self):

        grouped = self.grouped.copy()
        grouped["age"] = grouped["last_year"] - grouped["first_publication_year"] + 1
        grouped["global_citations_per_year"] = (
            grouped["global_citations"] / grouped["age"]
        )
        grouped["local_citations_per_year"] = (
            grouped["local_citations"] / grouped["age"]
        )

        grouped["global_citations_per_document"] = (
            grouped["global_citations"] / grouped["OCC"]
        )
        grouped["local_citations_per_document"] = (
            grouped["local_citations"] / grouped["OCC"]
        )
        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_06_compute_impact_metrics(self):

        data_frame = self.data_frame.copy()
        grouped = self.grouped.copy()

        # H-index
        h_indexes = data_frame.query("global_citations >= position")
        h_indexes = h_indexes.groupby(self.params.field, as_index=True).agg(
            {"position": "max"}
        )
        h_indexes = h_indexes.rename(columns={"position": "h_index"})
        grouped.loc[h_indexes.index, "h_index"] = h_indexes.astype(int)
        grouped["h_index"] = grouped["h_index"].fillna(0)

        # G-index
        g_indexes = data_frame.query("global_citations >= position2")
        g_indexes = g_indexes.groupby(self.params.field, as_index=True).agg(
            {"position": "max"}
        )
        g_indexes = g_indexes.rename(columns={"position": "g_index"})
        grouped.loc[g_indexes.index, "g_index"] = g_indexes.astype(int)
        grouped["g_index"] = grouped["g_index"].fillna(0)

        # M-index
        grouped = grouped.assign(m_index=grouped.h_index / grouped.age)
        grouped["m_index"] = grouped.m_index.round(decimals=2)

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def sort_data_frame_by_metric(self, data_frame, metric):

        data_frame = data_frame.copy()
        data_frame["_name_"] = data_frame.index.tolist()

        columns = SELECTED_COLUMNS[metric]
        ascending = [False] * (len(columns) - 1) + [True]

        data_frame = data_frame.sort_values(columns, ascending=ascending)
        data_frame = data_frame.drop(columns=["_name_"])

        return data_frame

    # -------------------------------------------------------------------------
    def step_07_remove_stopwords(self):

        grouped = self.grouped.copy()
        stopwords = internal__load_user_stopwords(params=self.params)
        grouped = grouped.drop(stopwords, axis=0, errors="ignore")
        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_08_add_rank_columns(self):

        grouped = self.grouped.copy()

        grouped = self.sort_data_frame_by_metric(grouped, "local_citations")
        grouped.insert(0, "rank_lcs", range(1, len(grouped) + 1))

        grouped = self.sort_data_frame_by_metric(grouped, "global_citations")
        grouped.insert(0, "rank_gcs", range(1, len(grouped) + 1))

        grouped = self.sort_data_frame_by_metric(grouped, "OCC")
        grouped.insert(0, "rank_occ", range(1, len(grouped) + 1))

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_09_filter_by_term_occurrences_range(self):

        grouped = self.grouped.copy()

        if self.params.term_occurrences_range is None:
            return grouped

        min_value, max_value = self.params.term_occurrences_range

        if min_value is not None:
            grouped = grouped[grouped["OCC"] >= min_value]
        if max_value is not None:
            grouped = grouped[grouped["OCC"] <= max_value]

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_10_filter_by_term_citations_range(self):

        grouped = self.grouped.copy()

        if self.params.term_citations_range is None:
            return grouped

        min_value, max_value = self.params.term_citations_range

        if min_value is not None:
            grouped = grouped[grouped["global_citations"] >= min_value]
        if max_value is not None:
            grouped = grouped[grouped["global_citations"] <= max_value]

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_11_filter_by_terms_in(self):

        grouped = self.grouped.copy()

        if self.params.terms_in is None:
            return grouped

        if self.params.terms_in is not None:
            grouped = grouped.loc[self.params.terms_in, :]

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_12_filter_by_top_n_terms(self):

        grouped = self.sort_data_frame_by_metric(
            data_frame=self.grouped.copy(),
            metric=self.params.terms_order_by,
        )

        if self.params.top_n is not None:
            grouped = grouped.head(self.params.top_n)

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_13_check_field_types(self):

        grouped = self.grouped.copy()

        if "OCC" in grouped.columns:
            grouped["OCC"] = grouped["OCC"].astype(int)

        if "global_citations" in grouped.columns:
            grouped["global_citations"] = grouped["global_citations"].astype(int)

        if "local_citations" in grouped.columns:
            grouped["local_citations"] = grouped["local_citations"].astype(int)

        if "h_index" in grouped.columns:
            grouped["h_index"] = grouped["h_index"].astype(int)

        if "g_index" in grouped.columns:
            grouped["g_index"] = grouped["g_index"].astype(int)

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def step_14_add_term_with_counters_column(self):

        grouped = self.grouped.copy()
        grouped["counters"] = grouped.index.astype(str)

        # n_zeros = len(str(grouped["OCC"].max()))
        # grouped["counters"] += " " + grouped["OCC"].map(lambda x: f"{x:0{n_zeros}d}")
        grouped["counters"] += " " + grouped["OCC"].map(lambda x: f"{x:d}")

        # n_zeros = len(str(grouped["global_citations"].max()))
        # grouped["counters"] += ":" + grouped["global_citations"].map(
        #     lambda x: f"{x:0{n_zeros}d}"
        # )
        grouped["counters"] += ":" + grouped["global_citations"].map(lambda x: f"{x:d}")

        self.grouped = grouped

    # -------------------------------------------------------------------------
    def run(self):

        self.step_01_load_the_database()
        self.step_02_select_metric_fields()
        self.step_03_explode_data_frame()
        self.step_04_compute_initial_performance_metrics()
        self.step_05_compute_derived_performance_metrics()
        self.step_06_compute_impact_metrics()
        self.step_07_remove_stopwords()
        self.step_08_add_rank_columns()
        self.step_09_filter_by_term_occurrences_range()
        self.step_10_filter_by_term_citations_range()
        self.step_11_filter_by_terms_in()
        self.step_12_filter_by_top_n_terms()
        self.step_13_check_field_types()
        self.step_14_add_term_with_counters_column()

        return self.grouped
