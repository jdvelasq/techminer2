"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.direct_similarity_network import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
from tm2p.enum import AnalysisUnit

from ..mtx.mtx import Matrix as CoOccurrenceMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.analysis_unit not in (
            AnalysisUnit.AUTHKW,
            AnalysisUnit.IDXKW,
            AnalysisUnit.KW,
            AnalysisUnit.CONCEPT,
            AnalysisUnit.WORD,
        ):
            raise ValueError(f"Unsupported analysis unit: {self.params.analysis_unit}")

        matrix = CoOccurrenceMatrix().update(**self.params.__dict__).run()

        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
