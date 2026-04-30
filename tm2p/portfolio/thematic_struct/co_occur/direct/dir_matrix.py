"""
DirectMatrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import DirectMatrix
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
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
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                            fintech 119:26148  finance 029:07137  innovation 020:03916  china 018:03596  financial inclusion 017:03823  financial technology 016:02809  sustainable development 015:02158  banking 013:03043  sustainability 013:02308  blockchain 012:03450
    ROWS
    fintech 119:26148                              0.000              0.005                 0.006            0.006                          0.007                           0.004                              0.004              0.006                     0.006                 0.006
    finance 029:07137                              0.005              0.000                 0.014            0.011                          0.004                           0.004                              0.016              0.005                     0.011                 0.011
    innovation 020:03916                           0.006              0.014                 0.000            0.019                          0.000                           0.003                              0.017              0.015                     0.015                 0.008
    china 018:03596                                0.006              0.011                 0.019            0.000                          0.000                           0.010                              0.022              0.013                     0.021                 0.000
    financial inclusion 017:03823                  0.007              0.004                 0.000            0.000                          0.000                           0.004                              0.000              0.009                     0.005                 0.005
    financial technology 016:02809                 0.004              0.004                 0.003            0.010                          0.004                           0.000                              0.012              0.000                     0.005                 0.005
    sustainable development 015:02158              0.004              0.016                 0.017            0.022                          0.000                           0.012                              0.000              0.005                     0.041                 0.006
    banking 013:03043                              0.006              0.005                 0.015            0.013                          0.009                           0.000                              0.005              0.000                     0.006                 0.006
    sustainability 013:02308                       0.006              0.011                 0.015            0.021                          0.005                           0.005                              0.041              0.006                     0.000                 0.000
    blockchain 012:03450                           0.006              0.011                 0.008            0.000                          0.005                           0.005                              0.006              0.006                     0.000                 0.000


    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
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
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                  fintech  finance  innovation  china  financial inclusion  financial technology  sustainable development  banking  sustainability  blockchain
    ROWS
    fintech                    0.000    0.005       0.006  0.006                0.007                 0.004                    0.004    0.006           0.006       0.006
    finance                    0.005    0.000       0.014  0.011                0.004                 0.004                    0.016    0.005           0.011       0.011
    innovation                 0.006    0.014       0.000  0.019                0.000                 0.003                    0.017    0.015           0.015       0.008
    china                      0.006    0.011       0.019  0.000                0.000                 0.010                    0.022    0.013           0.021       0.000
    financial inclusion        0.007    0.004       0.000  0.000                0.000                 0.004                    0.000    0.009           0.005       0.005
    financial technology       0.004    0.004       0.003  0.010                0.004                 0.000                    0.012    0.000           0.005       0.005
    sustainable development    0.004    0.016       0.017  0.022                0.000                 0.012                    0.000    0.005           0.041       0.006
    banking                    0.006    0.005       0.015  0.013                0.009                 0.000                    0.005    0.000           0.006       0.006
    sustainability             0.006    0.011       0.015  0.021                0.005                 0.005                    0.041    0.006           0.000       0.000
    blockchain                 0.006    0.011       0.008  0.000                0.005                 0.005                    0.006    0.006           0.000       0.000


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix

from .matrix import Matrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()
        matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )
        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
