import networkx as nx  # type: ignore


def set_node_year(
    nx_graph: nx.Graph,
    i2y: dict[str, float],
) -> nx.Graph:
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["group"] = i2y[node]
    return nx_graph
