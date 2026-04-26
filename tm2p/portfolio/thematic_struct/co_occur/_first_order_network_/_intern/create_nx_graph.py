import networkx as nx  # type: ignore

from tm2p._intern.nx import add_weighted_edges_from_matrix_list

from ...dir_simil_netw import DirectMatrixList


# -------------------------------------------------------------------------
def _add_nodes_to_nx_graph_from(
    nx_graph,
    cooc_matrix,
):
    matrix = cooc_matrix.copy()
    nodes = matrix.columns.tolist()
    nx_graph.add_nodes_from(nodes, group=0)

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["labeled"] = True
        nx_graph.nodes[node]["text"] = node

    return nx_graph


# -------------------------------------------------------------------------
def _add_weighted_edges_to_nx_graph_from(
    nx_graph,
    cooc_matrix,
):
    matrix = cooc_matrix.copy()

    for i_row, row in enumerate(cooc_matrix.index.tolist()):
        for i_col, col in enumerate(cooc_matrix.columns.tolist()):

            if i_col <= i_row:
                continue

            weight = matrix.loc[row, col]
            if weight > 0:
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                    dash="solid",
                )

    return nx_graph


def create_nx_graph(params):

    nx_graph = nx.Graph()

    matrix_list = (
        DirectMatrixList().update(**params.__dict__).update(counters=True).run()
    )
    nx_graph = add_weighted_edges_from_matrix_list(nx_graph, matrix_list)

    return nx_graph
