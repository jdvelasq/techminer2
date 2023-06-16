# flake8: noqa
"""
Matrix Clustering by ML Methods
===============================================================================

Clusters a database field using clustering methods based on machine learning.


* **Example**


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
>>> print(vantagepoint.analyze.network_communities(graph).to_markdown())
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


def matrix_clustering(
    obj,
    estimator,
):
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
    graph = network_utils.nx_create_graph_from_matrix_list(matrix_list)

    columns = obj.matrix_.columns.tolist()
    names2cluster = dict(zip(columns, labels))

    for node in graph.nodes():
        graph.nodes[node]["group"] = names2cluster[node]

    graph = network_utils.nx_set_node_color_by_group(graph)

    return graph
