# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx
import numpy as np
import plotly.express as px

from ....nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ

# from ....vosviewer.nx_utils import (
#     nx_compute_spring_layout,
#     nx_compute_textposition,
#     nx_scale_node_size_prop_to_occ_property,
#     nx_scale_textfont_opacity_prop_to_occ_property,
#     nx_scale_textfont_size_prop_to_occ_property,
# )
# from ....vosviewer.px_utils import px_create_network_chart
from ....nx_compute_spring_layout import nx_compute_spring_layout
from ....nx_compute_textfont_opacity_from_item_occ import nx_compute_textfont_opacity_from_item_occ
from ....nx_compute_textfont_size_from_item_occ import nx_compute_textfont_size_from_item_occ
from ....nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ....nx_visualize_graph import nx_visualize_graph


def correlation_map(
    similarity,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES:
    edge_color="#7793a5",
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    #
    # Create a empty networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, similarity)
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
    nx_graph = __set_edge_properties(nx_graph, edge_color)

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

    ###
    ###
    ###

    # #
    # # Creates the nodes of the graph
    # #
    # nodes = similarity.index.tolist()

    # for node in nodes:
    #     nx_graph.add_nodes_from(
    #         #
    #         # NODE NAME:
    #         [node],
    #         #
    #         # NODE ATTR:
    #         text=" ".join(node.split(" ")[:-1]),
    #         OCC=int(node.split(" ")[-1].split(":")[0]),
    #         global_citations=int(node.split(" ")[-1].split(":")[0]),
    #         #
    #         # OTHER ATTR:
    #         group=0,
    #         color=edge_color,
    #         # node_size=node_size,
    #         # textfont_color=textfont_color,
    #         # textfont_size=textfont_size,
    #     )

    # #
    # # Scales the node size
    # nx_graph = nx_scale_node_size_prop_to_occ_property(
    #     nx_graph, node_size_min, node_size_max
    # )

    # #
    # # Scales the font size
    # nx_graph = nx_scale_textfont_size_prop_to_occ_property(
    #     nx_graph, textfont_size_min, textfont_size_max
    # )

    # #
    # # Scales the font color
    # nx_graph = nx_scale_textfont_opacity_prop_to_occ_property(
    #     nx_graph,
    #     textfont_opacity_min=0.35,
    #     textfont_opacity_max=1.00,
    # )

    # #
    # #
    # # Adds edges to the graph
    # #
    # #
    # for i_row in range(similarity.shape[0]):
    #     for i_col in range(i_row + 1, similarity.shape[1]):
    #         if similarity.iloc[i_row, i_col] > 0:
    #             #
    #             source_node = similarity.index[i_row]
    #             target_node = similarity.columns[i_col]
    #             weight = similarity.iloc[i_row, i_col]

    #             #
    #             # Sets the properties for correlation maps
    #             #
    #             if weight < 0.25:
    #                 width, dash = 2, "dot"

    #             elif weight < 0.5:
    #                 width, dash = 2, "dash"

    #             elif weight < 0.75:
    #                 width, dash = 4, "solid"

    #             else:
    #                 width, dash = 6, "solid"

    #             nx_graph.add_weighted_edges_from(
    #                 ebunch_to_add=[(source_node, target_node, weight)],
    #                 width=width,
    #                 dash=dash,
    #                 color="#b8c6d0",
    #             )

    # nx_graph = nx_compute_spring_layout(
    #     graph=nx_graph, k=nx_k, iterations=nx_iterations, seed=nx_random_state
    # )

    # nx_graph = nx_compute_textposition(nx_graph)

    # fig = px_create_network_chart(
    #     nx_graph=nx_graph,
    #     xaxes_range=xaxes_range,
    #     yaxes_range=yaxes_range,
    #     show_axes=show_axes,
    #     n_labels=n_labels,
    # )

    # return fig


#
#
#
def __add_nodes_from(
    nx_graph,
    similarity,
):
    matrix = similarity.copy()
    nodes = matrix.columns.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color="#7793a5")

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


def __set_edge_properties(nx_graph, edge_color):
    for edge in nx_graph.edges():
        weight = nx_graph.edges[edge]["weight"]

        if weight < 0.25:
            width, dash = 2, "dot"

        elif weight < 0.5:
            width, dash = 2, "dash"

        elif weight < 0.75:
            width, dash = 4, "solid"

        else:
            width, dash = 6, "solid"

        nx_graph.edges[edge]["width"] = width
        nx_graph.edges[edge]["dash"] = dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
