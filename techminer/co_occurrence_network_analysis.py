"""
Co-occurrence network analysis
===============================================================================

TODO: pagerank

This module is eqivalent to Bibliometrix' Conceptual Structure/Co-occurrence Network.
The following capabilities are available:

1. Clustering the co-occurrence matrix using sklearn algorithms.

2. Plots the network of co-occurrence relationships, using the clusters found.

3. Build a pandas.DataFrame with the cluster members.

4. Compute and visualize the centrality-density map.

5. Apply a manifold technique to visualize the elements of the cluster. Here
   the manifold is restricted to 2D space (`n_components=2`).


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> mds = MDS(random_state=12345)
>>> analyzer = co_occurrence_network_analysis(
...     coc_matrix, 
...     clustering_method='louvain', 
...     manifold_method=mds,
... )

>>> analyzer.communities()
cluster                      CLUST_0                            CLUST_1  \
rn                                                                        
0                      bank 065:0363       financial inclusion 072:0742   
1                innovation 049:0543      peer-to-peer lending 054:0378   
2         financial service 038:0355      financial innovation 028:0067   
3                   digital 035:0284           digital economy 021:0079   
4                regulation 032:0117           digital finance 019:0362   
5                   finance 028:0200       financial stability 018:0197   
6              technologies 026:0195        regulatory sandbox 017:0064   
7            business model 017:0343              mobile money 017:0065   
8                 insurtech 015:0063     financial institution 016:0376   
9                      risk 014:0063    digital transformation 014:0055   
10                investing 014:0042        financial literacy 013:0024   
11       fintech innovation 013:0054         bank digitization 012:0067   
12             credit score 012:0065  financial intermediation 009:0073   
13              competition 011:0040      digital technologies 009:0164   
14          commercial bank 011:0044                                      
15                financial 009:0034                                      
.
cluster                                   CLUST_2  \
rn                                                  
0                             blockchain 152:1087   
1                       cryptocurrencies 062:0576   
2                           crowdfunding 050:0492   
3                                bitcoin 039:0236   
4                         smart-contract 025:0063   
5                  initial coin offering 020:0244   
6                entrepreneurial finance 013:0080   
7                        venture capital 011:0054   
8                                    ico 010:0055   
9                               ethereum 010:0024   
10       distributed ledger technologies 010:0030   
11                        sustainability 009:0059   
.
cluster                               CLUST_3  \
rn                                              
0        small and medium enterprise 026:0088   
1                            startup 015:0107   
2                   entrepreneurship 014:0141   
3                            payment 013:0038   
4                       case-studies 011:0183   
5                    emerging market 010:0037   
6                            lending 009:0141   
7                          ecosystem 009:0054   
8              disruptive innovation 009:0251   
9                           platform 008:0038   
.
cluster                               CLUST_4  \
rn                                              
0        technology acceptance model 021:0163   
1                     mobile payment 015:0128   
2                           covid-19 015:0054   
3                    islamic finance 012:0044   
4                              trust 011:0039   
5                         e-commerce 011:0051   
6                       islamic bank 010:0015   
7                    digital payment 010:0004   
8                technology adoption 009:0078   
.
cluster                           CLUST_5                           CLUST_6  \
rn                                                                            
0        artificial intelligence 052:0248               securities 016:0072   
1               machine-learning 040:0138  internet of thing (iot) 015:0050   
2                        regtech 037:0241                                     
3                       big data 030:0163                                     
4           financial regulation 023:0105                                     
5                   robo-advisor 021:0124                                     
6                  deep learning 015:0116                                     
.
cluster                CLUST_7  
rn                              
0        open banking 011:0019  
1                psd2 009:0018  


>>> analyzer.network()

.. image:: images/co_occurrence_network_analysis_network_map.png
    :width: 500px
    :align: center

>>> analyzer.manifold_map()

.. image:: images/co_occurrence_network_analysis_manifold_map.png
    :width: 500px
    :align: center

>>> analyzer.centrality_density_table()
         num_documents     density  centrality  \
cluster                                          
0                  389  135.045214   16.489890   
1                  330   97.972208   13.820855   
2                  411  394.048639   16.904207   
3                  114   40.110269    6.673760   
4                  113   51.683455    7.217962   
5                  218   68.421149    7.908047   
6                   31    9.428571    1.442924   
7                   20   50.000000    1.307387   
.
                                         name  
cluster                                        
0                               bank 065:0363  
1                financial inclusion 072:0742  
2                         blockchain 152:1087  
3        technology acceptance model 021:0163  
4        small and medium enterprise 026:0088  
5            artificial intelligence 052:0248  
6                         securities 016:0072  
7                       open banking 011:0019

>>> analyzer.centrality_density_map()

.. image:: images/co_occurrence_network_analysis_cen_den_map.png
    :width: 500px
    :align: center



"""
from techminer.utils.co_occurrence_analysis import Co_occurrence_analysis

from .networkx import network_clustering

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
        self._clustering()
        #
        self.make_manifold_data()
        self._compute_centrality_density()

    def _clustering(self):

        self.nodes_, self.edges_ = network_clustering(
            self.nodes_,
            self.edges_,
            self.clustering_method,
        )

        self.labels_ = self.nodes_["group"].copy()


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
