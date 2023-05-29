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
...    topic_min_occ=2,
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_criterion(
...    co_occ_matrix,
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.create_concept_grid(graph)
                         CL_00  ...                           CL_04
0               fintech 12:249  ...  artificial intelligence 04:023
1    financial services 04:168  ...    anti-money laundering 03:021
2  financial regulation 04:035  ...              charitytech 02:017
3            innovation 03:012  ...              english law 02:017
4       data protection 02:027  ...                                
5               finance 02:001  ...                                
6             reporting 02:001  ...                                
<BLANKLINE>
[7 rows x 5 columns]


Example: Clustering using sklearn algoritms.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=2,
...    root_dir=root_dir,
... )
>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(n_clusters=5, random_state=0)
>>> graph = vantagepoint.analyze.cluster_criterion(
...    co_occ_matrix,
...    sklearn_clustering=kmeans,
... )
>>> vantagepoint.analyze.create_concept_grid(graph)
                           CL_00  ...                               CL_04
0                 regtech 28:329  ...  anti money laundering (aml) 02:013
1                 fintech 12:249  ...                                    
2   regulatory technology 07:037  ...                                    
3              compliance 07:030  ...                                    
4              regulation 05:164  ...                                    
5      financial services 04:168  ...                                    
6    financial regulation 04:035  ...                                    
7         risk management 03:014  ...                                    
8              innovation 03:012  ...                                    
9              blockchain 03:005  ...                                    
10                suptech 03:004  ...                                    
11  semantic technologies 02:041  ...                                    
12                sandbox 02:012  ...                                    
13                finance 02:001  ...                                    
14              reporting 02:001  ...                                    
<BLANKLINE>
[15 rows x 5 columns]


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
    co_normalized_matrix = values / values.sum(axis=1, keepdims=True)
    dissimilarity_matrix = pdist(co_normalized_matrix, metric="euclidean")
    dissimilarity_matrix = squareform(dissimilarity_matrix)

    # perform clustering using the specified estimator
    clustering = estimator.fit(dissimilarity_matrix)

    # create a graph
    matrix_list = list_cells_in_matrix(obj)
    graph = network_utils.create_graph(matrix_list)

    columns = obj.matrix_.columns.tolist()
    labels = clustering.labels_.tolist()
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
