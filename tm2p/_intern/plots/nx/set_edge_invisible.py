import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_edge_invisible(
    nx_graph: nx.Graph,
) -> nx.Graph:
    for edge in nx_graph.edges():
        nx_graph.edges[edge]["edge_color"] = "#f5f5f5"
        nx_graph.edges[edge]["width"] = 0.001

    return nx_graph
