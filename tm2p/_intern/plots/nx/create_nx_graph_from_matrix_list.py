import networkx as nx  # type: ignore


def create_nx_graph_from_matrix_list(
    matrix_list,
    source,
    target,
    weight,
):

    nx_graph = nx.from_pandas_edgelist(
        matrix_list,
        source=source,
        target=target,
        edge_attr=weight,
    )
    nx_graph.remove_edges_from(nx.selfloop_edges(nx_graph))

    return nx_graph
