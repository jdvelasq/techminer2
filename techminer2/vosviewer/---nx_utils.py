# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""Utils based on networkx"""

import networkx as nx
import numpy as np
import plotly.express as px
from cdlib import algorithms

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


#
#
# VOSviewer-based functions
#
#


def nx_set_node_color_by_group(nx_graph):
    """Modifies the color of the nodes according to the group."""

    for node in nx_graph.nodes():
        i_group = nx_graph.nodes[node]["group"]
        nx_graph.nodes[node]["color"] = CLUSTER_COLORS[i_group]

    return nx_graph


def nx_scale_edge_width(
    nx_graph,
    edge_width_min,
    edge_width_max,
):
    #
    # Set the lower value of the edge width to node_size_min
    values = np.array([nx_graph.edges[edge]["width"] for edge in nx_graph.edges()])
    min_value = min(values)
    values = values - min_value + edge_width_min

    max_value = values.max()
    if max_value > edge_width_max:
        values = edge_width_min + (values - edge_width_min) / (max_value - edge_width_min) * (
            edge_width_max - edge_width_min
        )

    #
    # Sets the value of node_size
    for width, edge in zip(values, nx_graph.edges()):
        nx_graph.edges[edge]["width"] = width

    return nx_graph


def nx_scale_node_size_prop_to_occ_property(
    nx_graph,
    node_size_min,
    node_size_max,
):
    #
    # Set the lower value of the node size to node_size_min
    occ = np.array([nx_graph.nodes[node]["OCC"] for node in nx_graph.nodes()])
    min_occ = min(occ)
    occ = occ - min_occ + node_size_min
    node_sizes = occ

    #
    # checks if the max value is greater than node_size_max and scales the
    # sizes between node_size_min and node_size_max
    max_value = occ.max()
    if max_value > node_size_max:
        node_sizes = node_size_min + (occ - node_size_min) / (max_value - node_size_min) * (
            node_size_max - node_size_min
        )

    #
    # Sets the value of node_size
    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["node_size"] = size

    return nx_graph


def nx_scale_textfont_size_prop_to_occ_property(
    nx_graph,
    textfont_size_min,
    textfont_size_max,
):
    #
    # Set the lower value of the textfont size to textfont_size_min
    occ = np.array([nx_graph.nodes[node]["OCC"] for node in nx_graph.nodes()])
    min_occ = min(occ)
    occ = occ - min_occ + textfont_size_min
    textfont_sizes = occ

    #
    # Checks the maximum value of textfont sizes and scales the sizes between
    # textfont_size_min and textfont_size_max
    max_value = occ.max()
    if max_value > textfont_size_max:
        textfont_sizes = textfont_size_min + (occ - textfont_size_min) / (
            max_value - textfont_size_min
        ) * (textfont_size_max - textfont_size_min)

    #
    # Sets the value of textfont_size
    for size, node in zip(textfont_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["textfont_size"] = size

    return nx_graph


def nx_scale_textfont_opacity_prop_to_occ_property(
    nx_graph,
    textfont_opacity_min,
    textfont_opacity_max,
):
    #
    # Set the lower value of the textfont opacity to textfont_opacity_min
    occ = np.array([nx_graph.nodes[node]["OCC"] for node in nx_graph.nodes()])
    min_occ = min(occ)
    occ = occ - min_occ + textfont_opacity_min
    textfont_opacities = occ

    #
    # Checks the maximum value of textfont opacities and scales the opacities
    max_value = occ.max()
    if max_value > textfont_opacity_max:
        textfont_opacities = textfont_opacity_min + (occ - textfont_opacity_min) / (
            max_value - textfont_opacity_min
        ) * (textfont_opacity_max - textfont_opacity_min)

    #
    # Transforms the opacities to colors
    colors = px.colors.sequential.Greys
    textfont_colors = np.array(colors)[np.round(textfont_opacities * (len(colors) - 1)).astype(int)]

    for index, node in enumerate(nx_graph.nodes()):
        nx_graph.nodes[node]["textfont_color"] = textfont_colors[index]

    return nx_graph


def nx_scale_links(nx_graph, link_width_min, link_width_max):
    """Scales the width of the links in a networkx graph."""

    links = [nx_graph.edges[edge]["weight"] for edge in nx_graph.edges()]
    links = np.array(links)
    links = links / np.max(links)
    links = links * (link_width_max - link_width_min) + link_width_min

    for i, edge in enumerate(nx_graph.edges()):
        nx_graph.edges[edge]["width"] = links[i]

    return nx_graph