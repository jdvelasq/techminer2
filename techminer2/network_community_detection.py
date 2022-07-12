"""
Network Community Detection
===============================================================================

Builds a network from a matrix

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> matrix_list = co_occ_matrix_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> from techminer2.co_occ_network import co_occ_network
>>> graph = co_occ_network(matrix_list)
>>> from techminer2.community_detection import community_detection
>>> community_detection(graph, method='louvain')


"""
from cdlib import algorithms


def network_community_detection(graph, method):

    """Network community detection."""

    algorithm = {
        "label_propagation": algorithms.label_propagation,
        "leiden": algorithms.leiden,
        "louvain": algorithms.louvain,
        "walktrap": algorithms.walktrap,
    }[method]

    communities = algorithm(graph, randomize=False).communities

    for i_community, community in enumerate(communities):
        for node in community:
            graph.nodes[node]["group"] = i_community

    return graph
