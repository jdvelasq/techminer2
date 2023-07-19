# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import plotly.express as px

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


def nx_set_node_color_from_group_attr(nx_graph):
    for node in nx_graph.nodes():
        group = nx_graph.nodes[node]["group"]
        nx_graph.nodes[node]["node_color"] = CLUSTER_COLORS[group]

    return nx_graph
