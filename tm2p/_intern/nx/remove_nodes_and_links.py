import networkx as nx  # type: ignore


def remove_nodes_and_links(params, nx_graph):

    nodes_to_remove = list(nx.isolates(nx_graph))
    nodes_to_remove += [
        node
        for node, degree in dict(nx_graph.degree()).items()
        if degree < params.min_edges_per_node
    ]
    nx_graph.remove_nodes_from(nodes_to_remove)

    edges_to_keep = set()

    for node in nx_graph.nodes():
        incident_edges = sorted(
            nx_graph.edges(node, data=True),
            key=lambda edge: edge[2].get("weight", 1.0),
            reverse=True,
        )
        for u, v, _ in incident_edges[: params.top_edges_per_node]:
            edges_to_keep.add(tuple(sorted((u, v))))

    pruned_graph = nx_graph.__class__()
    pruned_graph.add_nodes_from(nx_graph.nodes(data=True))

    for u, v in edges_to_keep:
        pruned_graph.add_edge(u, v, **nx_graph[u][v])

    return pruned_graph
