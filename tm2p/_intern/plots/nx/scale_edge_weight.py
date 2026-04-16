import networkx as nx  # type: ignore
import numpy as np

from tm2p._intern import Params
from tm2p.enum import Scaling


def scale_edge_weight(params: Params, nx_graph: nx.Graph) -> nx.Graph:

    weights = np.array([data["weight"] for _, _, data in nx_graph.edges(data=True)])

    if params.edge_scaling == Scaling.SQRT:
        weights = np.sqrt(weights)
    if params.edge_scaling == Scaling.LOG:
        weights = np.log1p(weights)

    for weight, (u, v) in zip(weights, nx_graph.edges()):
        nx_graph.edges[u, v]["weight"] = weight

    return nx_graph
