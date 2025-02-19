# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__assign_degree_to_nodes(nx_graph):
    for node, adjacencies in nx_graph.adjacency():
        nx_graph.nodes[node]["degree"] = len(adjacencies)

    return nx_graph
