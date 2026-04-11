"""
MatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.co_occurrence_matrix import MatrixList
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_co_occurrence_threshold(12)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> df.head(50)


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.matrix_to_matrix_list import matrix_to_matrix_list

from .matrix import Matrix as BaseMatrix


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = BaseMatrix().update(**self.params.__dict__).run()

        matrix_list = matrix_to_matrix_list(matrix, value_name="OCC")

        return matrix_list
