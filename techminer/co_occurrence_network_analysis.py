"""
Co-occurrence network analysis
===============================================================================

TODO: pagerank

This module is eqivalent to:

* Bibliometrix' Conceptual Structure/Co-occurrence Network.
    - Network map
    - Table with (node, cluster, betweenness, closeness, pagerank)
    - Degree plot

* VantagePoint Co-occurrence map (newtork without clustering).

* T-LAB Co-occurrence analysis

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').plot()

.. image:: images/co_occurrence_network.png
    :width: 700px
    :align: center


>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').communities()
cluster                  CLUST_0                        CLUST_1  \\
rn                                                                
0               fintech 882:5181  financial technology 072:0372   
1            blockchain 131:1031   financial inclusion 072:0742   
2          crowdfunding 050:0492                 china 028:0115   
3            innovation 044:0527  financial innovation 024:0058   
4        cryptocurrency 039:0267  financial regulation 021:0103   
.
cluster                                  CLUST_2  
rn                                                
0               artificial intelligence 048:0238  
1                      machine learning 039:0135  
2                               regtech 033:0237  
3                              big data 030:0163  
4        financial technology (fintech) 026:0137

>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').table().head()
                      node  num_documents  global_citations  cluster  \\
0  artificial intelligence             48               238        2   
1                  banking             38               258        0   
2                    banks             16                96        0   
3                 big data             30               163        2   
4                  bitcoin             39               236        0   
-
   betweenness  closeness  
0     0.020965   0.744186  
1     0.020708   0.744186  
2     0.002279   0.603774  
3     0.010653   0.695652  
4     0.004572   0.640000


>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').heat_map()

.. image:: images/co_occurrence_heat_map.png
    :width: 700px
    :align: center


>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').node_degrees()

.. image:: images/co_occurrence_degrees.png
    :width: 700px
    :align: center


"""
import numpy as np
import pandas as pd

from techminer.utils.co_occurrence_analysis import Co_occurrence_analysis

from .networkx import (
    betweenness_centrality,
    closeness_centrality,
    network_clustering,
    network_plot,
    node_degrees_plot,
)

cluster_colors = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
    "cornflowerblue",
    "lightsalmon",
    "limegreen",
    "tomato",
    "mediumvioletred",
    "darkgoldenrod",
    "lightcoral",
    "silver",
    "darkkhaki",
    "skyblue",
] * 5


class Co_occurrence_network_analysis(Co_occurrence_analysis):
    def __init__(
        self,
        co_occurrence_matrix,
        clustering_method,
        manifold_method,
    ):
        super().__init__(
            co_occurrence_matrix=co_occurrence_matrix,
            clustering_method=clustering_method,
            manifold_method=manifold_method,
        )

        # ----< algorithm >----------------------------------------------------
        self._sort_co_occurrence_matrix()
        self._make_nodes()
        self._make_edges()
        #
        print(self.nodes_)
        self._clustering()
        #
        self.make_manifold_data()

    def _clustering(self):

        self.nodes_, self.edges_ = network_clustering(
            self.nodes_,
            self.edges_,
            self.clustering_method,
        )

        self.labels_ = self.nodes_["group"]


def co_occurrence_network_analysis(
    co_occurrence_matrix,
    clustering_method,
    manifold_method,
):

    return Co_occurrence_network_analysis(
        co_occurrence_matrix=co_occurrence_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )
