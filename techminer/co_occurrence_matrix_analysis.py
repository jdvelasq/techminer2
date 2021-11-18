"""
Co-occurrence matrix analysis
===============================================================================

This module contains functions to find and map relationships concerning items
co-occurrences.

The method is based on T-LAB concept mapping analysis of the co-occurrence
matrix.

The algorithm is described as follows:

1. Compute the co-occurrence matrix.

2. Apply a cluster analysis to the co-occurrence matrix.

3. Apply a manifold technique to visualize the elements of the cluster. Here
   the manifold is restricted to 2D space (`n_components=2`).



>>> from techminer import *
>>> from sklearn.cluster import KMeans
>>> from sklearn.manifold import MDS
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> coc_matrix = co_occurrence_matrix(directory, 'author_keywords', min_occ=15)
>>> concept_mapping(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), clustering_method=KMeans(n_clusters=6), manifold_method=MDS()).silhouette_scores_plot()

.. image:: images/manifold_factorial_analysis_silhouette.png
    :width: 500px
    :align: center

>>> concept_mapping(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), clustering_method=KMeans(n_clusters=6), manifold_method=MDS()).words_by_cluster().head()
                                    Dim-0       Dim-1  Cluster
author_keywords      #d  #c                                   
fintech              882 5181  692.348302  486.687722        2
blockchain           131 1031   28.441931  131.348961        1
financial inclusion  72  742    55.044629  -11.972299        4
financial technology 72  372    34.559715  -62.101282        3
crowdfunding         50  492   -32.731821   33.764264        0

>>> concept_mapping(coc_matrix, manifold_method=MDS(), clustering_method=KMeans(n_clusters=4)).map()

.. image:: images/concept_mapping_map.png
    :width: 800px
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

        self.edges_["group"] = [
            nodes.loc[source, "group"]
            if node_sizes[source] > node_sizes[target]
            else nodes.loc[target, "group"]
            for source, target in zip(self.edges_.source, self.edges_.target)
        ]
        #
        #
        self.make_manifold_data()

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
