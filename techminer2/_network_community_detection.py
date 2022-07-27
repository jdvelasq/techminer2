"""
Network Community Detection
===============================================================================




>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__co_occ_matrix_list
>>> from techminer2._matrix_list_2_network_graph import matrix_list_2_network_graph
>>> from techminer2._get_network_graph_indicators import get_network_graph_indicators
>>> from techminer2._network_community_detection import network_community_detection

>>> matrix_list = vantagepoint__co_occ_matrix_list(
...    criterion='author_keywords',
...    topics_length=3,
...    directory=directory,
... )

>>> graph = matrix_list_2_network_graph(matrix_list) 
>>> graph = network_community_detection(graph, method='louvain') # doctest: +ELLIPSIS
>>> graph
<networkx.classes.graph.Graph ...

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
