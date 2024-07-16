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
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm


def cluster_networkx_graph(
    #
    # FUNCTION PARAMS:
    nx_graph,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
):

    if isinstance(algorithm_or_dict, str):
        return nx_apply_cdlib_algorithm(nx_graph, algorithm_or_dict)

    if isinstance(algorithm_or_dict, dict):
        #
        # The group is assigned using and external algorithm. It is designed
        # to provide analysis capabilities to the system when other types of
        # analysis are conducted, for example, factor analysis.
        for node, group in algorithm_or_dict.items():
            nx_graph.nodes[node]["group"] = group

    return nx_graph
