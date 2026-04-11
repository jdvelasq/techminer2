"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.second_order_matrix import Matrix
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
    ...     .using_co_occurrence_threshold(1)
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
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    columns                            fintech 117:25478  financial inclusion 017:03823  financial technology 015:02734  green finance 011:02844  blockchain 011:02023  banking 010:02599  china 009:01947  innovation 009:01703  artificial intelligence 008:01915  financial services 007:01673
    rows
    fintech 117:25478                              1.000                          0.687                           0.756                    0.512                 0.555              0.649            0.481                 0.542                              0.586                         0.562
    financial inclusion 017:03823                  0.687                          1.000                           0.549                    0.240                 0.656              0.519            0.259                 0.625                              0.610                         0.464
    financial technology 015:02734                 0.756                          0.549                           1.000                    0.627                 0.407              0.550            0.132                 0.678                              0.306                         0.056
    green finance 011:02844                        0.512                          0.240                           0.627                    1.000                 0.273              0.168            0.292                 0.429                              0.312                         0.207
    blockchain 011:02023                           0.555                          0.656                           0.407                    0.273                 1.000              0.349            0.158                 0.193                              0.317                         0.330
    banking 010:02599                              0.649                          0.519                           0.550                    0.168                 0.349              1.000            0.454                 0.490                              0.276                         0.448
    china 009:01947                                0.481                          0.259                           0.132                    0.292                 0.158              0.454            1.000                 0.026                              0.184                         0.684
    innovation 009:01703                           0.542                          0.625                           0.678                    0.429                 0.193              0.490            0.026                 1.000                              0.235                         0.319
    artificial intelligence 008:01915              0.586                          0.610                           0.306                    0.312                 0.317              0.276            0.184                 0.235                              1.000                         0.408
    financial services 007:01673                   0.562                          0.464                           0.056                    0.207                 0.330              0.448            0.684                 0.319                              0.408                         1.000




"""

from tm2p._intern import ParamsMixin

from ..first_order_network import Matrix as BaseMatrix
from ._intern.compute_cosine_similarity import compute_cosine_similarity


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = BaseMatrix().update(**self.params.__dict__).run()
        df = compute_cosine_similarity(df)

        return df
