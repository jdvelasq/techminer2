"""
Factorial Analysis
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
>>> directory = "data/regtech/"

>>> fa = factorial_analysis_with_mds(
...     'author_keywords', 
...     min_occ=2, 
...     n_clusters=4, 
...     directory=directory,
... )


>>> fa.table_.head()
                                    Dim-1      Dim-2  CLUSTER
row                                                          
regtech 70:462                 -80.333342   6.284539        3
fintech 42:406                 -55.335972 -13.305144        1
blockchain 18:109              -22.741891  -2.324244        0
artificial intelligence 13:065  -8.019514 -11.869961        0
compliance 12:020               -8.445413  10.321464        2

>>> fa.cluster_members_.head()
                                      CL_00  ...           CL_03
0                         blockchain 18:109  ...  regtech 70:462
1            artificial intelligence 13:065  ...                
2  regulatory technologies (regtech) 12:047  ...                
3             financial technologies 09:032  ...                
4               financial regulation 08:091  ...                
<BLANKLINE>
[5 rows x 4 columns]



"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS
from sklearn.metrics import silhouette_score

from .vp.analyze.matrix.co_occ_matrix import co_occ_matrix

# from .conceptual_structure_map import conceptual_structure_map


class _FactorialAnalysis:
    """Generic class to realize Factorial Analysis"""

    def __init__(
        self,
        matrix,
        manifold_method,
        clustering_method,
    ):
        self.matrix = matrix
        self.manifold_method = manifold_method
        self.clustering_method = clustering_method
        self._table = None
        self._cluster_members = None
        self.run()

    def run(self):
        """Run the analysis"""

        matrix = self.matrix.copy()
        matrix = self.manifold_method.fit_transform(matrix)
        self.clustering_method.fit(matrix)

        table = pd.DataFrame(
            matrix,
            columns=["Dim-1", "Dim-2"],
            index=self.matrix.index,
        )
        table["CLUSTER"] = self.clustering_method.labels_
        self._table = table

        cluster_members = pd.DataFrame(
            {
                "CLUSTER": self._table["CLUSTER"],
                "ITEM": self._table.index,
            }
        )

        cluster_members["CLUSTER"] = cluster_members["CLUSTER"].map(
            lambda x: "CL_{:>02d}".format(x)
        )

        cluster_members = cluster_members.groupby("CLUSTER", as_index=False).agg(
            {"ITEM": list}
        )

        members = {
            cluster: item
            for cluster, item in zip(cluster_members.CLUSTER, cluster_members.ITEM)
        }

        for cluster in members:
            members[cluster] = [
                y.split()[-1] + " " + " ".join(y.split()[:-1]) for y in members[cluster]
            ]
            members[cluster] = sorted(members[cluster], reverse=True)
            members[cluster] = [
                " ".join(y.split()[1:]) + " " + y.split()[0] for y in members[cluster]
            ]

        cluster_members = pd.DataFrame.from_dict(members, orient="index").T
        cluster_members = cluster_members.fillna("")

        self._cluster_members = cluster_members

    @property
    def cluster_members_(self):
        return self._cluster_members.copy()

    @property
    def table_(self):
        return self._table.copy()

    def _silhouette_scores_plot(self, max_n_clusters=8, figsize=(7, 7)):

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
        pass

        # return conceptual_structure_map(
        #     words_by_cluster=self._table,
        #     top_n=top_n,
        #     figsize=figsize,
        # )


class _Result:
    def __init__(self):
        self.table_ = None
        self.cluster_members_ = None


def factorial_analysis_with_mds(
    column,
    top_n=50,
    min_occ=2,
    max_occ=None,
    n_clusters=2,
    random_state=0,
    directory="./",
):
    coc_matrix = co_occ_matrix(
        column,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database="documents",
    )

    manifold_method = MDS(
        n_components=2,
        random_state=random_state,
    )
    clustering_method = AgglomerativeClustering(
        n_clusters=n_clusters,
    )

    estimator = _FactorialAnalysis(
        matrix=coc_matrix,
        manifold_method=manifold_method,
        clustering_method=clustering_method,
    )

    result = _Result()
    result.table_ = estimator.table_
    result.cluster_members_ = estimator.cluster_members_

    return result
