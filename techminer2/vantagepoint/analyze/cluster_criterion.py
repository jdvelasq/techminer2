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
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.cluster_members(graph)
                            CL_00  ...                           CL_03
0                  regtech 28:329  ...  artificial intelligence 04:023
1               compliance 07:030  ...    anti-money laundering 03:021
2               blockchain 03:005  ...              charitytech 02:017
3          smart contracts 02:022  ...              english law 02:017
4           accountability 02:014  ...                                
5  data protection officer 02:014  ...                                
6                     gdpr 02:014  ...                                
7               technology 02:010  ...                                
<BLANKLINE>
[8 rows x 4 columns]


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
>>> kmeans = KMeans(n_clusters=4, random_state=0)
>>> graph = vantagepoint.analyze.cluster_criterion(
...    co_occ_matrix,
...    sklearn_clustering=kmeans,
... )
>>> vantagepoint.analyze.cluster_members(graph)



"""
from scipy.spatial.distance import pdist, squareform

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
    dissimilarity_matrix = pdist(values, metric="euclidean")
    dissimilarity_matrix = squareform(dissimilarity_matrix)
    # co_normalized_matrix = values / values.sum(axis=1, keepdims=True)
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
