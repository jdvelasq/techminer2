"""
DirectMatrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import DirectMatrix
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                        Julapa A. Jagtiani 005:01156  Douglas W. Arner 003:00911  Lars Hornuf 003:00904  Janos N. Barberis 003:00445  Gerhard Schwabe 003:00330  Liudmila Zavolokina 003:00330  Mateusz Dolata 003:00330  Peter Gomber 002:02579  Robert J. Kauffman 002:01445  Victor Murinde 002:01022
    ROWS
    Julapa A. Jagtiani 005:01156                            0.0                       0.000                    0.0                        0.000                      0.000                          0.000                     0.000                    0.00                          0.00                       0.0
    Douglas W. Arner 003:00911                              0.0                       0.000                    0.0                        0.222                      0.000                          0.000                     0.000                    0.00                          0.00                       0.0
    Lars Hornuf 003:00904                                   0.0                       0.000                    0.0                        0.000                      0.000                          0.000                     0.000                    0.00                          0.00                       0.0
    Janos N. Barberis 003:00445                             0.0                       0.222                    0.0                        0.000                      0.000                          0.000                     0.000                    0.00                          0.00                       0.0
    Gerhard Schwabe 003:00330                               0.0                       0.000                    0.0                        0.000                      0.000                          0.333                     0.333                    0.00                          0.00                       0.0
    Liudmila Zavolokina 003:00330                           0.0                       0.000                    0.0                        0.000                      0.333                          0.000                     0.333                    0.00                          0.00                       0.0
    Mateusz Dolata 003:00330                                0.0                       0.000                    0.0                        0.000                      0.333                          0.333                     0.000                    0.00                          0.00                       0.0
    Peter Gomber 002:02579                                  0.0                       0.000                    0.0                        0.000                      0.000                          0.000                     0.000                    0.00                          0.25                       0.0
    Robert J. Kauffman 002:01445                            0.0                       0.000                    0.0                        0.000                      0.000                          0.000                     0.000                    0.25                          0.00                       0.0
    Victor Murinde 002:01022                                0.0                       0.000                    0.0                        0.000                      0.000                          0.000                     0.000                    0.00                          0.00                       0.0


    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.round(3).head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS              Julapa A. Jagtiani  Douglas W. Arner  Lars Hornuf  Janos N. Barberis  Gerhard Schwabe  Liudmila Zavolokina  Mateusz Dolata  Peter Gomber  Robert J. Kauffman  Victor Murinde
    ROWS
    Julapa A. Jagtiani                  0.0             0.000          0.0              0.000            0.000                0.000           0.000          0.00                0.00             0.0
    Douglas W. Arner                    0.0             0.000          0.0              0.222            0.000                0.000           0.000          0.00                0.00             0.0
    Lars Hornuf                         0.0             0.000          0.0              0.000            0.000                0.000           0.000          0.00                0.00             0.0
    Janos N. Barberis                   0.0             0.222          0.0              0.000            0.000                0.000           0.000          0.00                0.00             0.0
    Gerhard Schwabe                     0.0             0.000          0.0              0.000            0.000                0.333           0.333          0.00                0.00             0.0
    Liudmila Zavolokina                 0.0             0.000          0.0              0.000            0.333                0.000           0.333          0.00                0.00             0.0
    Mateusz Dolata                      0.0             0.000          0.0              0.000            0.333                0.333           0.000          0.00                0.00             0.0
    Peter Gomber                        0.0             0.000          0.0              0.000            0.000                0.000           0.000          0.00                0.25             0.0
    Robert J. Kauffman                  0.0             0.000          0.0              0.000            0.000                0.000           0.000          0.25                0.00             0.0
    Victor Murinde                      0.0             0.000          0.0              0.000            0.000                0.000           0.000          0.00                0.00             0.0


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.norma_mtx import normalize_matrix

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
