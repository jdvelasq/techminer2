import networkx as nx  # type: ignore

from tm2p._intern import Params


def keep_top_k_edges_per_node(params: Params, nx_graph: nx.Graph) -> nx.Graph:

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
