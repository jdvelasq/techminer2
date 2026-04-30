"""
DirectMatrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.direct import DirectMatrix  # type: ignore
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
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
    COLUMNS                         Luca Benini 0041:000706  Michele Magno 0035:000501  Ivanovitch Silva 0027:000442  Danilo Pau 0021:000125  Marianne Silva 0020:000255  Marco Zennaro 0018:000115  Daniel G. Costa 0016:000312  Khalid El Makkaoui 0016:000178  Manuel Roveri 0016:000160  Danilo Pietro Pau 0016:000064
    ROWS                                                                                                                                                                                                                                                                                                                  
    Luca Benini 0041:000706                           0.000                      0.008                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0
    Michele Magno 0035:000501                         0.008                      0.000                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0
    Ivanovitch Silva 0027:000442                      0.000                      0.000                         0.000                     0.0                       0.037                        0.0                        0.032                             0.0                        0.0                            0.0
    Danilo Pau 0021:000125                            0.000                      0.000                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0
    Marianne Silva 0020:000255                        0.000                      0.000                         0.037                     0.0                       0.000                        0.0                        0.025                             0.0                        0.0                            0.0
    Marco Zennaro 0018:000115                         0.000                      0.000                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0
    Daniel G. Costa 0016:000312                       0.000                      0.000                         0.032                     0.0                       0.025                        0.0                        0.000                             0.0                        0.0                            0.0
    Khalid El Makkaoui 0016:000178                    0.000                      0.000                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0
    Manuel Roveri 0016:000160                         0.000                      0.000                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0
    Danilo Pietro Pau 0016:000064                     0.000                      0.000                         0.000                     0.0                       0.000                        0.0                        0.000                             0.0                        0.0                            0.0


    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
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
    COLUMNS             Luca Benini  Michele Magno  Ivanovitch Silva  Danilo Pau  Marianne Silva  Marco Zennaro  Daniel G. Costa  Khalid El Makkaoui  Manuel Roveri  Danilo Pietro Pau
    ROWS                                                                                                                                                                              
    Luca Benini               0.000          0.008             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0
    Michele Magno             0.008          0.000             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0
    Ivanovitch Silva          0.000          0.000             0.000         0.0           0.037            0.0            0.032                 0.0            0.0                0.0
    Danilo Pau                0.000          0.000             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0
    Marianne Silva            0.000          0.000             0.037         0.0           0.000            0.0            0.025                 0.0            0.0                0.0
    Marco Zennaro             0.000          0.000             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0
    Daniel G. Costa           0.000          0.000             0.032         0.0           0.025            0.0            0.000                 0.0            0.0                0.0
    Khalid El Makkaoui        0.000          0.000             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0
    Manuel Roveri             0.000          0.000             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0
    Danilo Pietro Pau         0.000          0.000             0.000         0.0           0.000            0.0            0.000                 0.0            0.0                0.0


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix

from .count_matrix import CountMatrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = CountMatrix().update(**self.params.__dict__).run()
        matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )
        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
