# flake8: noqa
"""
Factor Matrix Clustering
===============================================================================

Clusters a factor matrix using sklearn algorithms.

>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> factor_matrix = techminer2plus.factor_matrix_kernel_pca(
...     cooc_matrix,
... )


>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4, random_state=1)
>>> graph = techminer2plus.factor_matrix_clustering(
...    factor_matrix,
...    cooc_matrix,
...    estimator=kmeans,
... )

>>> print(techminer2plus.network_communities(graph).to_markdown())
|    | CL_00                          | CL_01                          | CL_02             | CL_03             |
|---:|:-------------------------------|:-------------------------------|:------------------|:------------------|
|  0 | REGULATORY_TECHNOLOGY 07:037   | ANTI_MONEY_LAUNDERING 05:034   | FINTECH 12:249    | REGTECH 28:329    |
|  1 | FINANCIAL_SERVICES 04:168      | ARTIFICIAL_INTELLIGENCE 04:023 | REGULATION 05:164 | COMPLIANCE 07:030 |
|  2 | FINANCIAL_REGULATION 04:035    | RISK_MANAGEMENT 03:014         |                   |                   |
|  3 | INNOVATION 03:012              | SUPTECH 03:004                 |                   |                   |
|  4 | BLOCKCHAIN 03:005              |                                |                   |                   |
|  5 | SEMANTIC_TECHNOLOGIES 02:041   |                                |                   |                   |
|  6 | DATA_PROTECTION 02:027         |                                |                   |                   |
|  7 | SMART_CONTRACTS 02:022         |                                |                   |                   |
|  8 | CHARITYTECH 02:017             |                                |                   |                   |
|  9 | ENGLISH_LAW 02:017             |                                |                   |                   |
| 10 | ACCOUNTABILITY 02:014          |                                |                   |                   |
| 11 | DATA_PROTECTION_OFFICER 02:014 |                                |                   |                   |


# pylint: disable=line-too-long
"""
import numpy as np

from ._network_lib import (
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_co_occ_networks,
    nx_set_node_color_by_group,
)
from .list_cells_in_matrix import list_cells_in_matrix


# pylint: disable=too-many-locals
def factor_matrix_clustering(
    factor_matrix,
    cooc_matrix,
    estimator,
):
    """Cluster a factor matrix using sckit-learn estimators."""

    n_clusters = estimator.get_params()["n_clusters"]

    # compute the dissimilarity matrix
    values = factor_matrix.df_.values
    np.fill_diagonal(values, 0)

    values = values[:, : n_clusters - 1]

    dissimilarity_matrix = values / np.abs(values).sum(axis=1, keepdims=True)

    # perform clustering using the specified estimator
    clustering = estimator.fit(dissimilarity_matrix)
    labels = clustering.labels_.tolist()

    # create communities
    n_clusters = len(set(labels))
    communities = {i_cluster: [] for i_cluster in range(n_clusters)}
    for i_label, label in enumerate(labels):
        communities[label].append(i_label)

    lengths = [(key, len(communities[key])) for key in communities.keys()]
    lengths = sorted(lengths, key=lambda x: x[1], reverse=True)

    new_labels = {}
    for new_label, (old_label, _) in enumerate(lengths):
        new_labels[old_label] = new_label

    labels = [new_labels[label] for label in labels]

    # create a graph
    matrix_list = list_cells_in_matrix(cooc_matrix)
    graph = nx_create_graph_from_matrix_list(matrix_list)

    columns = cooc_matrix.df_.columns.tolist()
    names2cluster = dict(zip(columns, labels))

    for node in graph.nodes():
        graph.nodes[node]["group"] = names2cluster[node]

    graph = nx_set_node_color_by_group(graph)
    graph = nx_set_edge_properties_for_co_occ_networks(graph)

    return graph
