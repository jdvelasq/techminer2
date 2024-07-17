# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def nx_assign_constant_opacity_to_text(
    nx_graph,
    opacity,
):
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["textfont_opacity"] = opacity
    return nx_graph
