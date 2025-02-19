# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Data Frame
===============================================================================


>>> from techminer2.pkgs.associations import DataFrame
>>> (
...     DataFrame()
...     #
...     # COLUMNS:
...     .with_field("author_keywords")
...     .having_terms_in_top(None)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(["FINTECH", "INNOVATION", "FINANCIAL_SERVICES"])
...     #
...     # ROWS:
...     .having_other_terms_in_top(10)
...     .having_other_terms_ordered_by("OCC")
...     .having_other_term_occurrences_between(None, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
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

from ..._internals.mixins import ParamsMixin
from ..co_occurrence_matrix import MatrixDataFrame


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_compute_co_occurence_matrix(self):
        return (
            MatrixDataFrame()
            .update(**self.params.__dict__)
            .using_term_counters(True)
            .with_other_field(self.params.field)
            .build()
        )

    # -------------------------------------------------------------------------
    def _step_02_remove_rows_with_only_zeros(self, matrix):
        return matrix.loc[matrix.index[matrix.sum(axis=1) > 0], :]

    # -------------------------------------------------------------------------
    def _step_03_remove_counters(self, matrix):
        if self.params.term_counters:
            return matrix
        matrix.columns = [col.split(" ")[0] for col in matrix.columns]
        matrix.index = [idx.split(" ")[0] for idx in matrix.index]
        return matrix

    # -------------------------------------------------------------------------
    def build(self):

        matrix = self._step_01_compute_co_occurence_matrix()
        matrix = self._step_02_remove_rows_with_only_zeros(matrix)
        matrix = self._step_03_remove_counters(matrix)

        return matrix
