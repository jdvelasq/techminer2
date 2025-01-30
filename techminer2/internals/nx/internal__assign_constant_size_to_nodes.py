# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__assign_constant_size_to_nodes(
    nx_graph,
    node_size,
):
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["node_size"] = node_size
    return nx_graph
