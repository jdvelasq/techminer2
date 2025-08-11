# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Node Degree Frame"""
from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degrees_data_frame,
)
from techminer2.packages.networks.citation._internals.from_others.create_nx_graph import (
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
