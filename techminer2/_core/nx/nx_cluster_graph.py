# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Creates a co-occurrence networkx graph from a co-occurrence matrix.


"""
from cdlib import algorithms  # type: ignore


def nx_cluster_graph(
    #
    # FUNCTION PARAMS:
    nx_graph,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
):

    if isinstance(algorithm_or_dict, str):
        return _apply_cdlib_algorithm(nx_graph, algorithm_or_dict)

    if isinstance(algorithm_or_dict, dict):
        #
        # The group is assigned using and external algorithm. It is designed
        # to provide analysis capabilities to the system when other types of
        # analysis are conducted, for example, factor analysis.
        for node, group in algorithm_or_dict.items():
            nx_graph.nodes[node]["group"] = group

    return nx_graph


def _apply_cdlib_algorithm(
    nx_graph,
    algorithm,
):
    """Network community detection."""

    cdlib_algorithm = {
        "label_propagation": algorithms.label_propagation,
        "leiden": algorithms.leiden,
        "louvain": algorithms.louvain,
        "walktrap": algorithms.walktrap,
    }[algorithm]

    if algorithm == "label_propagation":
        communities = cdlib_algorithm(nx_graph).communities
    elif algorithm == "leiden":
        communities = cdlib_algorithm(nx_graph).communities
    elif algorithm == "louvain":
        communities = cdlib_algorithm(nx_graph, randomize=False).communities
    elif algorithm == "walktrap":
        communities = cdlib_algorithm(nx_graph).communities

    for i_community, community in enumerate(communities):
        for node in community:
            nx_graph.nodes[node]["group"] = i_community

    return nx_graph
