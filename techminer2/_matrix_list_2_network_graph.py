"""
Matrix List ---> Networkx Graph
===============================================================================

Builds a network from a matrix


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__co_occ_matrix_list
>>> matrix_list = vantagepoint__co_occ_matrix_list(
...    criterion='author_keywords',
...    topics_length=3,
...    directory=directory,
... )

>>> from techminer2._matrix_list_2_network_graph import matrix_list_2_network_graph
>>> matrix_list_2_network_graph(matrix_list) # doctest: +ELLIPSIS
<networkx.classes.graph.Graph ...

"""
import networkx as nx


def matrix_list_2_network_graph(
    matrix_list,
):
    """Transforms a co-occurrence matrix list into a networkx graph."""

    graph = nx.Graph()
    graph = _create_nodes(graph, matrix_list)
    graph = _create_edges(graph, matrix_list)
    return graph


def _create_edges(graph, matrix_list):
    edges = []
    for _, row in matrix_list.iterrows():
        if row["row"] != row["column"]:
            edges.append((row[0], row[1], row[2]))
    graph.add_weighted_edges_from(edges)
    return graph


def _create_nodes(graph, matrix_list):
    matrix_list = matrix_list.copy()
    matrix_list = matrix_list[matrix_list["row"] == matrix_list["column"]]
    nodes = [
        (node, dict(size=occ, group=0))
        for node, occ in zip(matrix_list["row"], matrix_list["OCC"])
    ]
    graph.add_nodes_from(nodes)
    return graph
