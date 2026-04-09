import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_node_color_by_group(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    for node in nx_graph.nodes():
        group = nx_graph.nodes[node]["group"]
        nx_graph.nodes[node]["node_color"] = params.node_colors[group]
    return nx_graph
