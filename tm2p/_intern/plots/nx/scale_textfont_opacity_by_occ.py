import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_textfont_opacity_by_occ(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    textfont_opacity_range = params.textfont_opacity_range

    nodes = list(nx_graph.nodes())
    counters = [node.split(" ")[-1] for node in nodes]
    occ = [counter.split(":")[0] for counter in counters]
    occ = np.array([float(value) for value in occ])  # type: ignore

    if max(occ) == min(occ):
        textfont_opacities = np.array([textfont_opacity_range[0]] * len(occ))
    else:

        if params.node_scaling == Scaling.SQRT:
            occ = np.sqrt(occ)  # type: ignore
        if params.node_scaling == Scaling.LOG:
            occ = np.log1p(occ)  # type: ignore

        width = textfont_opacity_range[1] - textfont_opacity_range[0]
        prop = (occ - occ.min()) / (occ.max() - occ.min())  # type: ignore
        textfont_opacities = textfont_opacity_range[0] + prop * width

    for opacity, node in zip(textfont_opacities, nx_graph.nodes()):

        nx_graph.nodes[node]["textfont_opacity"] = opacity

        # nx_graph.nodes[node]["textfont_opacity"] = np.sqrt(
        #     np.sqrt(np.sqrt(np.sqrt(opacity)))
        # ) # old code

    return nx_graph
