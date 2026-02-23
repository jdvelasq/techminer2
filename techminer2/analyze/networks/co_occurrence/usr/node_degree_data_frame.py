"""
Node Degree Frame
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.user import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/data/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       Node                        Name  Degree
    0     0             FINTECH 32:5393      16
    1     1             FINANCE 11:1950      15
    2     2            COMMERCE 03:0846      11
    3     3   FINANCIAL_SERVICE 04:1036      10
    4     4  FINANCIAL_SERVICES 05:0746       9



"""

from techminer2._internals import ParamsMixin
from techminer2._internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degrees_data_frame,
)
from techminer2.analyze.networks.co_occurrence._internals.create_nx_graph import (
    internal__create_nx_graph,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__assign_degree_to_nodes(nx_graph)
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)

        return data_frame
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)

        return data_frame
