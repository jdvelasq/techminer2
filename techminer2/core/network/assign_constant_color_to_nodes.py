# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def assign_constant_color_to_nodes(nx_graph, color):
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["node_color"] = color
    return nx_graph
