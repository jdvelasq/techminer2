# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence DataFrame
===============================================================================


Example:
    >>> from techminer2.packages.co_occurrence_matrix import DataFrame
    >>> (
    ...     DataFrame()
    ...     #
    ...     # COLUMNS:
    ...     .with_field("raw_author_keywords")
    ...     .having_terms_in_top(10)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(2, None)
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
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
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


    >>> from techminer2.packages.co_occurrence_matrix import DataFrame
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(10)
                            rows                    columns  OCC
    0            FINTECH 31:5168            FINTECH 31:5168   31
    1         INNOVATION 07:0911         INNOVATION 07:0911    7
    2            FINTECH 31:5168         INNOVATION 07:0911    5
    3         INNOVATION 07:0911            FINTECH 31:5168    5
    4  FINANCIAL_SERVICE 04:0667  FINANCIAL_SERVICE 04:0667    4
    5         BLOCKCHAIN 03:0369         BLOCKCHAIN 03:0369    3
    6         BLOCKCHAIN 03:0369            FINTECH 31:5168    3
    7     BUSINESS_MODEL 03:0896     BUSINESS_MODEL 03:0896    3
    8     BUSINESS_MODEL 03:0896            FINTECH 31:5168    3
    9       CROWDFUNDING 03:0335       CROWDFUNDING 03:0335    3



"""
from ..._internals.mixins import ParamsMixin
from .matrix_data_frame import MatrixDataFrame


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_compute_co_occurence_matrix(self):
        return (
            MatrixDataFrame()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .using_term_counters(True)
            .run()
        )

    # -------------------------------------------------------------------------
    def _step_02_melt_matrix(self, matrix):
        matrix = matrix.reset_index(drop=False)
        matrix_list = matrix.melt(
            id_vars=["rows"],
            value_vars=matrix.columns,
            var_name="columns",
        )
        matrix_list = matrix_list.rename(columns={"value": "OCC"})
        matrix_list = matrix_list.sort_values(
            by=["OCC", "rows", "columns"],
            ascending=[False, True, True],
        )
        matrix_list = matrix_list.reset_index(drop=True)
        return matrix_list

    # -------------------------------------------------------------------------
    def run(self):

        matrix = self._step_01_compute_co_occurence_matrix()
        matrix_list = self._step_02_melt_matrix(matrix)

        return matrix_list
