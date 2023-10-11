# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx

from ..._common.nx_compute_node_size_from_item_occ import (
    nx_compute_node_size_from_item_occ,
)
from ..._common.nx_compute_spring_layout import nx_compute_spring_layout
from ..._common.nx_compute_textfont_opacity_from_item_occ import (
    nx_compute_textfont_opacity_from_item_occ,
)
from ..._common.nx_compute_textfont_size_from_item_occ import (
    nx_compute_textfont_size_from_item_occ,
)
from ..._common.nx_compute_textposition_from_graph import (
    nx_compute_textposition_from_graph,
)
from ..._common.nx_visualize_graph import nx_visualize_graph


def correlation_map(
    similarity,
    #
    # LAYOUT:
    nx_k,
    nx_iterations,
    nx_random_state,
    #
    # NODES:
    node_color,
    node_size_range,
    textfont_size_range,
    textfont_opacity_range,
    #
    # EDGES:
    edge_top_n,
    edge_similarity_min,
    edge_widths,
    edge_colors,
    #
    # AXES:
    xaxes_range,
    yaxes_range,
    show_axes,
):
    #
    # Create a empty networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, similarity, node_color)
    nx_graph = __add_weighted_edges_from(
        nx_graph, similarity, edge_similarity_min, edge_top_n
    )

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the layout
    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_range)
    nx_graph = nx_compute_textfont_size_from_item_occ(nx_graph, textfont_size_range)
    nx_graph = nx_compute_textfont_opacity_from_item_occ(
        nx_graph, textfont_opacity_range
    )

    #
    # Sets the edge attributes
    nx_graph = __set_edge_properties(nx_graph, edge_colors, edge_widths)

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
    edge_similarity_min,
    edge_top_n,
):
    matrix = similarity.copy()

    stacked_matrix = matrix.stack().reset_index()
    stacked_matrix.columns = ["row", "col", "weight"]

    row_index_dict = {row: i for i, row in enumerate(matrix.index.tolist())}
    col_index_dict = {col: i for i, col in enumerate(matrix.columns.tolist())}
    stacked_matrix["i_row"] = stacked_matrix["row"].map(row_index_dict)
    stacked_matrix["i_col"] = stacked_matrix["col"].map(col_index_dict)
    stacked_matrix = stacked_matrix[stacked_matrix["i_col"] > stacked_matrix["i_row"]]
    stacked_matrix = stacked_matrix[stacked_matrix.weight > 0]
    if edge_similarity_min is not None:
        stacked_matrix = stacked_matrix[stacked_matrix.weight >= edge_similarity_min]
    stacked_matrix = stacked_matrix.sort_values(by="weight", ascending=False)

    if edge_top_n is not None:
        stacked_matrix = stacked_matrix.head(edge_top_n)

    for _, row in stacked_matrix.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row["row"], row["col"], row["weight"])],
        )

    # for i_row, row in enumerate(similarity.index.tolist()):
    #     for i_col, col in enumerate(similarity.columns.tolist()):
    #         #
    #         # Unicamente toma valores por encima de la diagonal principal
    #         if i_col <= i_row:
    #             continue

    #         weight = matrix.loc[row, col]
    #         if weight > 0:
    #             nx_graph.add_weighted_edges_from(
    #                 ebunch_to_add=[(row, col, weight)],
    #             )

    return nx_graph


def __set_edge_properties(nx_graph, edge_colors, edge_widths):
    for edge in nx_graph.edges():
        weight = nx_graph.edges[edge]["weight"]

        if weight < 0.25:
            width, dash = edge_widths[0], "dot"
            edge_color = edge_colors[0]

        elif weight < 0.5:
            width, dash = edge_widths[1], "dash"
            edge_color = edge_colors[1]

        elif weight < 0.75:
            width, dash = edge_widths[2], "solid"
            edge_color = edge_colors[2]

        else:
            width, dash = edge_widths[3], "solid"
            edge_color = edge_colors[3]

        nx_graph.edges[edge]["width"] = width
        nx_graph.edges[edge]["dash"] = dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
