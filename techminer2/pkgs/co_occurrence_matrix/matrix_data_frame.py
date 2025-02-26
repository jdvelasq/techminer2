# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Matrix 
===============================================================================


>>> from techminer2.pkgs.co_occurrence_matrix import MatrixDataFrame
>>> (
...     MatrixDataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # ROWS:
...     .with_other_field("authors")
...     .having_other_terms_in_top(None)
...     .having_other_terms_ordered_by("OCC")
...     .having_other_term_occurrences_between(2, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head(10)
columns               FINTECH 31:5168  ...  CASE_STUDY 02:0340
rows                                   ...                    
Jagtiani J. 3:0317                  3  ...                   0
Gomber P. 2:1065                    1  ...                   0
Hornuf L. 2:0358                    2  ...                   0
Gai K. 2:0323                       2  ...                   0
Qiu M. 2:0323                       2  ...                   0
Sun X. 2:0323                       2  ...                   0
Lemieux C. 2:0253                   2  ...                   0
Dolata M. 2:0181                    2  ...                   0
Schwabe G. 2:0181                   2  ...                   0
Zavolokina L. 2:0181                2  ...                   0
<BLANKLINE>
[10 rows x 10 columns]

>>> from techminer2.pkgs.co_occurrence_matrix import MatrixDataFrame
>>> (
...     MatrixDataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head(10)
columns                       FINTECH 31:5168  ...  CASE_STUDY 02:0340
rows                                           ...                    
FINTECH 31:5168                            31  ...                   2
INNOVATION 07:0911                          5  ...                   0
FINANCIAL_SERVICES 04:0667                  3  ...                   0
FINANCIAL_INCLUSION 03:0590                 3  ...                   1
FINANCIAL_TECHNOLOGY 03:0461                2  ...                   0
CROWDFUNDING 03:0335                        2  ...                   0
MARKETPLACE_LENDING 03:0317                 3  ...                   0
BUSINESS_MODELS 02:0759                     2  ...                   0
CYBER_SECURITY 02:0342                      2  ...                   0
CASE_STUDY 02:0340                          2  ...                   2
<BLANKLINE>
[10 rows x 10 columns]


>>> # Submatrix of associated terms to FINTECH, INNOVATION, and FINANCIAL_SERVICES
>>> from techminer2.pkgs.co_occurrence_matrix import MatrixDataFrame
>>> (
...     MatrixDataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # ROWS:
...     .with_other_field("authors")
...     .having_other_terms_in_top(None)
...     .having_other_terms_ordered_by("OCC")
...     .having_other_term_occurrences_between(2, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(
...         {
...             "author_keywords": ["FINTECH", "INNOVATION", "FINANCIAL_SERVICES"],
...         },
...     )
...     #
...     .build()
... )
columns              FINTECH 31:5168  ...  TECHNOLOGY 02:0310
rows                                  ...                    
Jagtiani J. 3:317                  3  ...                   0
Hornuf L. 2:358                    2  ...                   0
Gai K. 2:323                       2  ...                   0
Qiu M. 2:323                       2  ...                   0
Sun X. 2:323                       2  ...                   0
Lemieux C. 2:253                   2  ...                   0
Dolata M. 2:181                    2  ...                   0
Schwabe G. 2:181                   2  ...                   0
Zavolokina L. 2:181                2  ...                   0
<BLANKLINE>
[9 rows x 10 columns]

>>> # Submatrix of associated terms to FINTECH, INNOVATION, and FINANCIAL_SERVICES
>>> from techminer2.pkgs.co_occurrence_matrix import MatrixDataFrame
>>> (
...     MatrixDataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(
...         {
...             "author_keywords": ["FINTECH", "INNOVATION", "FINANCIAL_SERVICES"],
...         },
...     )
...     #
...     .build()
... )
columns                       FINTECH 31:5168  ...  TECHNOLOGY 02:0310
rows                                           ...                    
FINTECH 31:5168                            31  ...                   1
INNOVATION 07:0911                          5  ...                   2
FINANCIAL_SERVICES 04:0667                  3  ...                   1
FINANCIAL_INCLUSION 03:0590                 3  ...                   0
MARKETPLACE_LENDING 03:0317                 3  ...                   0
BUSINESS_MODELS 02:0759                     2  ...                   0
FINANCIAL_TECHNOLOGY 02:0390                2  ...                   0
CYBER_SECURITY 02:0342                      2  ...                   0
CASE_STUDY 02:0340                          2  ...                   0
TECHNOLOGY 02:0310                          1  ...                   2
<BLANKLINE>
[10 rows x 10 columns]



"""
from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_filtered_database
from ...database.metrics.performance import DataFrame as PerformanceMetricsDataFrame


class MatrixDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_check_row_params(self):
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
    def _step_02_compute_column_peformance_metrics(self):
        return PerformanceMetricsDataFrame().update(**self.params.__dict__).build()

    # -------------------------------------------------------------------------
    def _step_03_compute_row_peformance_metrics(self):
        metrics = (
            PerformanceMetricsDataFrame()
            .update(**self.params.__dict__)
            .with_field(self.params.other_field)
            .having_terms_in_top(self.params.other_top_n)
            .having_terms_ordered_by(self.params.other_terms_order_by)
            .having_term_occurrences_between(
                self.params.other_term_occurrences_range[0],
                self.params.other_term_occurrences_range[1],
            )
            .having_term_citations_between(
                self.params.other_term_citations_range[0],
                self.params.other_term_citations_range[1],
            )
            .having_terms_in(self.params.other_terms_in)
            .build()
        )
        return metrics

    # -------------------------------------------------------------------------
    def _step_04_load_the_database(self):
        return internal__load_filtered_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_05_create_raw_matrix_list(self, records):
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
    def _step_06_explode_matrix_list(self, raw_matrix_list, name, selected_terms):
        #
        raw_matrix_list[name] = raw_matrix_list[name].str.split(";")
        raw_matrix_list = raw_matrix_list.explode(name)
        raw_matrix_list[name] = raw_matrix_list[name].str.strip()
        raw_matrix_list = raw_matrix_list[raw_matrix_list[name].isin(selected_terms)]
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_07_compute_occurrences(self, raw_matrix_list):
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
    def _step_08_build_mapping(self, data_frame):
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
    def _step_09_rename_terms(self, raw_matrix_list, row_mapping, column_mapping):
        #
        raw_matrix_list["rows"] = raw_matrix_list["rows"].map(row_mapping)
        raw_matrix_list["columns"] = raw_matrix_list["columns"].map(column_mapping)
        #
        return raw_matrix_list

    # -------------------------------------------------------------------------
    def _step_10_pivot_matrix_list(self, matrix_list):
        matrix = matrix_list.pivot(
            index=matrix_list.columns[0],
            columns=matrix_list.columns[1],
            values=matrix_list.columns[2],
        )
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)
        return matrix

    # -------------------------------------------------------------------------
    def _step_11_check_terms(self, matrix, row_mapping, col_mapping):

        for _, value in row_mapping.items():
            if value not in matrix.index:
                matrix.loc[value] = 0

        for _, value in col_mapping.items():
            if value not in matrix.columns:
                matrix[value] = 0

        return matrix

    # -------------------------------------------------------------------------
    def _step_12_sort_matrix_axis(self, matrix):
        matrix_cols = matrix.columns.tolist()
        matrix_rows = matrix.index.tolist()
        matrix_cols = sorted(matrix_cols, key=lambda x: x.split()[-1], reverse=True)
        matrix_rows = sorted(matrix_rows, key=lambda x: x.split()[-1], reverse=True)
        matrix = matrix[matrix_cols]
        matrix = matrix.loc[matrix_rows]
        return matrix

    # -------------------------------------------------------------------------
    def _step_13_remove_counters(self, matrix):
        if self.params.term_counters is False:
            matrix_cols = [" ".join(col.split()[:-1]) for col in matrix.columns]
            matrix_rows = [" ".join(row.split()[:-1]) for row in matrix.index]
            matrix.columns = matrix_cols
            matrix.index = matrix_rows
        return matrix

    # -------------------------------------------------------------------------
    def build(self):

        self._step_01_check_row_params()

        col_metrics = self._step_02_compute_column_peformance_metrics()
        row_metrics = self._step_03_compute_row_peformance_metrics()

        records = self._step_04_load_the_database()

        matrix_list = self._step_05_create_raw_matrix_list(records)

        matrix_list = self._step_06_explode_matrix_list(
            matrix_list,
            "columns",
            col_metrics.index.tolist(),
        )
        matrix_list = self._step_06_explode_matrix_list(
            matrix_list,
            "rows",
            row_metrics.index.tolist(),
        )

        matrix_list = self._step_07_compute_occurrences(matrix_list)

        row_mapping = self._step_08_build_mapping(row_metrics)
        col_mapping = self._step_08_build_mapping(col_metrics)

        matrix_list = self._step_09_rename_terms(matrix_list, row_mapping, col_mapping)

        matrix = self._step_10_pivot_matrix_list(matrix_list)
        matrix = self._step_11_check_terms(matrix, row_mapping, col_mapping)
        matrix = self._step_12_sort_matrix_axis(matrix)
        matrix = self._step_13_remove_counters(matrix)

        return matrix
