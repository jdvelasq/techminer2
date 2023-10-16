"""This module contains functions for network analysis that are common to
several modules.


"""

from collections import defaultdict

import networkx as nx
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from cdlib import algorithms

# from .api.records.matrix.co_occurrence_matrix.list_cells_in_matrix import (
#     AutoCorrCellsList,
#     CoocCellsList,
#     list_cells_in_matrix,
# )
from ._read_records import read_records

# from .vantagepoint.discover.matrix.list_cells_in_matrix import (
#     list_cells_in_matrix,
# )

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


def nx_add_nodes__to_graph_from_matrix(graph, matrix):
    """Creates nodes from 'row' and 'column' columns in a matrix list."""

    # Adds the items in 'row' column as nodes
    nodes = matrix.df_.index.to_list()
    nodes = [
        (node, {"group": 0, "color": "#7793a5", "textfont_color": "black"})
        for node in nodes
    ]
    graph.add_nodes_from(nodes)

    if matrix.rows_ != matrix.columns_:
        # Adds the items in 'column' column as nodes
        nodes = matrix.df_.columns.to_list()
        nodes = [
            (node, {"group": 1, "color": "#465c6b", "textfont_color": "black"})
            for node in nodes
        ]
        graph.add_nodes_from(nodes)

    return graph


def nx_add_edges_to_graph_from_matrix(graph, matrix):
    """Creates edges from 'row' and 'column' columns in a matrix list."""

    matrix_list = list_cells_in_matrix(matrix)
    return nx_add_edges_to_graph_from_matrix_list(graph, matrix_list)


def nx_add_edges_to_graph_from_matrix_list(graph, matrix_list):
    """Creates edges from 'row' and 'column' columns in a matrix list."""

    # table = matrix_list.df_.copy()

    # if isinstance(matrix_list, AutoCorrCellsList):
    #     table = table[table["row"] < table["column"]]
    #     table = table.loc[table.CORR > 0, :]

    # elif isinstance(matrix_list, CoocCellsList):
    #     table = table[table["row"] < table["column"]]
    #     table = table.loc[table.OCC > 0, :]

    # else:
    #     table = table[table[matrix_list.metric_] > 0]

    table = matrix_list.copy()

    for _, row in table.iterrows():
        if row[2] != 0 and row[0] != row[1]:
            graph.add_edges_from(
                [(row[0], row[1])],
                value=row[2],
                width=2,
                dash="solid",
                color="#7793a5",
            )

    return graph


# =============================================================================
#
#
# Functions for manipulating networkx graphs
#
#
def nx_create_graph_from_matrix(
    matrix,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
):
    """Creates a networkx graph from a matrix list."""

    graph = nx.Graph()

    graph = nx_add_nodes_to_graph_from_matrix(graph, matrix)
    graph = nx_create_node_occ_property_from_node_name(graph)
    graph = nx_compute_node_property_from_occ(
        graph, "node_size", node_size_min, node_size_max
    )
    graph = nx_compute_node_property_from_occ(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )

    graph = nx_add_edges_to_graph_from_matrix(graph, matrix)

    return graph


def nx_add_nodes_to_graph_from_matrix(graph, matrix):
    """Creates nodes from 'row' and 'column' columns in a matrix list."""

    # adds items in 'row' column as nodes
    nodes = matrix.index.to_list()
    nodes = [
        (node, {"group": 0, "color": "#7793a5", "textfont_color": "black"})
        for node in nodes
    ]
    graph.add_nodes_from(nodes)

    # adds items in 'column' column as nodes
    candidates = matrix.columns.to_list()
    nodes = []
    for candidate in candidates:
        if candidate not in graph.nodes:
            nodes.append(candidate)
    if len(nodes) > 0:
        nodes = [
            (node, {"group": 1, "color": "#465c6b", "textfont_color": "black"})
            for node in nodes
        ]
        graph.add_nodes_from(nodes)

    return graph


def nx_create_graph_from_matrix_list(
    matrix_list,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
):
    """Creates a networkx graph from a matrix list."""

    graph = nx.Graph()

    graph = nx_add_nodes__to_graph_from_matrix_list(graph, matrix_list)
    graph = nx_create_node_occ_property_from_node_name(graph)
    graph = nx_compute_node_property_from_occ(
        graph, "node_size", node_size_min, node_size_max
    )
    graph = nx_compute_node_property_from_occ(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )

    graph = nx_add_edges_to_graph_from_matrix_list(graph, matrix_list)

    return graph


def nx_add_nodes__to_graph_from_matrix_list(graph, matrix_list):
    """Creates nodes from 'row' and 'column' columns in a matrix list."""

    # adds items in 'row' column as nodes
    nodes = matrix_list.df_["row"].drop_duplicates().to_list()
    nodes = [
        (node, {"group": 0, "color": "#7793a5", "textfont_color": "black"})
        for node in nodes
    ]
    graph.add_nodes_from(nodes)

    # adds items in 'column' column as nodes
    candidates = matrix_list.df_["column"].drop_duplicates().to_list()
    nodes = []
    for candidate in candidates:
        if candidate not in graph.nodes:
            nodes.append(candidate)
    if len(nodes) > 0:
        nodes = [
            (node, {"group": 1, "color": "#465c6b", "textfont_color": "black"})
            for node in nodes
        ]
        graph.add_nodes_from(nodes)

    return graph


def nx_create_node_occ_property_from_node_name(graph):
    """Adds OCC value as a property of the node in a graph."""

    for node in graph.nodes():
        occ = node.split(" ")[-1]
        occ = occ.split(":")[0]
        occ = int(occ)
        graph.nodes[node]["OCC"] = occ

    return graph


def nx_compute_circular_layout(graph):
    """Computes a circular layout with the last node as center"""

    pos = nx.circular_layout(graph)
    last_node = list(graph.nodes())[-1]
    for node in graph.nodes():
        if node == last_node:
            graph.nodes[node]["pos"] = [0, 0]
        else:
            graph.nodes[node]["pos"] = pos[node]

    return graph


def nx_compute_spectral_layout(graph, scale):
    """Computes the layout of a networkx graph."""
    pos = nx.spectral_layout(graph, scale=scale)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


# pylint: disable=invalid-name
def nx_compute_node_statistics(graph):
    """Compute network statistics."""

    nodes = list(graph.nodes())
    degree = [graph.nodes[node]["degree"] for node in nodes]
    occ = [graph.nodes[node]["OCC"] for node in nodes]
    occ_gc = [node.split(" ")[-1] for node in nodes]
    gc = [int(text.split(":")[-1]) for text in occ_gc]
    betweenness = nx.betweenness_centrality(graph)
    closeness = nx.closeness_centrality(graph)
    pagerank = nx.pagerank(graph)

    # Callon centrality  - density
    callon_matrix = nx_graph_to_co_occ_matrix(graph).astype(float)
    callon_centrality = callon_matrix.values.diagonal()
    callon_density = callon_matrix.sum() - callon_centrality

    # strategic_diagram["callon_centrality"] *= 10
    # strategic_diagram["callon_density"] *= 100

    indicators = pd.DataFrame(
        {
            "Degree": degree,
            "Betweenness": betweenness,
            "Closeness": closeness,
            "PageRank": pagerank,
            "Centrality": callon_centrality,
            "Density": callon_density,
            "_occ_": occ,
            "_gc_": gc,
            "_name_": nodes,
        },
        index=nodes,
    )

    indicators = indicators.sort_values(
        by=["Degree", "_occ_", "_gc_", "_name_"],
        ascending=[False, False, False, True],
    )

    indicators = indicators.drop(columns=["_occ_", "_gc_", "_name_"])

    return indicators


def nx_compute_node_textfont_color_from_occ(graph):
    """Computes the textfont color for each node in a networkx graph."""

    occ = [graph.nodes[node]["OCC"] for node in graph.nodes()]
    occ_scaled = nx_scale_node_occ(occ, max_size=1.0, min_size=0.40)
    colors = px.colors.sequential.Greys
    textfont_color = np.array(colors)[
        np.round(occ_scaled * (len(colors) - 1)).astype(int)
    ]

    for index, node in enumerate(graph.nodes()):
        graph.nodes[node]["textfont_color"] = textfont_color[index]

    return graph


def nx_compute_node_property_from_occ(graph, prop, min_size, max_size):
    """Compute key size for a networkx graph from OCC property of the node."""

    if min_size == max_size:
        for index, node in enumerate(graph.nodes()):
            graph.nodes[node][prop] = min_size
        return graph

    occ = [graph.nodes[node]["OCC"] for node in graph.nodes()]

    occ_scaled = nx_scale_node_occ(occ, max_size, min_size)

    for index, node in enumerate(graph.nodes()):
        graph.nodes[node][prop] = occ_scaled[index]

    return graph


def nx_compute_textposition_from_graph(graph):
    """Computes the text position for a node in a networkx graph."""

    node_x, node_y = nx_extract_node_coordinates(graph)

    return nx_compute_node_textposition_from_node_coordinates(node_x, node_y)


def nx_compute_node_textposition_from_node_coordinates(node_x, node_y):
    """Computes the text positon for a node from its x and y coordinates."""

    x_mean = np.mean(node_x)
    y_mean = np.mean(node_y)

    textposition = []

    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition.append("top right")
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition.append("top left")
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition.append("bottom left")
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition.append("bottom right")

    return textposition


def nx_extract_node_textfont_colors(graph):
    """Extracts textfont colors from a networkx graph."""

    textfont_colors = []
    for node in graph.nodes():
        textfont_colors.append(graph.nodes[node]["textfont_color"])

    return textfont_colors


def nx_extract_node_textfont_sizes(graph):
    """Extracts textfont sizes from a networkx graph."""

    textfont_sizes = []
    for node in graph.nodes():
        textfont_sizes.append(graph.nodes[node]["textfont_size"])

    return textfont_sizes


def nx_extract_node_colors(graph):
    """Extracts node colors from a networkx graph."""

    node_colors = []
    for node in graph.nodes():
        node_colors.append(graph.nodes[node]["color"])

    return node_colors


def nx_extract_node_coordinates(graph):
    """Extracts node coordinates from a networkx graph."""

    node_x = []
    node_y = []
    for node in graph.nodes():
        pos_x, pos_y = graph.nodes[node]["pos"]
        node_x.append(pos_x)
        node_y.append(pos_y)

    return node_x, node_y


def nx_extract_node_names(graph):
    """Extracts node names from a networkx graph."""

    node_names = []
    for node in graph.nodes():
        node_names.append(node)

    return node_names


def nx_extract_node_sizes(graph):
    """Extracts node sizes from a networkx graph."""

    node_sizes = []
    for node in graph.nodes():
        if "node_size" not in graph.nodes[node]:
            raise ValueError(f"Node {node} does not have a node_size property.")
        node_sizes.append(graph.nodes[node]["node_size"])

    return node_sizes


def nx_extract_node_occ(graph):
    """Extracts node sizes from a networkx graph."""

    occ = []
    for node in graph.nodes():
        if "OCC" not in graph.nodes[node]:
            raise ValueError(f"Node {node} does not have a node_size property.")
        occ.append(graph.nodes[node]["OCC"])

    return occ


def nx_node_occ_to_node_textfont_color(occ):
    """Computes the textfont color from an OCC list."""
    occ_scaled = nx_scale_node_occ(occ, max_size=1.0, min_size=0.35)
    colors = px.colors.sequential.Greys
    textfont_color = np.array(colors)[
        np.round(occ_scaled * (len(colors) - 1)).astype(int)
    ]
    return textfont_color


def nx_scale_node_occ(occ, max_size, min_size):
    """Scales the OCC values to a range of sizes."""

    occ = np.array(occ)
    min_occ = occ.min()
    occ = occ - min_occ + min_size
    max_value = occ.max()
    if max_value > max_size:
        occ = min_size + (occ - min_size) / (max_value - min_size) * (
            max_size - min_size
        )
    return occ


def nx_graph_to_co_occ_matrix(graph):
    """Reconstructs the co-occurrence matrix from a graph."""

    matrix = nx.to_pandas_adjacency(graph)
    matrix = matrix.astype(int)
    matrix.loc[:, :] = 0

    for node in graph.nodes():
        matrix.loc[node, node] = graph.nodes[node]["OCC"]

    for edge in graph.edges():
        matrix.loc[edge[0], edge[1]] = graph.edges[edge]["value"]
        matrix.loc[edge[1], edge[0]] = graph.edges[edge]["value"]

    return matrix


def nx_set_node_colors(graph, node_names, new_color):
    """Sets node colors in a networkx graph."""

    for node in graph.nodes():
        if node in node_names:
            graph.nodes[node]["color"] = new_color

    return graph


# def nx_set_edge_properties_for_corr_maps(graph, color):
#     """Sets edge properties for correlation maps."""

#     for edge in graph.edges():
#         if graph.edges[edge]["value"] < 0.25:
#             graph.edges[edge]["width"] = 2
#             graph.edges[edge]["dash"] = "dot"
#             graph.edges[edge]["color"] = color

#         elif graph.edges[edge]["value"] < 0.5:
#             graph.edges[edge]["width"] = 2
#             graph.edges[edge]["dash"] = "solid"
#             graph.edges[edge]["color"] = color

#         elif graph.edges[edge]["value"] < 0.75:
#             graph.edges[edge]["width"] = 4
#             graph.edges[edge]["dash"] = "solid"
#             graph.edges[edge]["color"] = color

#         else:
#             graph.edges[edge]["width"] = 6
#             graph.edges[edge]["dash"] = "solid"
#             graph.edges[edge]["color"] = color

#     return graph


def nx_set_edge_properties_for_co_occ_networks(graph):
    """Sets edge properties for co-occurrence networks."""

    for edge in graph.edges():
        graph.edges[edge]["width"] = 1
        graph.edges[edge]["color"] = "lightgray"

    graph = nx_compute_node_textfont_color_from_occ(graph)

    return graph


###############################################################################
