"""
Similarity matrix --- clustering
===============================================================================
"""

import pandas as pd
from sklearn.cluster import KMeans


def similarity_matrix_clustering(
    similarity_matrix,
    cluster_estimator=None,
):

    if cluster_estimator is None:
        cluster_estimator = KMeans(n_clusters=3, random_state=0)

    clusters = cluster_estimator.fit_predict(similarity_matrix)

    cluster_members = pd.Series(
        data=clusters,
        index=similarity_matrix.index,
        name="cluster",
    )

    cluster_members = cluster_members.sort_values(ascending=True)

    return cluster_members
