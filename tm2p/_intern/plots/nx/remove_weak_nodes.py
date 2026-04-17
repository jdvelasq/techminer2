import networkx as nx  # type: ignore

from tm2p._intern import Params


def remove_weak_nodes(params: Params, nx_graph: nx.Graph) -> nx.Graph:

    nodes_to_remove = [
        node
        for node, degree in dict(nx_graph.degree()).items()
        if degree < params.min_node_degree
    ]
    nx_graph.remove_nodes_from(nodes_to_remove)

    return nx_graph
