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


def nx_compute_spring_layout(graph, k, iterations, seed):
    """Computes the layout of a networkx graph."""

    pos = nx.spring_layout(graph, k=k, iterations=iterations, seed=seed)
    for node in graph.nodes():
        graph.nodes[node]["x"] = pos[node][0]
        graph.nodes[node]["y"] = pos[node][1]
    return graph


def nx_compute_textposition(nx_graph):
    """Computes the text position for a node in a networkx graph."""

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]
    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]

    x_mean = np.mean(node_x)
    y_mean = np.mean(node_y)

    for node in nx_graph.nodes():
        x_pos = nx_graph.nodes[node]["x"]
        y_pos = nx_graph.nodes[node]["y"]

        if x_pos >= x_mean and y_pos >= y_mean:
            textposition = "top right"
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition = "top left"
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition = "bottom left"
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition = "bottom right"

        nx_graph.nodes[node]["textposition"] = textposition

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
