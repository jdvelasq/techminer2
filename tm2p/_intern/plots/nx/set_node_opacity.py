import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_node_opacity(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    nx_graph.graph["node_opacity"] = params.node_opacity_uniform  # type: ignore
    return nx_graph
