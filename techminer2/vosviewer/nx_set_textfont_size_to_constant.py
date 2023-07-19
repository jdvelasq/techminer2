# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def nx_set_textfont_size_to_constant(nx_graph, textfont_size):
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["textfont_size"] = textfont_size
    return nx_graph
