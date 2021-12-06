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
>>> directory = "/workspaces/techminer-api/data/"
>>> coc_matrix = co_occurrence_matrix('author_keywords', min_occ=4, directory=directory)
>>> file_name = "/workspaces/techminer-api/sphinx/images/factorial_analysis_manifold_silhouette.png"
>>> factorial_analyzer = Factorial_analysis_manifold(
...     coc_matrix, 
...     manifold_method=MDS(random_state=0), 
...     clustering_method=KMeans(n_clusters=4, random_state=0)
... )
>>> factorial_analyzer.silhouette_scores_plot(max_n_clusters=8).savefig(file_name)

.. image:: images/manifold_factorial_analysis_silhouette.png
    :width: 5500px
    :align: center


>>> factorial_analyzer.items_by_cluster().head()
                                     Dim-1       Dim-2  Cluster
author_keywords        #d  #c                                  
fintech                139 1285  21.789293  133.502844        1
financial technologies 28  225   23.214658   13.359314        3
financial inclusion    17  339  -14.080205   11.401536        2
blockchain             17  149   -4.997082   15.544741        2
innovation             13  249   13.538624   -4.960027        3

>>> file_name = "/workspaces/techminer-api/sphinx/images/factorial_analysis_manifold_map.png"
>>> factorial_analyzer.map().savefig(file_name)

.. image:: images/factorial_analysis_manifold_map.png
    :width: 5500px
    :align: center

"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

from .plots import conceptual_structure_map


class Factorial_analysis_manifold:
    def __init__(
        self,
        matrix,
        manifold_method,
        clustering_method,
    ):
        self.matrix = matrix
        self.manifold_method = manifold_method
        self.clustering_method = clustering_method
        self.table_ = None
        self.run()

    def run(self):

        matrix = self.matrix.copy()
        matrix = self.manifold_method.fit_transform(matrix)
        self.clustering_method.fit(matrix)

        table = pd.DataFrame(
            matrix, columns=["Dim-1", "Dim-2"], index=self.matrix.index
        )
        table["Cluster"] = self.clustering_method.labels_

        self.table_ = table

    def data(self):
        return self.table_.copy()

    def silhouette_scores_plot(self, max_n_clusters=8, figsize=(7, 7)):

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
        ax.set_xlabel("Number of clusters", fontsize=7)
        ax.set_ylabel("Silhouette score", fontsize=7)
        ax.grid(True, linestyle=":", alpha=0.5)

        return fig

    def map(
        self,
        top_n=5,
        figsize=(7, 7),
    ):

        return conceptual_structure_map(
            words_by_cluster=self.table_,
            top_n=top_n,
            figsize=figsize,
        )
