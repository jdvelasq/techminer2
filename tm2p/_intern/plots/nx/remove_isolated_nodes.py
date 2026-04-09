import networkx as nx  # type: ignore


def remove_isolated_nodes(nx_graph: nx.Graph) -> nx.Graph:
    nx_graph.remove_nodes_from(list(nx.isolates(nx_graph)))
    return nx_graph
