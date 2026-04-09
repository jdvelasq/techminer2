import networkx as nx  # type: ignore


def remove_selfloop_edges(nx_graph: nx.Graph) -> nx.Graph:
    nx_graph.remove_edges_from(nx.selfloop_edges(nx_graph))
    return nx_graph
