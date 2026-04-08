import numpy as np


def assign_edge_widths_based_on_weight(
    params,
    nx_graph,
):
    edge_width_range = params.edge_width_range

    widths = np.array([nx_graph.edges[edge]["weight"] for edge in nx_graph.edges()])

    if max(widths) == min(widths):
        widths = np.array([widths[0]] * len(widths))
    else:

        length = edge_width_range[1] - edge_width_range[0]
        prop = (widths - widths.min()) / (widths.max() - widths.min())
        widths = edge_width_range[0] + prop * length

    #
    # Sets the value of edge_width
    for width, edge in zip(widths, nx_graph.edges()):
        nx_graph.edges[edge]["width"] = width

    return nx_graph
