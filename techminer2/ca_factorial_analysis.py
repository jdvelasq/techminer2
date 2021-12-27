"""
MCA/CA Factorial Analysis
===============================================================================


Factorial analysis based on the clustering of the TF-IDF matrix

* Based on the bibliometrix/R/conceptualStructure.R code.

* Based on comparative analysis methodology from https://tlab.it/en/allegati/help_en_online/mcluster.htm

**Algorithm**

1. The algorithm receives the TF-IDF matrix.

2. Correspondence analysis for two components (for plotting)

3. Clustring of the ca-matrix.

"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

from .correspondence_analysis import CorrespondenceAnalysis
from .visualization_api.conceptual_structure_map import conceptual_structure_map


class CA_factorial_analysis:
    def __init__(self, tf_idf_matrix, clustering_method):
        self.tf_idf_matrix = tf_idf_matrix
        self.clustering_method = clustering_method
        self.words_by_cluster_ = None
        self.run()

    def run(self):

        tf_idf_matrix = self.tf_idf_matrix.copy()
        correspondence_analysis = CorrespondenceAnalysis()
        correspondence_analysis.fit(tf_idf_matrix)

        ppal_coordinates = correspondence_analysis.principal_coordinates_cols_
        ppal_coordinates = ppal_coordinates[ppal_coordinates.columns[:2]]

        words_by_cluster = pd.DataFrame(
            ppal_coordinates,
            columns=["Dim-1", "Dim-2"],
            index=self.tf_idf_matrix.columns,
        )

        print(words_by_cluster)

        self.clustering_method.fit(words_by_cluster)
        words_by_cluster["Cluster"] = self.clustering_method.labels_
        self.words_by_cluster_ = words_by_cluster

    def words_by_cluster(self):
        return self.words_by_cluster_.copy()

    def silhouette_scores_plot(self, max_n_clusters=8, figsize=(5, 5)):

        tf_idf_matrix = self.tf_idf_matrix.copy()
        correspondence_analysis = CorrespondenceAnalysis()
        correspondence_analysis.fit(tf_idf_matrix)
        ppal_coordinates = correspondence_analysis.principal_coordinates_

        words_by_cluster = pd.DataFrame(
            ppal_coordinates,
            columns=["Dim-1", "Dim-2"],
            index=self.tf_idf_matrix.columns,
        )

        silhouette_scores = []
        n_clusters = []

        for n in range(2, max_n_clusters):
            self.clustering_method.set_params(n_clusters=n)
            self.clustering_method.fit(words_by_cluster)
            n_clusters.append(n)
            silhouette_scores.append(
                silhouette_score(words_by_cluster, self.clustering_method.labels_)
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


def ca_factorial_analysis(matrix, clustering_method):
    """
    CA / Factor Analysis
    """
    return CA_factorial_analysis(matrix, clustering_method)
