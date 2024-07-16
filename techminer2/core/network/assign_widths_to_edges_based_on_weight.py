# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np


def assign_widths_to_edges_based_on_weight(
    nx_graph,
    edge_width_range,
):
    #
    widths = np.array([nx_graph.edges[edge]["weight"] for edge in nx_graph.edges()])

    #
    # Sets the lower value to edge_width_min
    min_width = min(widths)
    widths = widths - min_width + edge_width_range[0]

    #
    # Checks if widths.max() > edge_width_max and, if so, rescales
    if widths.max() > edge_width_range[1]:
        #
        # Scales the edge width to the range [edge_width_min, edge_width_max]
        widths -= edge_width_range[0]
        widths /= widths.max() - edge_width_range[0]
        widths *= edge_width_range[1] - edge_width_range[0]
        widths += edge_width_range[0]

    #
    # Sets the value of edge_width
    for width, edge in zip(widths, nx_graph.edges()):
        nx_graph.edges[edge]["width"] = width

    return nx_graph
