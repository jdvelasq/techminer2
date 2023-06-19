# flake8: noqa
"""
Cluster (Co-occurrence) Network 
===============================================================================

Clusters a co-occurrence network using community detection algorithm or sklearn algoritmos.


* **Example:** Clustering using Label Propagation

>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> co_occ_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )

>>> graph = techminer2plus.analyze.network.cluster_network(
...    co_occ_matrix,
...    normalization_index='association',
...    algorithm_or_estimator='label_propagation',
... )
>>> print(techminer2plus.analyze.network.network_communities(graph).to_markdown())
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
| 20 | GDPR 02:014                    |
| 21 | SANDBOXES 02:012               |
| 22 | TECHNOLOGY 02:010              |
| 23 | FINANCE 02:001                 |
| 24 | REPORTING 02:001               |



* **Example:** Clustering using Louvain


>>> graph = techminer2plus.analyze.network.cluster_network(
...    co_occ_matrix,
...    normalization_index='association',
...    algorithm_or_estimator='louvain',
... )
>>> print(techminer2plus.analyze.network.network_communities(graph).to_markdown())
|    | CL_00                          | CL_01                       | CL_02                        | CL_03                          |
|---:|:-------------------------------|:----------------------------|:-----------------------------|:-------------------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249              | REGULATORY_TECHNOLOGY 07:037 | ANTI_MONEY_LAUNDERING 05:034   |
|  1 | COMPLIANCE 07:030              | FINANCIAL_SERVICES 04:168   | REGULATION 05:164            | ARTIFICIAL_INTELLIGENCE 04:023 |
|  2 | BLOCKCHAIN 03:005              | FINANCIAL_REGULATION 04:035 | RISK_MANAGEMENT 03:014       | CHARITYTECH 02:017             |
|  3 | SMART_CONTRACTS 02:022         | INNOVATION 03:012           | SUPTECH 03:004               | ENGLISH_LAW 02:017             |
|  4 | ACCOUNTABILITY 02:014          | DATA_PROTECTION 02:027      | SEMANTIC_TECHNOLOGIES 02:041 |                                |
|  5 | DATA_PROTECTION_OFFICER 02:014 | SANDBOXES 02:012            | REPORTING 02:001             |                                |
|  6 | GDPR 02:014                    | FINANCE 02:001              |                              |                                |
|  7 | TECHNOLOGY 02:010              |                             |                              |                                |

    


* **Example:** Clustering using Walktrap

>>> graph = techminer2plus.analyze.network.cluster_network(
...    co_occ_matrix,
...    normalization_index='association',
...    algorithm_or_estimator='walktrap',
... )
>>> print(techminer2plus.analyze.network.network_communities(graph).to_markdown())
|    | CL_00                        | CL_01                       | CL_02                          | CL_03                          |
|---:|:-----------------------------|:----------------------------|:-------------------------------|:-------------------------------|
|  0 | REGTECH 28:329               | FINANCIAL_SERVICES 04:168   | ANTI_MONEY_LAUNDERING 05:034   | ACCOUNTABILITY 02:014          |
|  1 | FINTECH 12:249               | FINANCIAL_REGULATION 04:035 | ARTIFICIAL_INTELLIGENCE 04:023 | DATA_PROTECTION_OFFICER 02:014 |
|  2 | REGULATORY_TECHNOLOGY 07:037 | INNOVATION 03:012           | CHARITYTECH 02:017             | GDPR 02:014                    |
|  3 | COMPLIANCE 07:030            | DATA_PROTECTION 02:027      | ENGLISH_LAW 02:017             |                                |
|  4 | REGULATION 05:164            | SANDBOXES 02:012            |                                |                                |
|  5 | RISK_MANAGEMENT 03:014       | FINANCE 02:001              |                                |                                |
|  6 | BLOCKCHAIN 03:005            |                             |                                |                                |
|  7 | SUPTECH 03:004               |                             |                                |                                |
|  8 | SEMANTIC_TECHNOLOGIES 02:041 |                             |                                |                                |
|  9 | SMART_CONTRACTS 02:022       |                             |                                |                                |
| 10 | TECHNOLOGY 02:010            |                             |                                |                                |
| 11 | REPORTING 02:001             |                             |                                |                                |




* **Example**

>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4, random_state=1)
>>> graph = techminer2plus.analyze.network.cluster_network(
...    co_occ_matrix,
...    algorithm_or_estimator=kmeans,
... )
>>> print(techminer2plus.analyze.network.network_communities(graph).to_markdown())
|    | CL_00                        | CL_01                          | CL_02                          | CL_03                        |
|---:|:-----------------------------|:-------------------------------|:-------------------------------|:-----------------------------|
|  0 | REGTECH 28:329               | REGULATORY_TECHNOLOGY 07:037   | ACCOUNTABILITY 02:014          | ANTI_MONEY_LAUNDERING 05:034 |
|  1 | FINTECH 12:249               | REGULATION 05:164              | DATA_PROTECTION_OFFICER 02:014 | CHARITYTECH 02:017           |
|  2 | COMPLIANCE 07:030            | ARTIFICIAL_INTELLIGENCE 04:023 | GDPR 02:014                    | ENGLISH_LAW 02:017           |
|  3 | FINANCIAL_SERVICES 04:168    | RISK_MANAGEMENT 03:014         |                                |                              |
|  4 | FINANCIAL_REGULATION 04:035  | SUPTECH 03:004                 |                                |                              |
|  5 | INNOVATION 03:012            | REPORTING 02:001               |                                |                              |
|  6 | BLOCKCHAIN 03:005            |                                |                                |                              |
|  7 | SEMANTIC_TECHNOLOGIES 02:041 |                                |                                |                              |
|  8 | DATA_PROTECTION 02:027       |                                |                                |                              |
|  9 | SMART_CONTRACTS 02:022       |                                |                                |                              |
| 10 | SANDBOXES 02:012             |                                |                                |                              |
| 11 | TECHNOLOGY 02:010            |                                |                                |                              |
| 12 | FINANCE 02:001               |                                |                                |                              |



# pylint: disable=line-too-long
"""
# from scipy.spatial.distance import pdist, squareform

from ...network import (
    nx_apply_community_detection_method,
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_co_occ_networks,
    nx_set_node_color_by_group,
)
from ..matrix.co_occurrence_matrix import co_occurrence_matrix
from ..matrix.list_cells_in_matrix import list_cells_in_matrix
from .matrix_normalization import matrix_normalization


def cluster_network(
    obj=None,
    algorithm_or_estimator=None,
    #
    # Co-occurrente matrix params:
    normalization_index=None,
    rows_and_columns=None,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Cluster a co-occurrence matrix"""

    if obj is None:
        obj = co_occurrence_matrix(
            columns=rows_and_columns,
            #
            # Columns item filters:
            col_top_n=top_n,
            col_occ_range=occ_range,
            col_gc_range=gc_range,
            col_custom_items=custom_items,
            #
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        obj = matrix_normalization(obj, normalization_index)

    if isinstance(algorithm_or_estimator, str):
        return cluster_network_with_community_deteccion(
            obj, algorithm_or_estimator
        )
    return cluster_network_with_sklearn_estimators(obj, algorithm_or_estimator)


def cluster_network_with_community_deteccion(
    obj=None,
    algorithm=None,
):
    """Cluster a co-occurrence matrix

    :meta private:
    """

    matrix_list = list_cells_in_matrix(obj)
    graph = nx_create_graph_from_matrix_list(matrix_list)
    graph = nx_apply_community_detection_method(graph, algorithm)
    graph = nx_set_node_color_by_group(graph)
    graph = nx_set_edge_properties_for_co_occ_networks(graph)

    return graph


def cluster_network_with_sklearn_estimators(
    obj,
    estimator,
):
    """Cluster the matrix by sklearn cluster methods.

    :meta private:
    """

    # compute the dissimilarity matrix
    values = obj.matrix_.values
    dissimilarity_matrix = values / values.sum(axis=1, keepdims=True)

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
    matrix_list = list_cells_in_matrix(obj)
    graph = nx_create_graph_from_matrix_list(matrix_list)

    columns = obj.matrix_.columns.tolist()
    names2cluster = dict(zip(columns, labels))

    for node in graph.nodes():
        graph.nodes[node]["group"] = names2cluster[node]

    graph = nx_set_node_color_by_group(graph)

    return graph
