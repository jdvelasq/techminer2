import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_textfont_size(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    textfont_size_range = params.textfont_size_range

    nodes = list(nx_graph.nodes())
    raw_sizes = [nx_graph.nodes[node]["raw_node_size"] for node in nodes]  # type: ignore

    percentile_75 = None

    if max(raw_sizes) == min(raw_sizes):
        node_sizes = np.array([textfont_size_range[0]] * len(raw_sizes))
    else:

        if params.node_scaling == Scaling.SQRT:
            raw_sizes = np.sqrt(raw_sizes)  # type: ignore
        if params.node_scaling == Scaling.LOG:
            raw_sizes = np.log1p(raw_sizes)  # type: ignore

        width = textfont_size_range[1] - textfont_size_range[0]
        prop = (raw_sizes - raw_sizes.min()) / (raw_sizes.max() - raw_sizes.min())  # type: ignore
        node_sizes = textfont_size_range[0] + prop * width

        percentile_75 = np.percentile(node_sizes, 75)

    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["textfont_size"] = size

        if percentile_75 is not None:
            if size >= percentile_75:
                nx_graph.nodes[node]["bold"] = True

    return nx_graph
