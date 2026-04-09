import networkx as nx  # type: ignore


def set_top_n_node_labels(
    nx_graph: nx.Graph,
    sorted_nodes: list,
    top_n: int,
) -> nx.Graph:

    for node in nx_graph.nodes():
        if "text" not in nx_graph.nodes[node]:
            nx_graph.nodes[node]["text"] = node
        if "labeled" not in nx_graph.nodes[node]:
            nx_graph.nodes[node]["labeled"] = False

    n_labeled = 0
    for node in sorted_nodes:
        if node in nx_graph.nodes():
            nx_graph.nodes[node]["labeled"] = True
            n_labeled += 1
            if n_labeled >= top_n:
                break

    return nx_graph
