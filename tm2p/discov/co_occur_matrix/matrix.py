"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p import Field, ItemOrderBy
    >>> from tm2p.discov.co_occur_matrix import Matrix
    >>> df = (
    ...     Matrix()
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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    columns                           fintech 117:25478  financial inclusion 017:03823  financial-technology 015:02734  green finance 011:02844  blockchain 011:02023  banking 010:02599  china 009:01947  innovation 009:01703  artificialintelligence 008:01915  financial services 007:01673
    rows
    fintech 117:25478                               117                             14                               8                        8                     8                  7                7                     6                                 6                             4
    financial inclusion 017:03823                    14                             17                               1                        1                     1                  2                0                     0                                 1                             1
    financial-technology 015:02734                    8                              1                              15                        1                     1                  0                2                     0                                 1                             1
    green finance 011:02844                           8                              1                               1                       11                     0                  0                1                     0                                 0                             0
    blockchain 011:02023                              8                              1                               1                        0                    11                  1                0                     0                                 2                             0
    banking 010:02599                                 7                              2                               0                        0                     1                 10                0                     2                                 1                             2
    china 009:01947                                   7                              0                               2                        1                     0                  0                9                     2                                 0                             0
    innovation 009:01703                              6                              0                               0                        0                     0                  2                2                     9                                 0                             2
    artificialintelligence 008:01915                  6                              1                               1                        0                     2                  1                0                     0                                 8                             0
    financial services 007:01673                      4                              1                               1                        0                     0                  2                0                     2                                 0                             7




"""

from tm2p._intern import ParamsMixin

from ..cross_occur_matrix.matrix_list import Matrix as BaseMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            BaseMatrix()
            .update(**self.params.__dict__)
            #
            # COLUMNS:
            .with_column_field(self.params.source_field)
            .having_column_items_in_top(self.params.top_n)
            .having_column_items_ordered_by(self.params.items_order_by)
            .having_column_item_occurrences_between(
                self.params.item_occurrences_range[0],
                self.params.item_occurrences_range[1],
            )
            .having_column_item_citations_between(
                self.params.item_citations_range[0],
                self.params.item_citations_range[1],
            )
            .having_column_items_in(self.params.items_in)
            #
            # ROWS:
            .with_index_field(self.params.source_field)
            .having_index_items_in_top(self.params.top_n)
            .having_index_items_ordered_by(self.params.items_order_by)
            .having_index_item_occurrences_between(
                self.params.item_occurrences_range[0],
                self.params.item_occurrences_range[1],
            )
            .having_index_item_citations_between(
                self.params.item_citations_range[0],
                self.params.item_citations_range[1],
            )
            .having_index_items_in(self.params.items_in)
            #
            .run()
        )
