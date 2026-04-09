import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_uniform_edge_color(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    for edge in nx_graph.edges():
        nx_graph.edges[edge]["color"] = params.edge_color
    return nx_graph
