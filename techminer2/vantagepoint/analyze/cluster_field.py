# flake8: noqa
"""
Cluster Field --- ChatGPT
===============================================================================

Clusters a database field using community detection algorithms or scikit-learn methods.


Example: Clustering using community detection algorithms.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "association"
... )

>>> graph = vantagepoint.analyze.cluster_field(
...    normalized_co_occ_matrix,
...    community_clustering='label_propagation',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                                  |
|---:|:---------------------------------------|
|  0 | REGTECH 28:329                         |
|  1 | FINTECH 12:249                         |
|  2 | COMPLIANCE 07:030                      |
|  3 | REGULATION 05:164                      |
|  4 | FINANCIAL_SERVICES 04:168              |
|  5 | FINANCIAL_REGULATION 04:035            |
|  6 | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |
|  7 | ANTI_MONEY_LAUNDERING 04:023           |
|  8 | ARTIFICIAL_INTELLIGENCE 04:023         |
|  9 | RISK_MANAGEMENT 03:014                 |
| 10 | INNOVATION 03:012                      |
| 11 | REGULATORY_TECHNOLOGY 03:007           |
| 12 | BLOCKCHAIN 03:005                      |
| 13 | SUPTECH 03:004                         |
| 14 | DATA_PROTECTION 02:027                 |
| 15 | SMART_CONTRACT 02:022                  |
| 16 | CHARITYTECH 02:017                     |
| 17 | ENGLISH_LAW 02:017                     |
| 18 | ACCOUNTABILITY 02:014                  |
| 19 | DATA_PROTECTION_OFFICER 02:014         |
| 20 | GDPR 02:014                            |
| 21 | SANDBOXES 02:012                       |
| 22 | TECHNOLOGY 02:010                      |
| 23 | FINANCE 02:001                         |
| 24 | REPORTING 02:001                       |




>>> graph = vantagepoint.analyze.cluster_field(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                          | CL_01                       | CL_02                        | CL_03                                  |
|---:|:-------------------------------|:----------------------------|:-----------------------------|:---------------------------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249              | REGULATION 05:164            | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |
|  1 | COMPLIANCE 07:030              | FINANCIAL_SERVICES 04:168   | RISK_MANAGEMENT 03:014       | ANTI_MONEY_LAUNDERING 04:023           |
|  2 | BLOCKCHAIN 03:005              | FINANCIAL_REGULATION 04:035 | REGULATORY_TECHNOLOGY 03:007 | ARTIFICIAL_INTELLIGENCE 04:023         |
|  3 | SMART_CONTRACT 02:022          | INNOVATION 03:012           | SUPTECH 03:004               | CHARITYTECH 02:017                     |
|  4 | ACCOUNTABILITY 02:014          | DATA_PROTECTION 02:027      | REPORTING 02:001             | ENGLISH_LAW 02:017                     |
|  5 | DATA_PROTECTION_OFFICER 02:014 | FINANCE 02:001              |                              |                                        |
|  6 | GDPR 02:014                    |                             |                              |                                        |
|  7 | SANDBOXES 02:012               |                             |                              |                                        |
|  8 | TECHNOLOGY 02:010              |                             |                              |                                        |




>>> graph = vantagepoint.analyze.cluster_field(
...    normalized_co_occ_matrix,
...    community_clustering='walktrap',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                        | CL_01                          | CL_02                                  | CL_03                          |
|---:|:-----------------------------|:-------------------------------|:---------------------------------------|:-------------------------------|
|  0 | FINTECH 12:249               | REGTECH 28:329                 | REGULATORY_TECHNOLOGY (REGTECH) 04:030 | ACCOUNTABILITY 02:014          |
|  1 | REGULATION 05:164            | COMPLIANCE 07:030              | ANTI_MONEY_LAUNDERING 04:023           | DATA_PROTECTION_OFFICER 02:014 |
|  2 | FINANCIAL_SERVICES 04:168    | ARTIFICIAL_INTELLIGENCE 04:023 | CHARITYTECH 02:017                     | GDPR 02:014                    |
|  3 | FINANCIAL_REGULATION 04:035  | BLOCKCHAIN 03:005              | ENGLISH_LAW 02:017                     |                                |
|  4 | RISK_MANAGEMENT 03:014       | SMART_CONTRACT 02:022          |                                        |                                |
|  5 | INNOVATION 03:012            | TECHNOLOGY 02:010              |                                        |                                |
|  6 | REGULATORY_TECHNOLOGY 03:007 |                                |                                        |                                |
|  7 | SUPTECH 03:004               |                                |                                        |                                |
|  8 | DATA_PROTECTION 02:027       |                                |                                        |                                |
|  9 | SANDBOXES 02:012             |                                |                                        |                                |
| 10 | FINANCE 02:001               |                                |                                        |                                |
| 11 | REPORTING 02:001             |                                |                                        |                                |


Example: Clustering using sklearn algoritms.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4, random_state=1)
>>> graph = vantagepoint.analyze.cluster_field(
...    co_occ_matrix,
...    sklearn_clustering=kmeans,
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                        | CL_01                          | CL_02                          | CL_03                                  |
|---:|:-----------------------------|:-------------------------------|:-------------------------------|:---------------------------------------|
|  0 | REGTECH 28:329               | COMPLIANCE 07:030              | ANTI_MONEY_LAUNDERING 04:023   | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |
|  1 | FINTECH 12:249               | ACCOUNTABILITY 02:014          | ARTIFICIAL_INTELLIGENCE 04:023 | INNOVATION 03:012                      |
|  2 | REGULATION 05:164            | DATA_PROTECTION_OFFICER 02:014 | CHARITYTECH 02:017             |                                        |
|  3 | FINANCIAL_SERVICES 04:168    | GDPR 02:014                    | ENGLISH_LAW 02:017             |                                        |
|  4 | FINANCIAL_REGULATION 04:035  | TECHNOLOGY 02:010              |                                |                                        |
|  5 | RISK_MANAGEMENT 03:014       |                                |                                |                                        |
|  6 | REGULATORY_TECHNOLOGY 03:007 |                                |                                |                                        |
|  7 | BLOCKCHAIN 03:005            |                                |                                |                                        |
|  8 | SUPTECH 03:004               |                                |                                |                                        |
|  9 | DATA_PROTECTION 02:027       |                                |                                |                                        |
| 10 | SMART_CONTRACT 02:022        |                                |                                |                                        |
| 11 | SANDBOXES 02:012             |                                |                                |                                        |
| 12 | FINANCE 02:001               |                                |                                |                                        |
| 13 | REPORTING 02:001             |                                |                                |                                        |



# pylint: disable=line-too-long
"""
# from scipy.spatial.distance import pdist, squareform

from ... import network_utils
from .list_cells_in_matrix import list_cells_in_matrix


def cluster_field(
    obj,
    sklearn_clustering=None,
    community_clustering=None,
):
    """Cluster a co-occurrence matrix"""

    if sklearn_clustering is None and community_clustering is None:
        raise ValueError(
            "sklearn_clustering and community_clustering cannot be both None."
        )

    if sklearn_clustering is not None and community_clustering is not None:
        raise ValueError(
            "sklearn_clustering and community_clustering cannot be both different of None."
        )

    if community_clustering is not None:
        return _cluster_by_commnunity_detection(obj, community_clustering)

    if sklearn_clustering is not None:
        return _cluster_by_sklearn(obj, sklearn_clustering)

    raise ValueError("This should not happen.")


def _cluster_by_sklearn(obj, estimator):
    """Cluster the matrix by sklearn cluster methods.

    Args:
        obj (object): is a matrix.
        estimator (object): sklearn cluster estimator.

    Returns:
        graph: a networkx graph.

    """

    # compute the dissimilarity matrix
    values = obj.matrix_.values
    dissimilarity_matrix = values / values.sum(axis=1, keepdims=True)
    # dissimilarity_matrix = values
    # dissimilarity_matrix = pdist(co_normalized_matrix, metric="euclidean")
    # dissimilarity_matrix = squareform(dissimilarity_matrix)

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
    graph = network_utils.create_graph(matrix_list)

    columns = obj.matrix_.columns.tolist()
    names2cluster = dict(zip(columns, labels))

    for node in graph.nodes():
        graph.nodes[node]["group"] = names2cluster[node]

    graph = network_utils.set_color_nodes_by_group(graph)

    return graph


def _cluster_by_commnunity_detection(obj, algorithm):
    """Cluster the matrix by community detection.

    Args:
        obj (object): is a matrix.
        algorithm (str): community detection algorithm name.

    Returns:
        graph: a networkx graph.

    """

    matrix_list = list_cells_in_matrix(obj)
    graph = network_utils.create_graph(matrix_list)
    graph = network_utils.apply_community_detection_method(graph, algorithm)
    graph = network_utils.set_color_nodes_by_group(graph)
    graph = network_utils.set_properties_for_co_occ_networks(graph)

    return graph
