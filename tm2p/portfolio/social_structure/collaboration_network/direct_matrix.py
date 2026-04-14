"""
DirectMatrix
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CollaborationUnit, ItemOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import DirectMatrix
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_collaboration_unit(CollaborationUnit.AUTH)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_item_co_occurrence(1)
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
    ...     .with_collaboration_unit(CollaborationUnit.AUTH)
    ...     #
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
from tm2p._intern.networks.normalize_matrix import normalize_matrix
from tm2p.enum import CollaborationUnit, Field

from ...thematic_stucture.co_occurrence.matrix import Matrix as CoOccurrenceMatrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        field = {
            CollaborationUnit.AUTH: Field.AUTH_FULL_NAME,
            CollaborationUnit.CTRY: Field.CTRY_ISO3,
            CollaborationUnit.ORG: Field.ORG,
        }[self.params.collaboration_unit]

        self.with_source_field(field)

        matrix = CoOccurrenceMatrix().update(**self.params.__dict__).run()
        matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )
        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
