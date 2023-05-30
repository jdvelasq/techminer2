# flake8: noqa
"""
Cluster Criterion --- ChatGPT
===============================================================================

Example: Clustering using community detection algorithms.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=2,
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "association"
... )

>>> graph = vantagepoint.analyze.cluster_criterion(
...    normalized_co_occ_matrix,
...    community_clustering='label_propagation',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                              |
|---:|:-----------------------------------|
|  0 | regtech 28:329                     |
|  1 | fintech 12:249                     |
|  2 | regulatory technology 07:037       |
|  3 | compliance 07:030                  |
|  4 | regulation 05:164                  |
|  5 | financial services 04:168          |
|  6 | financial regulation 04:035        |
|  7 | artificial intelligence 04:023     |
|  8 | anti-money laundering 03:021       |
|  9 | risk management 03:014             |
| 10 | innovation 03:012                  |
| 11 | blockchain 03:005                  |
| 12 | suptech 03:004                     |
| 13 | semantic technologies 02:041       |
| 14 | data protection 02:027             |
| 15 | smart contracts 02:022             |
| 16 | charitytech 02:017                 |
| 17 | english law 02:017                 |
| 18 | accountability 02:014              |
| 19 | data protection officer 02:014     |
| 20 | gdpr 02:014                        |
| 21 | anti money laundering (aml) 02:013 |
| 22 | sandbox 02:012                     |
| 23 | technology 02:010                  |
| 24 | finance 02:001                     |
| 25 | reporting 02:001                   |


>>> graph = vantagepoint.analyze.cluster_criterion(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                          | CL_01                       | CL_02                              | CL_03                          |
|---:|:-------------------------------|:----------------------------|:-----------------------------------|:-------------------------------|
|  0 | regtech 28:329                 | fintech 12:249              | regulatory technology 07:037       | artificial intelligence 04:023 |
|  1 | compliance 07:030              | financial services 04:168   | regulation 05:164                  | anti-money laundering 03:021   |
|  2 | blockchain 03:005              | financial regulation 04:035 | risk management 03:014             | charitytech 02:017             |
|  3 | smart contracts 02:022         | innovation 03:012           | suptech 03:004                     | english law 02:017             |
|  4 | accountability 02:014          | data protection 02:027      | semantic technologies 02:041       |                                |
|  5 | data protection officer 02:014 | sandbox 02:012              | anti money laundering (aml) 02:013 |                                |
|  6 | gdpr 02:014                    | finance 02:001              | reporting 02:001                   |                                |
|  7 | technology 02:010              |                             |                                    |                                |


>>> graph = vantagepoint.analyze.cluster_criterion(
...    normalized_co_occ_matrix,
...    community_clustering='walktrap',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                        | CL_01                       | CL_02                  | CL_03                          | CL_04                          | CL_05                              |
|---:|:-----------------------------|:----------------------------|:-----------------------|:-------------------------------|:-------------------------------|:-----------------------------------|
|  0 | fintech 12:249               | financial services 04:168   | regtech 28:329         | artificial intelligence 04:023 | accountability 02:014          | anti money laundering (aml) 02:013 |
|  1 | regulatory technology 07:037 | financial regulation 04:035 | compliance 07:030      | anti-money laundering 03:021   | data protection officer 02:014 |                                    |
|  2 | regulation 05:164            | innovation 03:012           | blockchain 03:005      | charitytech 02:017             | gdpr 02:014                    |                                    |
|  3 | risk management 03:014       | data protection 02:027      | smart contracts 02:022 | english law 02:017             |                                |                                    |
|  4 | suptech 03:004               | sandbox 02:012              | technology 02:010      |                                |                                |                                    |
|  5 | semantic technologies 02:041 | finance 02:001              |                        |                                |                                |                                    |
|  6 | reporting 02:001             |                             |                        |                                |                                |                                    |



Example: Clustering using sklearn algoritms.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=2,
...    root_dir=root_dir,
... )
>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=4, random_state=1)
>>> graph = vantagepoint.analyze.cluster_criterion(
...    co_occ_matrix,
...    sklearn_clustering=kmeans,
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                        | CL_01                          | CL_02                          | CL_03                              |
|---:|:-----------------------------|:-------------------------------|:-------------------------------|:-----------------------------------|
|  0 | fintech 12:249               | regtech 28:329                 | artificial intelligence 04:023 | anti money laundering (aml) 02:013 |
|  1 | regulatory technology 07:037 | compliance 07:030              | anti-money laundering 03:021   |                                    |
|  2 | regulation 05:164            | blockchain 03:005              | charitytech 02:017             |                                    |
|  3 | financial services 04:168    | data protection 02:027         | english law 02:017             |                                    |
|  4 | financial regulation 04:035  | smart contracts 02:022         |                                |                                    |
|  5 | risk management 03:014       | accountability 02:014          |                                |                                    |
|  6 | innovation 03:012            | data protection officer 02:014 |                                |                                    |
|  7 | suptech 03:004               | gdpr 02:014                    |                                |                                    |
|  8 | semantic technologies 02:041 | technology 02:010              |                                |                                    |
|  9 | sandbox 02:012               |                                |                                |                                    |
| 10 | finance 02:001               |                                |                                |                                    |
| 11 | reporting 02:001             |                                |                                |                                    |


# pylint: disable=line-too-long
"""
# from scipy.spatial.distance import pdist, squareform

from ... import network_utils
from .list_cells_in_matrix import list_cells_in_matrix


def cluster_criterion(
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

    return graph
