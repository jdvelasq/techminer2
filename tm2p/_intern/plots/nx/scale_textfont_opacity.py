import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_textfont_opacity(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    textfont_opacity_range = params.textfont_opacity_range

    nodes = list(nx_graph.nodes())
    nodes = list(nx_graph.nodes())
    raw_sizes = [nx_graph.nodes[node]["raw_node_size"] for node in nodes]  # type: ignore

    if max(raw_sizes) == min(raw_sizes):
        textfont_opacities = np.array([textfont_opacity_range[0]] * len(raw_sizes))
    else:

        if params.node_scaling == Scaling.SQRT:
            raw_sizes = np.sqrt(raw_sizes)  # type: ignore
        if params.node_scaling == Scaling.LOG:
            raw_sizes = np.log1p(raw_sizes)  # type: ignore

        width = textfont_opacity_range[1] - textfont_opacity_range[0]
        prop = (raw_sizes - raw_sizes.min()) / (raw_sizes.max() - raw_sizes.min())  # type: ignore
        textfont_opacities = textfont_opacity_range[0] + prop * width

    for opacity, node in zip(textfont_opacities, nx_graph.nodes()):

        nx_graph.nodes[node]["textfont_opacity"] = opacity

    return nx_graph
