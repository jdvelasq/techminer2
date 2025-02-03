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
...     # ROWWS:
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
...     .where_directory_is("example/")
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




"""
from ...internals.mixins import InputFunctionsMixin
from .data_frame import DataFrame


class MatrixDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_create_matrix_list(self):
        return (
            DataFrame()
            .update_params(**self.params.__dict__)
            .using_term_counters(True)
            .build()
        )

    # -------------------------------------------------------------------------
    def _step_2_pivot_matrix_list(self, matrix_list):
        matrix = matrix_list.pivot(
            index=matrix_list.columns[0],
            columns=matrix_list.columns[1],
            values=matrix_list.columns[2],
        )
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)
        return matrix

    # -------------------------------------------------------------------------
    def _step_3_sort_matrix_axis(self, matrix):
        matrix_cols = matrix.columns.tolist()
        matrix_rows = matrix.index.tolist()
        matrix_cols = sorted(matrix_cols, key=lambda x: x.split()[-1], reverse=True)
        matrix_rows = sorted(matrix_rows, key=lambda x: x.split()[-1], reverse=True)
        matrix = matrix[matrix_cols]
        matrix = matrix.loc[matrix_rows]
        return matrix

    # -------------------------------------------------------------------------
    def _step_4_remove_counters(self, matrix):
        if self.params.term_counters is False:
            matrix_cols = [" ".join(col.split()[:-1]) for col in matrix.columns]
            matrix_rows = [" ".join(row.split()[:-1]) for row in matrix.index]
            matrix.columns = matrix_cols
            matrix.index = matrix_rows
        return matrix

    # -------------------------------------------------------------------------
    def build(self):

        matrix_list = self._step_1_create_matrix_list()
        matrix = self._step_2_pivot_matrix_list(matrix_list)
        matrix = self._step_3_sort_matrix_axis(matrix)
        matrix = self._step_4_remove_counters(matrix)

        return matrix
