# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__assign_uniform_color_to_edges(
    nx_graph,
    color,
):
    for edge in nx_graph.edges():
        nx_graph.edges[edge]["color"] = color
    return nx_graph
