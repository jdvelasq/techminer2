"""
MatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.second_order_matrix import MatrixList
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
    >>> df.head(10).round(3)
                                    rows                            columns  SIM
    0                  banking 010:02599                  banking 010:02599  1.0
    1  artificial intelligence 008:01915  artificial intelligence 008:01915  1.0
    2               blockchain 011:02023               blockchain 011:02023  1.0
    3                    china 009:01947                    china 009:01947  1.0
    4            green finance 011:02844            green finance 011:02844  1.0
    5       financial services 007:01673       financial services 007:01673  1.0
    6     financial technology 015:02734     financial technology 015:02734  1.0
    7               innovation 009:01703               innovation 009:01703  1.0
    8      financial inclusion 017:03823      financial inclusion 017:03823  1.0
    9                  fintech 117:25478                  fintech 117:25478  1.0


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.matrix_to_matrix_list import matrix_to_matrix_list

from .matrix import Matrix


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()
        matrix_list = matrix_to_matrix_list(matrix, value_name="SIM")

        return matrix_list
