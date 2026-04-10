import networkx as nx  # type: ignore

from tm2p._intern import Params


def style_edges_by_weight_bins(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    def get_properties(weight: float):
        if weight < 0.25:
            return params.edge_widths[0], "dot", params.edge_colors[0]
        if weight < 0.5:
            return params.edge_widths[1], "dash", params.edge_colors[1]
        if weight < 0.75:
            return params.edge_widths[2], "solid", params.edge_colors[2]
        return params.edge_widths[3], "solid", params.edge_colors[3]

    for edge in nx_graph.edges():

        weight = nx_graph.edges[edge]["weight"]

        edge_width, edge_dash, edge_color = get_properties(weight)

        nx_graph.edges[edge]["width"] = edge_width
        nx_graph.edges[edge]["dash"] = edge_dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
