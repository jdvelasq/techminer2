"""
DirectMatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CollaborationUnit, Field, ItemOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import DirectMatrixList
    >>> df = (
    ...     DirectMatrixList()
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
    >>> df.head(10).round(3)
                                ROWS                        COLUMNS  ASSOC
    0      Gerhard Schwabe 003:00330  Liudmila Zavolokina 003:00330  0.333
    1      Gerhard Schwabe 003:00330       Mateusz Dolata 003:00330  0.333
    2  Liudmila Zavolokina 003:00330      Gerhard Schwabe 003:00330  0.333
    3  Liudmila Zavolokina 003:00330       Mateusz Dolata 003:00330  0.333
    4       Mateusz Dolata 003:00330      Gerhard Schwabe 003:00330  0.333
    5       Mateusz Dolata 003:00330  Liudmila Zavolokina 003:00330  0.333
    6         Peter Gomber 002:02579   Robert J. Kauffman 002:01445  0.250
    7   Robert J. Kauffman 002:01445         Peter Gomber 002:02579  0.250
    8     Douglas W. Arner 003:00911    Janos N. Barberis 003:00445  0.222
    9    Janos N. Barberis 003:00445     Douglas W. Arner 003:00911  0.222


    >>> df = (
    ...     DirectMatrixList()
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
    >>> df.head(10).round(3)
                      ROWS              COLUMNS  ASSOC
    0      Gerhard Schwabe  Liudmila Zavolokina  0.333
    1      Gerhard Schwabe       Mateusz Dolata  0.333
    2  Liudmila Zavolokina      Gerhard Schwabe  0.333
    3  Liudmila Zavolokina       Mateusz Dolata  0.333
    4       Mateusz Dolata      Gerhard Schwabe  0.333
    5       Mateusz Dolata  Liudmila Zavolokina  0.333
    6         Peter Gomber   Robert J. Kauffman  0.250
    7   Robert J. Kauffman         Peter Gomber  0.250
    8     Douglas W. Arner    Janos N. Barberis  0.222
    9    Janos N. Barberis     Douglas W. Arner  0.222


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.matrix_to_matrix_list import matrix_to_matrix_list

from .direct_matrix import DirectMatrix


class DirectMatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        counters = self.params.counters
        matrix = (
            DirectMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        matrix_list = matrix_to_matrix_list(matrix, value_name="ASSOC")
        if counters is False:
            matrix_list["ROWS"] = matrix_list["ROWS"].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )
            matrix_list["COLUMNS"] = matrix_list["COLUMNS"].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )

        return matrix_list
