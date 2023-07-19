# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


#
# Apply network community dectection algoriths to a nx_graph
#
from cdlib import algorithms


def nx_apply_cdlib_algorithm(
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
