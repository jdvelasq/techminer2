"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import Matrix
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
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    columns                            fintech 117:25478  financial inclusion 017:03823  financial technology 015:02734  green finance 011:02844  blockchain 011:02023  banking 010:02599  china 009:01947  innovation 009:01703  artificial intelligence 008:01915  financial services 007:01673
    rows
    fintech 117:25478                              0.000                          0.007                           0.005                    0.006                 0.006              0.006            0.007                 0.006                              0.006                         0.005
    financial inclusion 017:03823                  0.007                          0.000                           0.004                    0.005                 0.005              0.012            0.000                 0.000                              0.007                         0.008
    financial technology 015:02734                 0.005                          0.004                           0.000                    0.006                 0.006              0.000            0.015                 0.000                              0.008                         0.010
    green finance 011:02844                        0.006                          0.005                           0.006                    0.000                 0.000              0.000            0.010                 0.000                              0.000                         0.000
    blockchain 011:02023                           0.006                          0.005                           0.006                    0.000                 0.000              0.009            0.000                 0.000                              0.023                         0.000
    banking 010:02599                              0.006                          0.012                           0.000                    0.000                 0.009              0.000            0.000                 0.022                              0.012                         0.029
    china 009:01947                                0.007                          0.000                           0.015                    0.010                 0.000              0.000            0.000                 0.025                              0.000                         0.000
    innovation 009:01703                           0.006                          0.000                           0.000                    0.000                 0.000              0.022            0.025                 0.000                              0.000                         0.032
    artificial intelligence 008:01915              0.006                          0.007                           0.008                    0.000                 0.023              0.012            0.000                 0.000                              0.000                         0.000
    financial services 007:01673                   0.005                          0.008                           0.010                    0.000                 0.000              0.029            0.000                 0.032                              0.000                         0.000


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
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                             fintech  financial inclusion  financial technology  green finance  blockchain  banking  china  innovation  artificial intelligence  financial services
    fintech                    0.000                0.007                 0.005          0.006       0.006    0.006  0.007       0.006                    0.006               0.005
    financial inclusion        0.007                0.000                 0.004          0.005       0.005    0.012  0.000       0.000                    0.007               0.008
    financial technology       0.005                0.004                 0.000          0.006       0.006    0.000  0.015       0.000                    0.008               0.010
    green finance              0.006                0.005                 0.006          0.000       0.000    0.000  0.010       0.000                    0.000               0.000
    blockchain                 0.006                0.005                 0.006          0.000       0.000    0.009  0.000       0.000                    0.023               0.000
    banking                    0.006                0.012                 0.000          0.000       0.009    0.000  0.000       0.022                    0.012               0.029
    china                      0.007                0.000                 0.015          0.010       0.000    0.000  0.000       0.025                    0.000               0.000
    innovation                 0.006                0.000                 0.000          0.000       0.000    0.022  0.025       0.000                    0.000               0.032
    artificial intelligence    0.006                0.007                 0.008          0.000       0.023    0.012  0.000       0.000                    0.000               0.000
    financial services         0.005                0.008                 0.010          0.000       0.000    0.029  0.000       0.032                    0.000               0.000


"""

from tm2p._intern import ParamsMixin

from ._intern.create_similarity_matrix import create_similarity_matrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return create_similarity_matrix(params=self.params)
