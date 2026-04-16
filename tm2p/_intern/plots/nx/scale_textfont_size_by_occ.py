import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_textfont_size_by_occ(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    textfont_size_range = params.textfont_size_range

    nodes = list(nx_graph.nodes())
    counters = [node.split(" ")[-1] for node in nodes]
    occ = [counter.split(":")[0] for counter in counters]
    occ = np.array([float(value) for value in occ])  # type: ignore

    percentile_75 = None

    if max(occ) == min(occ):
        node_sizes = np.array([textfont_size_range[0]] * len(occ))
    else:

        if params.node_scaling == Scaling.SQRT:
            occ = np.sqrt(occ)  # type: ignore
        if params.node_scaling == Scaling.LOG:
            occ = np.log1p(occ)  # type: ignore

        width = textfont_size_range[1] - textfont_size_range[0]
        prop = (occ - occ.min()) / (occ.max() - occ.min())  # type: ignore
        node_sizes = textfont_size_range[0] + prop * width

        percentile_75 = np.percentile(node_sizes, 75)

    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["textfont_size"] = size

        if percentile_75 is not None:
            if size >= percentile_75:
                nx_graph.nodes[node]["bold"] = True

    return nx_graph
