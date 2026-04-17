import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_edge_color_by_group(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    for edge in nx_graph.edges():

        color_0 = nx_graph.nodes[edge[0]]["node_color"]
        color_1 = nx_graph.nodes[edge[1]]["node_color"]

        if color_0 == color_1:
            nx_graph.edges[edge]["color"] = color_0
        else:
            nx_graph.edges[edge]["color"] = params.edge_color_uniform

    return nx_graph
