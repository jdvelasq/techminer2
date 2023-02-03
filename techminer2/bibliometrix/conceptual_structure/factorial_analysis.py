"""
Factorial Analysis
===============================================================================


Factorial analysis based on the clustering applyed to the dimensionality reduction 
of the co-occurrence matrix.

Based on the bibliometrix/R/conceptualStructure.R code.


**Algorithm**

1. Compute the co-occurrence matrix
2. Apply the dimensionality reduction (manifold learning or decomposition algorithms).
3. Apply the clustering algorithm (sklearn clustering algorithms).
4. Visualize the results.


>>> directory = "data/regtech/"

>>> from sklearn.manifold import MDS
>>> mds = MDS(n_components=2, random_state=0)

>>> from sklearn.cluster import AgglomerativeClustering
>>> ac = AgglomerativeClustering(n_clusters=4)

>>> from techminer2 import bibliometrix
>>> fa = bibliometrix.conceptual_structure.factorial_analysis(
...     criterion='author_keywords', 
...     manifold_method=mds,
...     clustering_method=ac,
...     topic_min_occ=2, 
...     directory=directory,
... )



>>> fa.table_.head()
                                  Dim-1     Dim-2  CLUSTER
row                                                       
regtech 28:329                28.268965  3.015757        3
fintech 12:249                13.957324 -1.695197        1
compliance 07:030              4.269020 -6.685674        0
regulatory technology 07:037  -0.346827  6.995581        2
regulation 05:164              4.150326  2.044916        2

>>> fa.cluster_members_.head()
                          CL_00  ...           CL_03
0             compliance 07:030  ...  regtech 28:329
1     financial services 04:168  ...                
2   financial regulation 04:035  ...                
3  anti-money laundering 03:021  ...                
4  semantic technologies 02:041  ...                
<BLANKLINE>
[5 rows x 4 columns]


"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

from ... import vantagepoint


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
            columns=[f"Dim-{i}" for i in range(1, matrix.shape[1] + 1)],
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


class _Result:
    def __init__(self):
        self.table_ = None
        self.cluster_members_ = None


def factorial_analysis(
    criterion,
    manifold_method,
    clustering_method,
    topics_length=50,
    topic_min_occ=2,
    topic_min_citations=None,
    directory="./",
    start_year=None,
    end_year=None,
    **filters,
):
    coc_matrix = vantagepoint.analyze.matrix.co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
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
