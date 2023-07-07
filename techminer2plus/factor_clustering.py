# flake8: noqa
# pylint: disable=line-too-long
"""
Factor Clustering
===============================================================================

Clusters a factor matrix using sklearn algorithms.

>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> factor_matrix = techminer2plus.factor_decomposition_kernel_pca(
...     cooc_matrix,
... )

>>> factor_clusters = techminer2plus.factor_clustering(
...    factor_matrix,
...    n_clusters=4,
... )
>>> factor_clusters.centers_
      DIM_00    DIM_01    DIM_02    DIM_03
0  -2.980853 -0.390462 -0.713463 -0.503811
1  -0.057956  0.441319  1.944838  1.505084
2  27.114349 -2.511742 -0.067028 -1.633201
3  11.926518  5.381146 -0.382140  0.657317


"""
from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


@dataclass
class FactorClusters:
    """Factor Clusters."""

    #
    # RESULTS:
    labels_: list
    df_: pd.DataFrame
    centers_: pd.DataFrame
    communities_: dict


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_clustering(
    factor_matrix,
    #
    # KMEANS PARAMS:
    n_clusters=8,
    init="k-means++",
    n_init=10,
    max_iter=300,
    tol=0.0001,
    random_state=0,
    algorithm: Literal["lloyd", "elkan", "auto", "full"] = "auto",
):
    """Cluster a factor matrix using a K-means estimators."""

    def build_estimator():
        """Builds a K-means estimator."""
        return KMeans(
            n_clusters=n_clusters,
            init=init,
            n_init=n_init,
            max_iter=max_iter,
            tol=tol,
            random_state=random_state,
            algorithm=algorithm,
        )

    def select_first_n_columns_of_factor_matrix():
        return factor_matrix.df_.iloc[:, :n_clusters]

    def normalize_matrix(matrix):
        """Normalizes a matrix."""
        # divide each row by the max value of the row
        matrix = matrix.copy()
        return matrix.div(matrix.max(axis=1), axis=0)

    def get_communities(items, labels):
        """Creates communities."""

        communities = {i_cluster: [] for i_cluster in range(n_clusters)}
        for item, label in zip(items, labels):
            communities[label].append(item)
        return communities

    def get_sorted_labels(items, labels):
        communities = get_communities(items, labels)
        lengths = [(key, len(communities[key])) for key in communities.keys()]
        lengths = sorted(lengths, key=lambda x: x[1], reverse=True)
        sorted_labels = [index for index, _ in lengths]
        return sorted_labels

    estimator = build_estimator()
    matrix = select_first_n_columns_of_factor_matrix()
    normalized_matrix = normalize_matrix(matrix)
    estimator.fit(normalized_matrix)
    sorted_labels = get_sorted_labels(matrix.index, estimator.labels_)
    new_centers = estimator.cluster_centers_[sorted_labels, :]
    old_2_new = {old: new for new, old in enumerate(sorted_labels)}
    new_labels = [old_2_new[label] for label in estimator.labels_]

    communities = get_communities(matrix.index, new_labels)

    # adds the prefix 'CL_' to the labels
    n_zeros = int(np.log10(n_clusters - 1)) + 1
    fmt = "CL_{:0" + str(n_zeros) + "d}"
    new_labels = [fmt.format(label) for label in new_labels]
    centers = pd.DataFrame(
        new_centers,
        columns=matrix.columns,
        index=[fmt.format(i) for i in range(n_clusters)],
    )

    communities = {
        fmt.format(key): communities[key] for key in communities.keys()
    }

    return FactorClusters(
        labels_=new_labels,
        df_=matrix,
        centers_=centers,
        communities_=communities,
    )
