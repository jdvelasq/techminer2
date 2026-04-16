"""
MatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.matrix import MatrixList
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(12)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
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
    >>> df.head(10)
                                 ROWS                         COLUMNS  OCC
    0               fintech 117:25478               fintech 117:25478  117
    1   financial inclusion 017:03823   financial inclusion 017:03823   17
    2  financial technology 015:02734  financial technology 015:02734   15
    3               fintech 117:25478   financial inclusion 017:03823   14
    4   financial inclusion 017:03823               fintech 117:25478   14
    5         green finance 011:02844         green finance 011:02844   11
    6            blockchain 011:02023            blockchain 011:02023   11
    7               banking 010:02599               banking 010:02599   10
    8                 china 009:01947                 china 009:01947    9
    9            innovation 009:01703            innovation 009:01703    9


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
