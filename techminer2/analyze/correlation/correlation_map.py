# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx

from ..._common.nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from ..._common.nx_compute_spring_layout import nx_compute_spring_layout
from ..._common.nx_compute_textfont_opacity_from_item_occ import (
    nx_compute_textfont_opacity_from_item_occ,
)
from ..._common.nx_compute_textfont_size_from_item_occ import nx_compute_textfont_size_from_item_occ
from ..._common.nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ..._common.nx_visualize_graph import nx_visualize_graph


def correlation_map(
    similarity,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_color="#7793a5",
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES:
    edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    #
    # Create a empty networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, similarity, node_color)
    nx_graph = __add_weighted_edges_from(nx_graph, similarity)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the layout
    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_min, node_size_max)
    nx_graph = nx_compute_textfont_size_from_item_occ(
        nx_graph, textfont_size_min, textfont_size_max
    )
    nx_graph = nx_compute_textfont_opacity_from_item_occ(
        nx_graph, textfont_opacity_min, textfont_opacity_max
    )

    #
    # Sets the edge attributes
    nx_graph = __set_edge_properties(nx_graph, edge_colors)

    #
    #
    nx_graph = nx_compute_textposition_from_graph(nx_graph)

    return nx_visualize_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )


#
#
#
def __add_nodes_from(
    nx_graph,
    similarity,
    node_color,
):
    matrix = similarity.copy()
    nodes = matrix.columns.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color=node_color)

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    similarity,
):
    matrix = similarity.copy()

    for i_row, row in enumerate(similarity.index.tolist()):
        for i_col, col in enumerate(similarity.columns.tolist()):
            #
            # Unicamente toma valores por encima de la diagonal principal
            if i_col <= i_row:
                continue

            weight = matrix.loc[row, col]
            if weight > 0:
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                )

    return nx_graph


def __set_edge_properties(nx_graph, edge_colors):
    for edge in nx_graph.edges():
        weight = nx_graph.edges[edge]["weight"]

        if weight < 0.25:
            width, dash = 2, "dot"
            edge_color = edge_colors[0]

        elif weight < 0.5:
            width, dash = 2, "dash"
            edge_color = edge_colors[1]

        elif weight < 0.75:
            width, dash = 4, "solid"
            edge_color = edge_colors[2]

        else:
            width, dash = 6, "solid"
            edge_color = edge_colors[3]

        nx_graph.edges[edge]["width"] = width
        nx_graph.edges[edge]["dash"] = dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
