"""
Concept mapping
===============================================================================

This module contains functions to find and map relationships concerning word
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
import pandas as pd
from sklearn.metrics import silhouette_score

from techminer.plots.bubble_map import bubble_map


class Concept_mapping:
    def __init__(self, matrix, clustering_method, manifold_method):
        self.matrix = matrix
        self.clustering_method = clustering_method
        self.manifold_method = manifold_method
        self.words_by_cluster_ = None
        self.run()

    def run(self):

        # matrix is the co-occurrence matrix
        matrix = self.matrix.copy()

        # Apply a cluster analysis to the co-occurrence matrix.
        self.clustering_method.fit(matrix)

        # Apply a manifold technique to visualize the elements of the cluster.
        transformed_matrix = self.manifold_method.fit_transform(matrix)

        # DataFrame with the coordinates of the keywords
        words_by_cluster = pd.DataFrame(
            transformed_matrix, columns=["Dim-0", "Dim-1"], index=self.matrix.index
        )
        words_by_cluster["Cluster"] = self.clustering_method.labels_

        self.words_by_cluster_ = words_by_cluster

    def words_by_cluster(self):
        return self.words_by_cluster_.copy()

    def silhouette_scores_plot(self, max_n_clusters=8, figsize=(5, 5)):

        matrix = self.matrix.copy()

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

    def map(
        self,
        color_scheme="clusters",
        figsize=(7, 7),
        fontsize=7,
    ):
        return bubble_map(
            node_x=self.words_by_cluster_["Dim-0"],
            node_y=self.words_by_cluster_["Dim-1"],
            node_clusters=self.words_by_cluster_["Cluster"],
            node_texts=self.words_by_cluster_.index.get_level_values(0),
            node_sizes=self.words_by_cluster_.index.get_level_values(1),
            x_axis_at=0,
            y_axis_at=0,
            color_scheme=color_scheme,
            xlabel="X-Axis",
            ylabel="Y-Axis",
            figsize=figsize,
            fontsize=fontsize,
        )


def concept_mapping(matrix, clustering_method, manifold_method):
    return Concept_mapping(
        matrix=matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )
