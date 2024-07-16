# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ..assign_colors_to_edges_based_on_weight import assign_colors_to_edges_based_on_weight
from ..assign_colors_to_nodes_by_group_attribute import assign_colors_to_nodes_by_group_attribute
from ..assign_opacity_to_text_based_on_frequency import assign_opacity_to_text_based_on_frequency
from ..assign_sizes_to_nodes_based_on_occurrences import assign_sizes_to_nodes_based_on_occurrences
from ..assign_text_positions_to_nodes_by_quadrants import assign_text_positions_to_nodes_by_quadrants
from ..assign_textfont_sizes_to_nodes_based_on_occurrences import assign_textfont_sizes_to_nodes_based_on_occurrences
from ..assign_uniform_color_to_edges import assign_uniform_color_to_edges

#
# Creates a co-occurrence networkx graph from a co-occurrence matrix.
#
from ..assign_widths_to_edges_based_on_weight import assign_widths_to_edges_based_on_weight
from ..compute_spring_layout_positions import compute_spring_layout_positions


def create_co_occurrence_networkx_graph(
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
    nx_graph = compute_spring_layout_positions(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = assign_colors_to_nodes_by_group_attribute(nx_graph)
    nx_graph = assign_sizes_to_nodes_based_on_occurrences(nx_graph, node_size_range)
    nx_graph = assign_textfont_sizes_to_nodes_based_on_occurrences(nx_graph, textfont_size_range)
    nx_graph = assign_opacity_to_text_based_on_frequency(nx_graph, textfont_opacity_range)

    #
    # Sets the edge attributes
    nx_graph = assign_widths_to_edges_based_on_weight(nx_graph, edge_width_range)
    nx_graph = assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = assign_uniform_color_to_edges(nx_graph, edge_color)
    nx_graph = assign_colors_to_edges_based_on_weight(nx_graph)

    return nx_graph
