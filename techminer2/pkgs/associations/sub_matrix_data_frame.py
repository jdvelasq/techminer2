# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Sub Matrix DataFrame
===============================================================================


>>> from techminer2.pkgs.associations import SubMatrixDataFrame
>>> (
...     SubMatrixDataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(2, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # TERMS:
...     .having_col_terms_in(["FINTECH", "INNOVATION", "FINANCIAL_SERVICES"])
...     #
...     # ROWS:
...     .with_other_field(None)
...     .having_other_terms_in_top(None)
...     .having_other_terms_ordered_by(None)
...     .having_other_term_occurrences_between(None, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... ).head(10)
columns                       FINTECH 31:5168  ...  FINANCIAL_SERVICES 04:0667
rows                                           ...                            
FINTECH 31:5168                            31  ...                           3
INNOVATION 07:0911                          5  ...                           2
FINANCIAL_SERVICES 04:0667                  3  ...                           4
FINANCIAL_INCLUSION 03:0590                 3  ...                           0
FINANCIAL_TECHNOLOGY 03:0461                2  ...                           1
CROWDFUNDING 03:0335                        2  ...                           0
MARKETPLACE_LENDING 03:0317                 3  ...                           0
BUSINESS_MODELS 02:0759                     2  ...                           1
CYBER_SECURITY 02:0342                      2  ...                           0
CASE_STUDY 02:0340                          2  ...                           0
<BLANKLINE>
[10 rows x 3 columns]

"""

from ...internals.mixins import InputFunctionsMixin
from ..co_occurrence_matrix import MatrixDataFrame


class SubMatrixDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_compute_co_occurence_matrix(self):
        return (
            MatrixDataFrame()
            .update_params(**self.params.__dict__)
            .using_term_counters(True)
            .build()
        )

    # -------------------------------------------------------------------------
    def _step_02_select_terms(self, matrix, col_terms):
        #
        selected_columns = []
        for col in matrix.columns:
            name = col.split(" ")[0]
            if name in col_terms:
                selected_columns.append(col)
        #
        return matrix[selected_columns]

    # -------------------------------------------------------------------------
    def _step_03_remove_rows_of_zeros(self, matrix):
        return matrix.loc[(matrix.T != 0).any()]

    # -------------------------------------------------------------------------
    def _step_04_remove_counters(self, matrix):
        if self.params.term_counters:
            return matrix
        matrix.columns = [col.split(" ")[0] for col in matrix.columns]
        matrix.index = [idx.split(" ")[0] for idx in matrix.index]

        return matrix

    # -------------------------------------------------------------------------
    def build(self):

        matrix = self._step_01_compute_co_occurence_matrix()
        matrix = self._step_02_select_terms(matrix, self.params.col_terms)
        matrix = self._step_03_remove_rows_of_zeros(matrix)
        matrix = self._step_04_remove_counters(matrix)

        return matrix
