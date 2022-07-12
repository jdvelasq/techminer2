"""
Network Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> matrix_list = co_occ_matrix_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> from techminer2.co_occ_network import co_occ_network
>>> graph = co_occ_network(matrix_list)
>>> from techminer2.network_community_detection import network_community_detection
>>> graph = network_community_detection(graph, method='louvain')

>>> from techminer2.network_indicators import network_indicators
>>> network_indicators(graph).head()
                                group  betweenness  closeness  pagerank
regtech 70:462                      0     0.562500   0.875000  0.293120
fintech 42:406                      0     0.151210   0.662162  0.192005
blockchain 18:109                   0     0.002016   0.471154  0.057606
artificial intelligence 13:065      1     0.000000   0.462264  0.035665
compliance 12:020                   0     0.000000   0.462264  0.030006


"""
import networkx as nx
import pandas as pd


def network_indicators(graph):
    """Network indicators"""

    nodes = [node for node in graph.nodes()]
    group = [data["group"] for _, data in graph.nodes(data=True)]
    betweenness = nx.betweenness_centrality(graph)
    closeness = nx.closeness_centrality(graph)
    pagerank = nx.pagerank(graph)

    indicators = pd.DataFrame(
        {
            "group": group,
            "betweenness": betweenness,
            "closeness": closeness,
            "pagerank": pagerank,
        },
        index=nodes,
    )

    return indicators
