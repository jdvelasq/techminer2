# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cross co-occurrence DataFrame 
===============================================================================


>>> from techminer2.pkgs.co_occurrence_matrix import DataFrame
>>> (
...     DataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(2, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # ROWS:
...     .with_other_field("authors")
...     .having_other_terms_in_top(None)
...     .having_other_terms_ordered_by(None)
...     .having_other_term_occurrences_between(2, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head(10)
                 rows                      columns  OCC
0  Jagtiani J. 3:0317              FINTECH 31:5168    3
1  Jagtiani J. 3:0317  MARKETPLACE_LENDING 03:0317    3
2    Dolata M. 2:0181              FINTECH 31:5168    2
3    Dolata M. 2:0181           INNOVATION 07:0911    2
4       Gai K. 2:0323              FINTECH 31:5168    2
5    Hornuf L. 2:0358              FINTECH 31:5168    2
6   Lemieux C. 2:0253              FINTECH 31:5168    2
7   Lemieux C. 2:0253  MARKETPLACE_LENDING 03:0317    2
8       Qiu M. 2:0323              FINTECH 31:5168    2
9   Schwabe G. 2:0181              FINTECH 31:5168    2


>>> from techminer2.pkgs.co_occurrence_matrix import DataFrame
>>> (
...     DataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(2, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # ROWS:
...     .with_other_field(None)
...     .having_other_terms_in_top(None)
...     .having_other_terms_ordered_by(None)
...     .having_other_term_occurrences_between(None, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head(10)
                           rows                       columns  OCC
0               FINTECH 31:5168               FINTECH 31:5168   31
1            INNOVATION 07:0911            INNOVATION 07:0911    7
2               FINTECH 31:5168            INNOVATION 07:0911    5
3            INNOVATION 07:0911               FINTECH 31:5168    5
4    FINANCIAL_SERVICES 04:0667    FINANCIAL_SERVICES 04:0667    4
5          CROWDFUNDING 03:0335          CROWDFUNDING 03:0335    3
6   FINANCIAL_INCLUSION 03:0590   FINANCIAL_INCLUSION 03:0590    3
7   FINANCIAL_INCLUSION 03:0590               FINTECH 31:5168    3
8    FINANCIAL_SERVICES 04:0667               FINTECH 31:5168    3
9  FINANCIAL_TECHNOLOGY 03:0461  FINANCIAL_TECHNOLOGY 03:0461    3


"""
from ...database.load import DatabaseLoader
from ...database.metrics.performance import DataFrame as PerformanceMetricsDataFrame
from ...internals.mixins import InputFunctionsMixin


class DataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_check_row_params(self):
        if self.params.other_field is None:
            self.with_other_field(
                self.params.field,
            )
            self.having_other_terms_in_top(
                self.params.top_n,
            )
            self.having_other_terms_ordered_by(
                self.params.terms_order_by,
            )
            self.having_other_term_occurrences_between(
                self.params.term_occurrences_range[0],
                self.params.term_occurrences_range[1],
            )
            self.having_other_term_citations_between(
                self.params.term_citations_range[0],
                self.params.term_citations_range[1],
            )
            self.having_other_terms_in(
                self.params.terms_in,
            )

    # -------------------------------------------------------------------------
    def _step_2_compute_column_peformance_metrics(self):
        return (
            PerformanceMetricsDataFrame().update_params(**self.params.__dict__).build()
        )

    # -------------------------------------------------------------------------
    def _step_3_compute_row_peformance_metrics(self):
        metrics = (
            PerformanceMetricsDataFrame()
            .update_params(**self.params.__dict__)
            .with_field(self.params.other_field)
            .having_terms_in_top(self.params.other_top_n)
            .having_terms_ordered_by(self.params.other_terms_order_by)
            .having_term_occurrences_between(
                self.params.term_occurrences_range[0],
                self.params.term_occurrences_range[1],
            )
            .having_term_citations_between(
                self.params.term_citations_range[0],
                self.params.term_citations_range[1],
            )
            .having_terms_in(self.params.terms_in)
            .build()
        )
        return metrics

    # -------------------------------------------------------------------------
    def _step_3_load_the_database(self):
        return DatabaseLoader().update_params(**self.params.__dict__).build()

    # -------------------------------------------------------------------------
    def _step_4_create_raw_matrix_list(self, records):
        #
        columns = self.params.field
        rows = self.params.other_field
        #
        raw_matrix_list = records[[columns]].copy()
        raw_matrix_list = raw_matrix_list.rename(columns={columns: "columns"})
        raw_matrix_list = raw_matrix_list.assign(rows=records[[rows]])
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_5_explode_matrix_list(self, raw_matrix_list, name, selected_terms):
        #
        raw_matrix_list[name] = raw_matrix_list[name].str.split(";")
        raw_matrix_list = raw_matrix_list.explode(name)
        raw_matrix_list[name] = raw_matrix_list[name].str.strip()
        raw_matrix_list = raw_matrix_list[raw_matrix_list[name].isin(selected_terms)]
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_6_compute_occurrences(self, raw_matrix_list):
        #
        raw_matrix_list["OCC"] = 1
        raw_matrix_list = raw_matrix_list.groupby(
            ["rows", "columns"], as_index=False
        ).aggregate("sum")
        #
        raw_matrix_list = raw_matrix_list.sort_values(
            ["OCC", "rows", "columns"], ascending=[False, True, True]
        )
        raw_matrix_list = raw_matrix_list.reset_index(drop=True)
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_7_build_mapping(self, data_frame):
        #
        data_frame["counters"] = data_frame.index.astype(str)

        n_zeros = len(str(data_frame["OCC"].max()))
        data_frame["counters"] += " " + data_frame["OCC"].map(
            lambda x: f"{x:0{n_zeros}d}"
        )

        n_zeros = len(str(data_frame["global_citations"].max()))
        data_frame["counters"] += ":" + data_frame["global_citations"].map(
            lambda x: f"{x:0{n_zeros}d}"
        )

        mapping = data_frame["counters"].to_dict()
        #
        return mapping

    # -------------------------------------------------------------------------
    def _step_8_rename_terms(self, raw_matrix_list, row_mapping, column_mapping):
        #
        raw_matrix_list["rows"] = raw_matrix_list["rows"].map(row_mapping)
        raw_matrix_list["columns"] = raw_matrix_list["columns"].map(column_mapping)
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def build(self):
        self._step_1_check_row_params()
        column_metrics = self._step_2_compute_column_peformance_metrics()
        row_metrics = self._step_3_compute_row_peformance_metrics()
        records = self._step_3_load_the_database()
        raw_matrix_list = self._step_4_create_raw_matrix_list(records)
        raw_matrix_list = self._step_5_explode_matrix_list(
            raw_matrix_list,
            "columns",
            column_metrics.index.tolist(),
        )
        raw_matrix_list = self._step_5_explode_matrix_list(
            raw_matrix_list,
            "rows",
            row_metrics.index.tolist(),
        )
        raw_matrix_list = self._step_6_compute_occurrences(raw_matrix_list)
        row_mapping = self._step_7_build_mapping(row_metrics)
        column_mapping = self._step_7_build_mapping(column_metrics)
        if self.params.term_counters:
            raw_matrix_list = self._step_8_rename_terms(
                raw_matrix_list, row_mapping, column_mapping
            )
        return raw_matrix_list
