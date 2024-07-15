# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

#
# Creates a co-occurrence networkx graph from a co-occurrence matrix.
#
from ..nx_compute_edge_width_from_edge_weight import (
    nx_compute_edge_width_from_edge_weight,
)
from ..nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from ..nx_compute_spring_layout import nx_compute_spring_layout
from ..nx_compute_textfont_opacity_from_item_occ import (
    nx_compute_textfont_opacity_from_item_occ,
)
from ..nx_compute_textfont_size_from_item_occ import (
    nx_compute_textfont_size_from_item_occ,
)
from ..nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ..nx_set_edge_color_from_palette import nx_set_edge_color_from_palette
from ..nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from ..nx_set_node_color_from_group_attr import nx_set_node_color_from_group_attr


def create_graph_from_co_occurrence_network(
    #
    # NETWORK:
    nx_graph,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
):
    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_set_node_color_from_group_attr(nx_graph)
    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_range)
    nx_graph = nx_compute_textfont_size_from_item_occ(nx_graph, textfont_size_range)
    nx_graph = nx_compute_textfont_opacity_from_item_occ(nx_graph, textfont_opacity_range)

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_range)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)
    nx_graph = nx_set_edge_color_from_palette(nx_graph)

    return nx_graph
