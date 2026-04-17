"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.direct_similarity_network import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                            fintech 119:26148  finance 029:07137  innovation 020:03916  china 018:03596  financial inclusion 017:03823  financial technology 016:02809  sustainable development 015:02158  banking 013:03043  sustainability 013:02308  blockchain 012:03450
    ROWS
    fintech 119:26148                                119                 17                    14               12                             14                               8                                  7                  9                         9                     8
    finance 029:07137                                 17                 29                     8                6                              2                               2                                  7                  2                         4                     4
    innovation 020:03916                              14                  8                    20                7                              0                               1                                  5                  4                         4                     2
    china 018:03596                                   12                  6                     7               18                              0                               3                                  6                  3                         5                     0
    financial inclusion 017:03823                     14                  2                     0                0                             17                               1                                  0                  2                         1                     1
    financial technology 016:02809                     8                  2                     1                3                              1                              16                                  3                  0                         1                     1
    sustainable development 015:02158                  7                  7                     5                6                              0                               3                                 15                  1                         8                     1
    banking 013:03043                                  9                  2                     4                3                              2                               0                                  1                 13                         1                     1
    sustainability 013:02308                           9                  4                     4                5                              1                               1                                  8                  1                        13                     0
    blockchain 012:03450                               8                  4                     2                0                              1                               1                                  1                  1                         0                    12


    >>> df = (
    ...     Matrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                  fintech  finance  innovation  china  financial inclusion  financial technology  sustainable development  banking  sustainability  blockchain
    ROWS
    fintech                      119       17          14     12                   14                     8                        7        9               9           8
    finance                       17       29           8      6                    2                     2                        7        2               4           4
    innovation                    14        8          20      7                    0                     1                        5        4               4           2
    china                         12        6           7     18                    0                     3                        6        3               5           0
    financial inclusion           14        2           0      0                   17                     1                        0        2               1           1
    financial technology           8        2           1      3                    1                    16                        3        0               1           1
    sustainable development        7        7           5      6                    0                     3                       15        1               8           1
    banking                        9        2           4      3                    2                     0                        1       13               1           1
    sustainability                 9        4           4      5                    1                     1                        8        1              13           0
    blockchain                     8        4           2      0                    1                     1                        1        1               0          12


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, Field

from ..matrix.matrix import Matrix as CoOccurrenceMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        field = {
            AnalysisUnit.AUTHKW: Field.AUTHKW_NORM,
            AnalysisUnit.IDXKW: Field.IDXKW_NORM,
            AnalysisUnit.KW: Field.KW_NORM,
            AnalysisUnit.CONCEPT: Field.CONCEPT_NORM,
            AnalysisUnit.WORD: Field.WORD_NORM,
        }[self.params.analysis_unit]

        self.with_source_field(field)

        matrix = CoOccurrenceMatrix().update(**self.params.__dict__).run()

        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
