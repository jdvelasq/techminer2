# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Creates a co-occurrence networkx graph from a co-occurrence matrix.


"""
import networkx as nx

from ...co_occurrence_matrix.compute_co_occurrence_matrix import compute_co_occurrence_matrix
from ...co_occurrence_matrix.normalize_co_occurrence_matrix import normalize_co_occurrence_matrix


def nx_create_co_occurrence_graph(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    association_index="association",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):

    cooc_matrix = compute_co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=rows_and_columns,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if association_index is not None:
        cooc_matrix = normalize_co_occurrence_matrix(cooc_matrix, association_index)

    #
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = _add_nodes_from(nx_graph, cooc_matrix)
    nx_graph = _add_weighted_edges_from(nx_graph, cooc_matrix)

    return nx_graph


def _add_nodes_from(
    nx_graph,
    cooc_matrix,
):
    matrix = cooc_matrix.df_.copy()
    nodes = matrix.columns.tolist()
    nx_graph.add_nodes_from(nodes, group=0)

    for node in nx_graph.nodes():
        # nx_graph.nodes[node]["text"] = node

        #
        # Remove metrics from the name
        nx_graph.nodes[node]["text"] = " ".join(node.split(" ")[:-1])

    return nx_graph


def _add_weighted_edges_from(
    nx_graph,
    cooc_matrix,
):
    matrix = cooc_matrix.df_.copy()

    for i_row, row in enumerate(cooc_matrix.df_.index.tolist()):
        for i_col, col in enumerate(cooc_matrix.df_.columns.tolist()):
            #
            # Unicamente toma valores por encima de la diagonal principal
            if i_col <= i_row:
                continue

            weight = matrix.loc[row, col]
            if weight > 0:
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                    dash="solid",
                )

    return nx_graph
