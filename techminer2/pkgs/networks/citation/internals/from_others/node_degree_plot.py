# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Node Degree Plot"""
from ......internals.mixins import InputFunctionsMixin
from ......internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degree_plot,
    internal__create_node_degrees_data_frame,
)
from ......internals.nx.assign_degree_to_nodes import internal__assign_degree_to_nodes
from .create_nx_graph import internal__create_nx_graph


class NodeDegreePlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__assign_degree_to_nodes(nx_graph)
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)
        plot = internal__create_node_degree_plot(data_frame)

        return plot
