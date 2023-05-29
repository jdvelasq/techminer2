# flake8: noqa
"""
Cluster Criterion --- ChatGPT
===============================================================================

Example: Clustering using community detection algorithms.
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=2,
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_criterion(
...    occ_matrix,
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

"""

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
