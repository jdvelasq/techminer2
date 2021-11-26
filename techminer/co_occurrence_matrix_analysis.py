"""
Co-occurrence matrix analysis
===============================================================================

This module contains functions to find and map relationships concerning items
co-occurrences. 

For keywords-related columns, this module allows to plot relationships between
keywords, and to find the most relevant clusters. The method is based on T-LAB 
concept mapping analysis of the co-occurrence matrix.

The following capabilities are available:

1. Clustering the co-occurrence matrix using sklearn algorithms.

2. Plots the network of co-occurrence relationships, using the clusters found.

3. Build a pandas.DataFrame with the cluster members.

4. Compute and visualize the centrality-density map.

5. Apply a manifold technique to visualize the elements of the cluster. Here
   the manifold is restricted to 2D space (`n_components=2`).


>>> from techminer import *
>>> from sklearn.cluster import KMeans
>>> from sklearn.manifold import MDS
>>> directory = "/workspaces/techminer-api/data/"
>>> coc_matrix = co_occurrence_matrix(
...     directory, 
...     'author_keywords', 
...     min_occ=15, 
...     association="equivalence",
... )
>>> kmeans=KMeans(n_clusters=5, random_state=1234)
>>> mds = MDS(random_state=12345)
>>> analyzer = co_occurrence_matrix_analysis(
...     coc_matrix, 
...     clustering_method=kmeans, 
...     manifold_method=mds
... )


>>> analyzer.communities()
cluster                                   CLUST_0  \
rn                                                  
0                   peer-to-peer lending 054:0378   
1                           crowdfunding 050:0492   
2                                regtech 037:0241   
3                               big data 030:0163   
4                   financial innovation 028:0067   
5            small and medium enterprise 026:0088   
6            technology acceptance model 021:0163   
7                  initial coin offering 020:0244   
8                        digital finance 019:0362   
9                     regulatory sandbox 017:0064   
10                      entrepreneurship 014:0141   
11               entrepreneurial finance 013:0080   
12                          credit score 012:0065   
13                       venture capital 011:0054   
14                       commercial bank 011:0044   
15                                   ico 010:0055   
16       distributed ledger technologies 010:0030   
17                        sustainability 009:0059   
18                               lending 009:0141   
19              financial intermediation 009:0073   
.
cluster                          CLUST_1                CLUST_2  \
rn                                                                
0                       digital 035:0284  open banking 011:0019   
1                smart-contract 025:0063          psd2 009:0018   
2               digital economy 021:0079                          
3                mobile payment 015:0128                          
4        digital transformation 014:0055                          
5                         trust 011:0039                          
6                    e-commerce 011:0051                          
7               digital payment 010:0004                          
8         disruptive innovation 009:0251                          
.
cluster                           CLUST_3                    CLUST_4  
rn                                                                    
0            financial inclusion 072:0742        blockchain 152:1087  
1                           bank 065:0363  cryptocurrencies 062:0576  
2        artificial intelligence 052:0248           bitcoin 039:0236  
3                     innovation 049:0543          ethereum 010:0024  
4               machine-learning 040:0138                             
5              financial service 038:0355                             
6                     regulation 032:0117                             
7                        finance 028:0200                             
8                   technologies 026:0195                             
9           financial regulation 023:0105                             
10                  robo-advisor 021:0124                             
11           financial stability 018:0197                             
12                  mobile money 017:0065                             
13                business model 017:0343                             
14                    securities 016:0072                             
15         financial institution 016:0376                             
16                       startup 015:0107                             
17       internet of thing (iot) 015:0050                             
18                     insurtech 015:0063                             
19                 deep learning 015:0116                             
20                      covid-19 015:0054                             
21                          risk 014:0063                             
22                     investing 014:0042                             
23                       payment 013:0038                             
24            fintech innovation 013:0054                             
25            financial literacy 013:0024                             
26               islamic finance 012:0044                             
27             bank digitization 012:0067                             
28                   competition 011:0040                             
29                  case-studies 011:0183                             
30                  islamic bank 010:0015                             
31               emerging market 010:0037                             
32           technology adoption 009:0078                             
33                     financial 009:0034                             
34                     ecosystem 009:0054                             
35          digital technologies 009:0164                             
36                      platform 008:0038                             


>>> analyzer.network()

.. image:: images/co_occurrence_matrix_analysis_network.png
    :width: 500px
    :align: center


>>> analyzer.manifold_map()

.. image:: images/co_occurrence_matrix_analysis_manifold_map.png
    :width: 500px
    :align: center

>>> analyzer.centrality_density_table()
         num_documents     density  centrality                           name
cluster                                                                      
0                  410  303.119783   30.617132  peer-to-peer lending 054:0378
1                  151   61.022540   15.789041               digital 035:0284
2                   20   80.000000    1.307387          open banking 011:0019
3                  782  467.019950   28.088034   financial inclusion 072:0742
4                  263  208.839200   19.436812            blockchain 152:1087

>>> analyzer.centrality_density_map()

.. image:: images/co_occurrence_matrix_analysis_cen_den_map.png
    :width: 500px
    :align: center



"""
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

from .utils import Co_occurrence_analysis


class Co_occurrence_matrix_analysis(Co_occurrence_analysis):
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
        self.clustering_method.fit(self.co_occurrence_matrix)
        self.nodes_["group"] = self.clustering_method.labels_
        #
        self.labels_ = self.clustering_method.labels_
        #
        node_sizes = self.nodes_.copy()
        node_sizes = node_sizes.set_index("name")
        node_sizes = node_sizes["size"]
        node_sizes.index = self.nodes_["name"]
        nodes = self.nodes_.copy()
        nodes = nodes.set_index("name")

        communities = dict(zip(self.nodes_.name, self.nodes_.group))
        self.edges_["cluster_source"] = self.edges_.source.map(communities)
        self.edges_["cluster_target"] = self.edges_.target.map(communities)

        self.edges_["group"] = [
            nodes.loc[source, "group"]
            if node_sizes[source] > node_sizes[target]
            else nodes.loc[target, "group"]
            for source, target in zip(self.edges_.source, self.edges_.target)
        ]
        #
        #
        self.make_manifold_data()
        self._compute_centrality_density()

    def silhouette_scores_plot(self, max_n_clusters=8, figsize=(5, 5)):

        matrix = self.co_occurrence_matrix.copy()

        silhouette_scores = []
        n_clusters = []

        for n in range(2, max_n_clusters):
            self.clustering_method.set_params(n_clusters=n)
            self.clustering_method.fit(matrix)
            n_clusters.append(n)
            silhouette_scores.append(
                silhouette_score(matrix, self.clustering_method.labels_)
            )

        fig = plt.figure(figsize=figsize)
        ax = fig.subplots()

        ax.plot(n_clusters, silhouette_scores, "o-k")
        ax.set_xlabel("Number of clusters")
        ax.set_ylabel("Silhouette score")
        ax.grid(True, linestyle="--", alpha=0.5)

        return fig


def co_occurrence_matrix_analysis(
    co_occurrence_matrix, clustering_method, manifold_method
):
    return Co_occurrence_matrix_analysis(
        co_occurrence_matrix=co_occurrence_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )
