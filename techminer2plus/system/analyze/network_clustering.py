# flake8: noqa
"""
Network Clustering by Community Detection
===============================================================================

Clusters a database field using community detection algorithms


* **Example:** Clustering using Label Propagation

>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> co_occ_matrix = techminer2plus.system.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = techminer2plus.system.analyze.association_index(
...     co_occ_matrix, "association"
... )

>>> graph = techminer2plus.system.analyze.network_clustering(
...    normalized_co_occ_matrix,
...    algorithm='label_propagation',
... )
>>> print(techminer2plus.system.analyze.network_communities(graph).to_markdown())
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



* **Example:** Clustering using Louvain


>>> graph = techminer2plus.system.analyze.network_clustering(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> print(techminer2plus.system.analyze.network_communities(graph).to_markdown())
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


* **Example:** Clustering using Walktrap

>>> graph = techminer2plus.system.analyze.network_clustering(
...    normalized_co_occ_matrix,
...    community_clustering='walktrap',
... )
>>> print(techminer2plus.system.analyze.network_communities(graph).to_markdown())
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




# pylint: disable=line-too-long
"""
# from scipy.spatial.distance import pdist, squareform

from ...network import (
    nx_apply_community_detection_method,
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_co_occ_networks,
    nx_set_node_color_by_group,
)
from .list_cells_in_matrix import list_cells_in_matrix


def network_clustering(obj, algorithm):
    """Cluster the matrix by community detection.

    Args:
        obj (object): is a matrix.
        algorithm (str): community detection algorithm name.

    Returns:
        graph: a networkx graph.

    """

    matrix_list = list_cells_in_matrix(obj)
    graph = nx_create_graph_from_matrix_list(matrix_list)
    graph = nx_apply_community_detection_method(graph, algorithm)
    graph = nx_set_node_color_by_group(graph)
    graph = nx_set_edge_properties_for_co_occ_networks(graph)

    return graph
