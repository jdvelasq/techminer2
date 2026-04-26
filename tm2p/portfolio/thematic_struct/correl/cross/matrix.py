"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import UnitOrderBy, Field, Correlation
    >>> from tm2p.portfolio.thematic_stucture.correlation.cross import Matrix
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
    ...     # CROSS WITH:
    ...     .with_cross_field(Field.CTRY_ISO3)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.PEARSON)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.round(3)
    columns                            fintech 117:25478  ...  financial services 007:01673
    rows                                                  ...
    fintech 117:25478                              1.000  ...                         0.128
    financial inclusion 017:03823                  0.262  ...                         0.244
    financial technology 015:02734                 0.000  ...                         0.206
    green finance 011:02844                        0.148  ...                         0.100
    blockchain 011:02023                           0.018  ...                         0.543
    banking 010:02599                              0.000  ...                         0.474
    china 009:01947                                0.117  ...                         0.019
    innovation 009:01703                           0.000  ...                         0.161
    artificial intelligence 008:01915              0.018  ...                         0.276
    financial services 007:01673                   0.128  ...                         1.000
    <BLANKLINE>
    [10 rows x 10 columns]


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
    ...     # CROSS WITH:
    ...     .with_cross_field(Field.CTRY_ISO3)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.COSINE)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.round(3)
    columns                            fintech 117:25478  ...  financial services 007:01673
    rows                                                  ...
    fintech 117:25478                                1.0  ...                           0.0
    financial inclusion 017:03823                    1.0  ...                           0.0
    financial technology 015:02734                   1.0  ...                           0.0
    green finance 011:02844                          1.0  ...                           0.0
    blockchain 011:02023                             1.0  ...                           0.0
    banking 010:02599                                0.0  ...                           0.0
    china 009:01947                                  1.0  ...                           0.0
    innovation 009:01703                             1.0  ...                           0.0
    artificial intelligence 008:01915                0.0  ...                           0.0
    financial services 007:01673                     0.0  ...                           0.0
    <BLANKLINE>
    [10 rows x 10 columns]


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
    ...     # CROSS WITH:
    ...     .with_cross_field(Field.CTRY_ISO3)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.MAXPROPORTIONAL)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.round(3)
    columns                            fintech 117:25478  ...  financial services 007:01673
    rows                                                  ...
    fintech 117:25478                              1.000  ...                         0.163
    financial inclusion 017:03823                  0.465  ...                         0.250
    financial technology 015:02734                 0.465  ...                         0.227
    green finance 011:02844                        0.209  ...                         0.222
    blockchain 011:02023                           0.279  ...                         0.462
    banking 010:02599                              0.233  ...                         0.455
    china 009:01947                                0.140  ...                         0.143
    innovation 009:01703                           0.140  ...                         0.286
    artificial intelligence 008:01915              0.279  ...                         0.308
    financial services 007:01673                   0.163  ...                         1.000
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import UnitOrderBy
from tm2p.portfolio.thematic_struct.cross_occur.matrix import Matrix as OCCMatrix

from .._intern import comput_correl_matrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_matrix = (
            OCCMatrix()
            .update(**self.params.__dict__)
            #
            .with_column_analysis_unit(self.params.source_field)
            .having_column_units_in_top(self.params.top_n_units)
            .having_column_units_ordered_by(UnitOrderBy.OCC)
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
            .with_index_analysis_unit(self.params.cross_analysis_unit)
            .having_index_units_ordered_by(UnitOrderBy.OCC)
            .having_index_unit_occurrence_between(None, None)
            .having_index_unit_citation_between(None, None)
            .having_index_units_in(None)
            #
            .run()
        )

        data_matrix = data_matrix.map(lambda x: 1.0 if x > 0 else 0.0)
        data_matrix = data_matrix.loc[~(data_matrix == 0).all(axis=1), :]
        data_matrix = data_matrix.loc[:, ~(data_matrix == 0).all(axis=0)]

        matrix = comput_correl_matrix(
            params=self.params,
            tfidf=data_matrix,
        )

        matrix.columns.name = "columns"
        matrix.index.name = "rows"

        return matrix
