import networkx as nx  # type: ignore


def create_nx_graph_from_matrix(matrix):

    nx_graph = nx.from_pandas_adjacency(matrix)
    nx_graph.remove_edges_from(nx.selfloop_edges(nx_graph))

    return nx_graph
