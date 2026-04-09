import networkx as nx  # type: ignore


def set_uniform_edge_line_style(
    nx_graph: nx.Graph,
    edge_line_style: str = "solid",
) -> nx.Graph:
    for edge in nx_graph.edges():
        nx_graph.edges[edge]["dash"] = edge_line_style
    return nx_graph
