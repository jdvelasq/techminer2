import networkx as nx  # type: ignore

from tm2p._intern import Params


def keep_top_n_edges(params: Params, nx_graph: nx.Graph) -> nx.Graph:

    edges = nx_graph.edges(data=True)
    edges = sorted(edges, key=lambda edge: edge[2].get("weight", 1.0), reverse=True)
    edges_to_keep = edges[: params.global_top_edges]

    pruned_graph = nx_graph.__class__()
    pruned_graph.add_nodes_from(nx_graph.nodes(data=True))

    for u, v, _ in edges_to_keep:
        pruned_graph.add_edge(u, v, **nx_graph[u][v])

    return pruned_graph
