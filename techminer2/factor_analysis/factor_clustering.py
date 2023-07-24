# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Factor Clustering."""

from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

from ..manifold_2d_map import manifold_2d_map

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


@dataclass
class FactorClusters:
    """Factor Clusters."""

    #
    # RESULTS:
    labels_: list
    centers_: pd.DataFrame
    communities_: pd.DataFrame

    def fig_(
        self,
        dim_x,
        dim_y,
        #
        # MAP:
        node_size_min=20,
        node_size_max=50,
        textfont_size=9,
        textfont_color="#465c6b",
        xaxes_range=None,
        yaxes_range=None,
    ):
        #
        # Compute node sizes:
        node_sizes = []
        for col in self.communities_.columns:
            sizes = self.communities_[col].to_list()
            sizes = [size for size in sizes if size.strip() != ""]
            node_sizes.append(len(sizes))

        #
        # Scales the node sizes:
        node_sizes = np.array(node_sizes)
        min_current_size = node_sizes.min()
        node_sizes = node_sizes - min_current_size + node_size_min

        if node_sizes.max() > node_size_max:
            #
            # Scales the node size to the range [node_size_min, node_size_max]
            node_sizes -= node_size_min
            node_sizes /= node_sizes.max() - node_size_min
            node_sizes *= node_size_max - node_size_min
            node_sizes += node_size_min

        n_groups = len(self.communities_.columns)

        return manifold_2d_map(
            node_x=self.centers_[dim_x],
            node_y=self.centers_[dim_y],
            node_text=self.centers_.index.to_list(),
            node_color=CLUSTER_COLORS[:n_groups],
            node_size=node_sizes,
            title_x=dim_x,
            title_y=dim_y,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
            remove_occ_gc=False,
        )


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

    communities = {fmt.format(key): communities[key] for key in communities.keys()}
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return FactorClusters(
        labels_=new_labels,
        centers_=centers,
        communities_=communities,
    )
