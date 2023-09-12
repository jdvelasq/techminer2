# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np


def nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max):
    #
    widths = np.array([nx_graph.edges[edge]["weight"] for edge in nx_graph.edges()])

    #
    # Sets the lower value to edge_width_min
    min_width = min(widths)
    widths = widths - min_width + edge_width_min

    #
    # Checks if widths.max() > edge_width_max and, if so, rescales
    if widths.max() > edge_width_max:
        #
        # Scales the edge width to the range [edge_width_min, edge_width_max]
        widths -= edge_width_min
        widths /= widths.max() - edge_width_min
        widths *= edge_width_max - edge_width_min
        widths += edge_width_min

    #
    # Sets the value of edge_width
    for width, edge in zip(widths, nx_graph.edges()):
        nx_graph.edges[edge]["width"] = width

    return nx_graph
