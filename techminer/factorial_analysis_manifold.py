"""
Factorial analysis (manifold)
===============================================================================


Factorial analysis based on the clustering applyed to the dimensionality reduction 
of the co-occurrence matrix.

Based on the bibliometrix/R/conceptualStructure.R code.


**Algorithm**

1. Compute the co-occurrence matrix
2. Apply the dimensionality reduction (sklearn mainfold learning algorithms).
3. Apply the clustering algorithm (sklearn clustering algorithms).
4. Visualize the results.

>>> from techminer import *
>>> from sklearn.cluster import KMeans
>>> from sklearn.manifold import MDS
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> coc_matrix = co_occurrence_matrix(directory, 'author_keywords', min_occ=15)
>>> mainfold_factorial_analysis(coc_matrix, manifold_method=MDS(), clustering_method=KMeans(n_clusters=4)).silhouette_scores_plot()

.. image:: images/manifold_factorial_analysis_silhouette.png
    :width: 400px
    :align: center


>>> mainfold_factorial_analysis(coc_matrix, manifold_method=MDS(), clustering_method=KMeans(n_clusters=4)).words_by_cluster().head()
                                    Dim-1       Dim-2  Cluster
author_keywords      #d  #c                                   
fintech              882 5181 -746.525234  398.589319        1
blockchain           131 1031  -39.415114  129.117394        3
financial inclusion  72  742   -54.229554  -24.433846        0
financial technology 72  372    59.166004   47.983897        2
crowdfunding         50  492    -9.401640   19.159085        0

>>> mainfold_factorial_analysis(coc_matrix, manifold_method=MDS(), clustering_method=KMeans(n_clusters=4)).map()

.. image:: images/manifold_factor_analysis_map.png
    :width: 800px
    :align: center

"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

from .plots import conceptual_structure_map


class Factorial_analysis_manifold:
    def __init__(self, matrix, manifold_method, clustering_method):
        self.matrix = matrix
        self.manifold_method = manifold_method
        self.clustering_method = clustering_method
        self.words_by_cluster_ = None
        self.run()

    def run(self):

        matrix = self.matrix.copy()
        matrix = self.manifold_method.fit_transform(matrix)
        self.clustering_method.fit(matrix)

        words_by_cluster = pd.DataFrame(
            matrix, columns=["Dim-1", "Dim-2"], index=self.matrix.index
        )
        words_by_cluster["Cluster"] = self.clustering_method.labels_

        self.words_by_cluster_ = words_by_cluster

    def words_by_cluster(self):
        return self.words_by_cluster_.copy()

    def silhouette_scores_plot(self, max_n_clusters=8, figsize=(5, 5)):

        matrix = self.matrix.copy()
        matrix = self.manifold_method.fit_transform(matrix)

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
        top_n=5,
        figsize=(7, 7),
    ):

        return conceptual_structure_map(
            words_by_cluster=self.words_by_cluster_,
            top_n=top_n,
            figsize=figsize,
        )


def factorial_analysis_manifold(matrix, manifold_method, clustering_method):
    """
    Mainfold Factor Analysis
    """
    return Factorial_analysis_manifold(matrix, manifold_method, clustering_method)
