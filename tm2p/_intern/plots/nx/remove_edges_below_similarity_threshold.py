import networkx as nx  # type: ignore

from tm2p._intern import Params


def remove_edges_below_similarity_threshold(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    edges_to_remove = []
    for edge in nx_graph.edges():
        weight = nx_graph.edges[edge]["weight"]
        if weight < params.edge_similarity_threshold:
            edges_to_remove.append(edge)

    nx_graph.remove_edges_from(edges_to_remove)

    return nx_graph
