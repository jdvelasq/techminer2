"""
Factorial Analysis (manifold)
===============================================================================


Factorial analysis based on the clustering applyed to the dimensionality reduction 
of the co-occurrence matrix.

Based on the bibliometrix/R/conceptualStructure.R code.


**Algorithm**

1. Compute the co-occurrence matrix
2. Apply the dimensionality reduction (sklearn mainfold learning algorithms).
3. Apply the clustering algorithm (sklearn clustering algorithms).
4. Visualize the results.

>>> from techminer2 import *
>>> from sklearn.cluster import KMeans
>>> from sklearn.manifold import MDS
>>> directory = "/workspaces/techminer2/data/"
>>> coc_matrix = co_occurrence_matrix('author_keywords', min_occ=4, directory=directory)
>>> file_name = "/workspaces/techminer2/sphinx/images/factorial_analysis_manifold_silhouette.png"
>>> factorial_analyzer = Factorial_analysis_manifold(
...     coc_matrix, 
...     manifold_method=MDS(random_state=0), 
...     clustering_method=KMeans(n_clusters=4, random_state=0)
... )
>>> factorial_analyzer.silhouette_scores_plot(max_n_clusters=8).savefig(file_name)

.. image:: images/manifold_factorial_analysis_silhouette.png
    :width: 700px
    :align: center


>>> factorial_analyzer.data().head()
                                     Dim-1       Dim-2  Cluster
author_keywords        #d  #c                                  
fintech                139 1285  20.418893  133.715387        1
financial technologies 28  225   23.598669   12.903288        3
financial inclusion    17  339  -14.816283   10.690490        2
block-chain            17  149   -5.769834   15.363572        2
innovating             13  249   13.479658   -3.236222        3


>>> factorial_analyzer.cluster_members().head()
                           CLTR_0  ...                           CLTR_3
rn                                 ...                                 
0           crowdfunding 008:0116  ...  financial technologies 028:0225
1   peer-to-peer lending 008:0073  ...              innovating 013:0249
2               covid-19 008:0036  ...                    bank 012:0185
3             technology 007:0192  ...                                 
4               start-up 007:0141  ...                                 
<BLANKLINE>
[5 rows x 4 columns]



>>> file_name = "/workspaces/techminer2/sphinx/images/factorial_analysis_manifold_map.png"
>>> factorial_analyzer.map().savefig(file_name)

.. image:: images/factorial_analysis_manifold_map.png
    :width: 7000px
    :align: center

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score

from .conceptual_structure_map import conceptual_structure_map


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

        names = self.table_.index.get_level_values(0)
        num_docs = self.table_.index.get_level_values(1)
        cited_by = self.table_.index.get_level_values(2)

        n_zeros_docs = int(np.log10(max(num_docs))) + 1
        n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

        fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
        text = [
            fmt.format(name, int(nd), int(tc))
            for name, nd, tc in zip(names, num_docs, cited_by)
        ]

        cluster_members = self.table_.copy()
        #
        cluster_members["num_documents"] = num_docs
        cluster_members["cited_by"] = cited_by
        cluster_members["item"] = text
        cluster_members.pop("Dim-1")
        cluster_members.pop("Dim-2")
        #
        cluster_members = cluster_members.sort_values(
            by=["Cluster", "num_documents", "cited_by"], ascending=[True, True, True]
        )

        cluster_members = cluster_members.assign(
            rn=cluster_members.groupby("Cluster").cumcount(())
        )
        cluster_members = cluster_members.pivot(
            index="rn", columns="Cluster", values="item"
        )
        cluster_members = cluster_members.fillna("")
        cluster_members.columns = [
            "CL_{:02d}".format(i) for i in cluster_members.columns
        ]
        self.cluster_members_ = cluster_members

    def cluster_members(self):
        return self.cluster_members_.copy()

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
