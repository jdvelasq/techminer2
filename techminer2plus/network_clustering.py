# flake8: noqa
"""
Network Clustering
===============================================================================

Clusters a co-occurrence network using community detection algorithm or sklearn algoritmos.


* **Example:** Clustering using Label Propagation

>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )

>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    normalization_index='association',
...    algorithm_or_estimator='label_propagation',
... )
>>> print(techminer2plus.network_communities(graph).to_markdown())
|    | CL_00                          |
|---:|:-------------------------------|
|  0 | REGTECH 28:329                 |
|  1 | FINTECH 12:249                 |
|  2 | REGULATORY_TECHNOLOGY 07:037   |
|  3 | COMPLIANCE 07:030              |
|  4 | REGULATION 05:164              |
|  5 | ANTI_MONEY_LAUNDERING 05:034   |
|  6 | FINANCIAL_SERVICES 04:168      |
|  7 | FINANCIAL_REGULATION 04:035    |
|  8 | ARTIFICIAL_INTELLIGENCE 04:023 |
|  9 | RISK_MANAGEMENT 03:014         |
| 10 | INNOVATION 03:012              |
| 11 | BLOCKCHAIN 03:005              |
| 12 | SUPTECH 03:004                 |
| 13 | SEMANTIC_TECHNOLOGIES 02:041   |
| 14 | DATA_PROTECTION 02:027         |
| 15 | SMART_CONTRACTS 02:022         |
| 16 | CHARITYTECH 02:017             |
| 17 | ENGLISH_LAW 02:017             |
| 18 | ACCOUNTABILITY 02:014          |
| 19 | DATA_PROTECTION_OFFICER 02:014 |



* **Example:** Clustering using Louvain


>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    normalization_index='association',
...    algorithm_or_estimator='louvain',
... )
>>> print(techminer2plus.network_communities(graph).to_markdown())
|    | CL_00                          | CL_01                       | CL_02                        | CL_03                          |
|---:|:-------------------------------|:----------------------------|:-----------------------------|:-------------------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249              | REGULATORY_TECHNOLOGY 07:037 | ANTI_MONEY_LAUNDERING 05:034   |
|  1 | COMPLIANCE 07:030              | FINANCIAL_SERVICES 04:168   | REGULATION 05:164            | ARTIFICIAL_INTELLIGENCE 04:023 |
|  2 | BLOCKCHAIN 03:005              | FINANCIAL_REGULATION 04:035 | RISK_MANAGEMENT 03:014       | CHARITYTECH 02:017             |
|  3 | SMART_CONTRACTS 02:022         | INNOVATION 03:012           | SUPTECH 03:004               | ENGLISH_LAW 02:017             |
|  4 | ACCOUNTABILITY 02:014          | DATA_PROTECTION 02:027      | SEMANTIC_TECHNOLOGIES 02:041 |                                |
|  5 | DATA_PROTECTION_OFFICER 02:014 |                             |                              |                                |



* **Example:** Clustering using Walktrap

>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    normalization_index='association',
...    algorithm_or_estimator='walktrap',
... )
>>> print(techminer2plus.network_communities(graph).to_markdown())
|    | CL_00                        | CL_01                          | CL_02                        | CL_03                       | CL_04                          |
|---:|:-----------------------------|:-------------------------------|:-----------------------------|:----------------------------|:-------------------------------|
|  0 | FINTECH 12:249               | REGTECH 28:329                 | ANTI_MONEY_LAUNDERING 05:034 | FINANCIAL_SERVICES 04:168   | ACCOUNTABILITY 02:014          |
|  1 | REGULATION 05:164            | REGULATORY_TECHNOLOGY 07:037   | CHARITYTECH 02:017           | FINANCIAL_REGULATION 04:035 | DATA_PROTECTION_OFFICER 02:014 |
|  2 | RISK_MANAGEMENT 03:014       | COMPLIANCE 07:030              | ENGLISH_LAW 02:017           | DATA_PROTECTION 02:027      |                                |
|  3 | INNOVATION 03:012            | ARTIFICIAL_INTELLIGENCE 04:023 |                              |                             |                                |
|  4 | SUPTECH 03:004               | BLOCKCHAIN 03:005              |                              |                             |                                |
|  5 | SEMANTIC_TECHNOLOGIES 02:041 | SMART_CONTRACTS 02:022         |                              |                             |                                |



* **Example:** K-means clustering

>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4, random_state=1)
>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    algorithm_or_estimator=kmeans,
... )
>>> print(techminer2plus.network_communities(graph).to_markdown())
|    | CL_00                        | CL_01                          | CL_02                     | CL_03                          |
|---:|:-----------------------------|:-------------------------------|:--------------------------|:-------------------------------|
|  0 | REGTECH 28:329               | ANTI_MONEY_LAUNDERING 05:034   | FINANCIAL_SERVICES 04:168 | ACCOUNTABILITY 02:014          |
|  1 | FINTECH 12:249               | ARTIFICIAL_INTELLIGENCE 04:023 | DATA_PROTECTION 02:027    | DATA_PROTECTION_OFFICER 02:014 |
|  2 | REGULATORY_TECHNOLOGY 07:037 | CHARITYTECH 02:017             | SMART_CONTRACTS 02:022    |                                |
|  3 | COMPLIANCE 07:030            | ENGLISH_LAW 02:017             |                           |                                |
|  4 | REGULATION 05:164            |                                |                           |                                |
|  5 | FINANCIAL_REGULATION 04:035  |                                |                           |                                |
|  6 | RISK_MANAGEMENT 03:014       |                                |                           |                                |
|  7 | INNOVATION 03:012            |                                |                           |                                |
|  8 | BLOCKCHAIN 03:005            |                                |                           |                                |
|  9 | SUPTECH 03:004               |                                |                           |                                |
| 10 | SEMANTIC_TECHNOLOGIES 02:041 |                                |                           |                                |


# pylint: disable=line-too-long
"""
import numpy as np

from .list_cells_in_matrix import list_cells_in_matrix
from .matrix_normalization import matrix_normalization
from .network_lib import (
    nx_apply_community_detection_method,
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_co_occ_networks,
    nx_set_node_color_by_group,
)


def network_clustering(
    cooc_matrix=None,
    algorithm_or_estimator=None,
    normalization_index=None,
):
    """Cluster a co-occurrence matrix"""

    cooc_matrix = matrix_normalization(cooc_matrix, normalization_index)

    if isinstance(algorithm_or_estimator, str):
        return cluster_network_with_community_deteccion(
            cooc_matrix, algorithm_or_estimator
        )

    return cluster_network_with_sklearn_estimators(
        cooc_matrix, algorithm_or_estimator
    )


def cluster_network_with_community_deteccion(
    cooc_matrix=None,
    algorithm=None,
):
    """Cluster a co-occurrence matrix

    :meta private:
    """

    matrix_list = list_cells_in_matrix(cooc_matrix)
    graph = nx_create_graph_from_matrix_list(matrix_list)
    graph = nx_apply_community_detection_method(graph, algorithm)
    graph = nx_set_node_color_by_group(graph)
    graph = nx_set_edge_properties_for_co_occ_networks(graph)

    return graph


def cluster_network_with_sklearn_estimators(
    cooc_matrix,
    estimator,
):
    """Cluster the matrix by sklearn cluster methods.

    :meta private:
    """

    # compute the dissimilarity matrix
    values = cooc_matrix.df_.values
    np.fill_diagonal(values, 0)
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

    return graph
