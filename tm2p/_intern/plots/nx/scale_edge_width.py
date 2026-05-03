import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params


def scale_edge_width(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    edge_width_range = params.edge_width_range

    widths = np.array([data["width"] for _, _, data in nx_graph.edges(data=True)])
    mask = widths > 0.001

    if max(widths) == min(widths):
        widths = np.array([widths[0]] * len(widths))
    else:

        length = edge_width_range[1] - edge_width_range[0]
        prop = (widths - widths.min()) / (widths.max() - widths.min())
        widths = edge_width_range[0] + prop * length

    for m, width, (u, v) in zip(mask, widths, nx_graph.edges()):
        if m:
            nx_graph.edges[u, v]["width"] = width
        else:
            nx_graph.edges[u, v]["width"] = 0.01

    return nx_graph
