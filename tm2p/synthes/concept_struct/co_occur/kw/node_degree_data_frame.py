"""
Node Degree Frame
===============================================================================


Smoke tests:
    >>> from tm2p.co_occurrence_network.keywords import NodeDegreeDataFrame
    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_item_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head() # doctest: +SKIP
       Node                           Name  Degree
    0     0                FINTECH 32:5393      17
    1     1                FINANCE 11:1950      15
    2     2      FINANCIAL_SERVICE 08:1680      12
    3     3               COMMERCE 03:0846      12
    4     4  FINANCIAL_INSTITUTION 04:0746       9



"""

from tm2p._intern import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.node_degree_data_frame import (
    NodeDegreeDataFrame as UserNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .with_source_field("keywords")
            .run()
        )
