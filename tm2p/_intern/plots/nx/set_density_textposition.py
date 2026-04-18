import networkx as nx  # type: ignore


def set_density_textposition(
    nx_graph: nx.Graph,
) -> nx.Graph:

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["textposition"] = "center center"

    return nx_graph
