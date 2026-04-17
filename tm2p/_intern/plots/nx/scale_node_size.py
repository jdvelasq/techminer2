import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_node_size(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    node_size_range = params.node_size_range

    nodes = list(nx_graph.nodes())
    raw_sizes = [nx_graph.nodes[node]["raw_node_size"] for node in nodes]  # type: ignore

    if max(raw_sizes) == min(raw_sizes):
        node_sizes = np.array([node_size_range[0]] * len(raw_sizes))
    else:

        if params.node_scaling == Scaling.SQRT:
            raw_sizes = np.sqrt(raw_sizes)  # type: ignore
        if params.node_scaling == Scaling.LOG:
            raw_sizes = np.log1p(raw_sizes)  # type: ignore

        width = node_size_range[1] - node_size_range[0]
        prop = (raw_sizes - raw_sizes.min()) / (raw_sizes.max() - raw_sizes.min())  # type: ignore
        node_sizes = node_size_range[0] + prop * width

    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["node_size"] = size

    return nx_graph
