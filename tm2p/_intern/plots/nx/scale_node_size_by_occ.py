import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_node_size_by_occ(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    node_size_range = params.node_size_range

    nodes = list(nx_graph.nodes())
    counters = [node.split(" ")[-1] for node in nodes]
    occ = [counter.split(":")[0] for counter in counters]
    occ = np.array([float(value) for value in occ])  # type: ignore

    if max(occ) == min(occ):
        node_sizes = np.array([node_size_range[0]] * len(occ))
    else:

        if params.node_scaling == Scaling.SQRT:
            occ = np.sqrt(occ)  # type: ignore
        if params.node_scaling == Scaling.LOG:
            occ = np.log1p(occ)  # type: ignore

        width = node_size_range[1] - node_size_range[0]
        prop = (occ - occ.min()) / (occ.max() - occ.min())  # type: ignore
        node_sizes = node_size_range[0] + prop * width

    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["node_size"] = size

    return nx_graph
