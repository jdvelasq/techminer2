"""
Similarity matrix --- from clusters
===============================================================================
"""
import pandas as pd


def build_similarity_matrix_from_clusters(
    similarity_matrix,
    clusters,
):
    similarity_matrix = similarity_matrix.copy()
    clusters = clusters.copy()
    clusters = "CLUST " + clusters.map(str)

    similarity_matrix = pd.concat([similarity_matrix, clusters], axis=1)
    cluster_similarity = similarity_matrix.groupby("cluster").sum()
    cluster_similarity = cluster_similarity.transpose()
    cluster_similarity = pd.concat([cluster_similarity, clusters], axis=1)
    cluster_similarity = cluster_similarity.groupby("cluster").sum()

    return cluster_similarity
