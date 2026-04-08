"""
MatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_structure.co_occurrence.first_order_network import MatrixList
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
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
                                    rows                            columns  ASSOC
    0               innovation 009:01703       financial services 007:01673  0.032
    1       financial services 007:01673               innovation 009:01703  0.032
    2                  banking 010:02599       financial services 007:01673  0.029
    3       financial services 007:01673                  banking 010:02599  0.029
    4                    china 009:01947               innovation 009:01703  0.025
    5               innovation 009:01703                    china 009:01947  0.025
    6               blockchain 011:02023  artificial intelligence 008:01915  0.023
    7  artificial intelligence 008:01915               blockchain 011:02023  0.023
    8                  banking 010:02599               innovation 009:01703  0.022
    9               innovation 009:01703                  banking 010:02599  0.022


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
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
                          rows                  columns  ASSOC
    0               innovation       financial services  0.032
    1       financial services               innovation  0.032
    2                  banking       financial services  0.029
    3       financial services                  banking  0.029
    4                    china               innovation  0.025
    5               innovation                    china  0.025
    6               blockchain  artificial intelligence  0.023
    7  artificial intelligence               blockchain  0.023
    8                  banking               innovation  0.022
    9               innovation                  banking  0.022


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.matrix_to_matrix_list import matrix_to_matrix_list

from .matrix import Matrix


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        counters = self.params.counters
        matrix = Matrix().update(**self.params.__dict__).using_counters(True).run()
        matrix_list = matrix_to_matrix_list(matrix, value_name="ASSOC")
        if counters is False:
            matrix_list["rows"] = matrix_list["rows"].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )
            matrix_list["columns"] = matrix_list["columns"].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )

        return matrix_list
