import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_uniform_node_color(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["node_color"] = params.node_color
    return nx_graph
