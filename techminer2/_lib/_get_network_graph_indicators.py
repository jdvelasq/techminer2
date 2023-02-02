"""
Network Indicators
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
>>> graph = network_community_detection(graph, method='louvain')
>>> get_network_graph_indicators(graph).head()
                   group  betweenness  closeness  pagerank
regtech 69:461         0          0.0        1.0  0.396082
fintech 42:406         0          0.0        1.0  0.376834
blockchain 18:109      0          0.0        1.0  0.227084


"""
import networkx as nx
import pandas as pd


def get_network_graph_indicators(graph):
    """Network indicators"""

    nodes = list(graph.nodes())
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
