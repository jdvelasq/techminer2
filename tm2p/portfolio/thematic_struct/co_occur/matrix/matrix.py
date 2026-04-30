"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.matrix import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
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
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                            fintech 117:25478  financial inclusion 017:03823  financial technology 015:02734  green finance 011:02844  blockchain 011:02023  banking 010:02599  china 009:01947  innovation 009:01703  artificial intelligence 008:01915  financial services 007:01673
    ROWS
    fintech 117:25478                                117                             14                               8                        8                     8                  7                7                     6                                  6                             4
    financial inclusion 017:03823                     14                             17                               1                        1                     1                  2                0                     0                                  1                             1
    financial technology 015:02734                     8                              1                              15                        1                     1                  0                2                     0                                  1                             1
    green finance 011:02844                            8                              1                               1                       11                     0                  0                1                     0                                  0                             0
    blockchain 011:02023                               8                              1                               1                        0                    11                  1                0                     0                                  2                             0
    banking 010:02599                                  7                              2                               0                        0                     1                 10                0                     2                                  1                             2
    china 009:01947                                    7                              0                               2                        1                     0                  0                9                     2                                  0                             0
    innovation 009:01703                               6                              0                               0                        0                     0                  2                2                     9                                  0                             2
    artificial intelligence 008:01915                  6                              1                               1                        0                     2                  1                0                     0                                  8                             0
    financial services 007:01673                       4                              1                               1                        0                     0                  2                0                     2                                  0                             7


    >>> df = (
    ...     Matrix()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                  fintech  financial inclusion  financial technology  green finance  blockchain  banking  china  innovation  artificial intelligence  financial services
    ROWS
    fintech                      117                   14                     8              8           8        7      7           6                        6                   4
    financial inclusion           14                   17                     1              1           1        2      0           0                        1                   1
    financial technology           8                    1                    15              1           1        0      2           0                        1                   1
    green finance                  8                    1                     1             11           0        0      1           0                        0                   0
    blockchain                     8                    1                     1              0          11        1      0           0                        2                   0
    banking                        7                    2                     0              0           1       10      0           2                        1                   2
    china                          7                    0                     2              1           0        0      9           2                        0                   0
    innovation                     6                    0                     0              0           0        2      2           9                        0                   2
    artificial intelligence        6                    1                     1              0           2        1      0           0                        8                   0
    financial services             4                    1                     1              0           0        2      0           2                        0                   7

"""

from tm2p._intern import ParamsMixin

from ...cross_occur.matrix.matrix_list import Matrix as CrossOccurrenceMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        matrix = (
            CrossOccurrenceMatrix()
            #
            .update(**self.params.__dict__)
            #
            # COLUMNS:
            .with_column_analysis_unit(self.params.analysis_unit)
            .having_column_units_in_top(self.params.top_n_units)
            .having_column_units_ordered_by(self.params.unit_order_by)
            .having_column_unit_occurrence_between(
                self.params.unit_occurrence_range[0],
                self.params.unit_occurrence_range[1],
            )
            .having_column_unit_citation_between(
                self.params.unit_global_citation_range[0],
                self.params.unit_global_citation_range[1],
            )
            .having_column_units_in(self.params.units_in)
            #
            # ROWS:
            .with_index_analysis_unit(self.params.analysis_unit)
            .having_index_units_in_top(self.params.top_n_units)
            .having_index_units_ordered_by(self.params.unit_order_by)
            .having_index_unit_occurrence_between(
                self.params.unit_occurrence_range[0],
                self.params.unit_occurrence_range[1],
            )
            .having_index_unit_citation_between(
                self.params.unit_global_citation_range[0],
                self.params.unit_global_citation_range[1],
            )
            .having_index_units_in(self.params.units_in)
            #
            .using_minimum_pair_co_occurrence(1)
            #
            .run()
        )

        diag = matrix.values.diagonal()
        matrix = matrix.where(matrix >= self.params.minimum_pair_co_occurrence, other=0)
        for i, value in enumerate(diag):
            matrix.values[i, i] = value

        matrix.index.name = "ROWS"
        matrix.columns.name = "COLUMNS"

        return matrix
