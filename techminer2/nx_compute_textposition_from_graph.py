# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np


def nx_compute_textposition_from_graph(nx_graph):
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
