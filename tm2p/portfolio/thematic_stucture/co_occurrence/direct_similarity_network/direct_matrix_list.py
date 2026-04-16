"""
DirectMatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CoOccurrenceUnit, Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.direct_similarity_network import DirectMatrixList
    >>> df = (
    ...     DirectMatrixList()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
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
    >>> df.head(10).round(3)
                                    ROWS                            COLUMNS  ASSOC
    0  sustainable development 015:02158           sustainability 013:02308  0.041
    1           sustainability 013:02308  sustainable development 015:02158  0.041
    2                    china 018:03596  sustainable development 015:02158  0.022
    3  sustainable development 015:02158                    china 018:03596  0.022
    4                    china 018:03596           sustainability 013:02308  0.021
    5           sustainability 013:02308                    china 018:03596  0.021
    6               innovation 020:03916                    china 018:03596  0.019
    7                    china 018:03596               innovation 020:03916  0.019
    8               innovation 020:03916  sustainable development 015:02158  0.017
    9  sustainable development 015:02158               innovation 020:03916  0.017


    >>> df = (
    ...     DirectMatrixList()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
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
    >>> df.head(10).round(3)
                          ROWS                  COLUMNS  ASSOC
    0  sustainable development           sustainability  0.041
    1           sustainability  sustainable development  0.041
    2                    china  sustainable development  0.022
    3  sustainable development                    china  0.022
    4                    china           sustainability  0.021
    5           sustainability                    china  0.021
    6               innovation                    china  0.019
    7                    china               innovation  0.019
    8               innovation  sustainable development  0.017
    9  sustainable development               innovation  0.017


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
