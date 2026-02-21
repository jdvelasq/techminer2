def internal__assign_constant_to_edge_colors(
    params,
    nx_graph,
):
    for edge in nx_graph.edges():
        nx_graph.edges[edge]["color"] = params.edge_colors[0]
    return nx_graph
