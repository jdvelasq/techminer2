import networkx as nx  # type: ignore


def set_node_group(
    nx_graph: nx.Graph,
    i2c: dict[str, int],
) -> nx.Graph:
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["group"] = i2c[node]
    return nx_graph
