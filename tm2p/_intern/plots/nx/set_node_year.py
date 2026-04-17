import networkx as nx  # type: ignore


def set_node_year(
    nx_graph: nx.Graph,
    i2y: dict[str, float],
) -> nx.Graph:
    for node in nx_graph.nodes():
        name = " ".join(node.split(" ")[:-1])
        nx_graph.nodes[node]["year"] = i2y[name]
    return nx_graph
