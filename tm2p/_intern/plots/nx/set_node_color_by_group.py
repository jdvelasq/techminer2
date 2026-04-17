import networkx as nx  # type: ignore
import plotly.express as px  # type: ignore

from tm2p._intern import Params


def set_node_color_by_group(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    colors = (
        list(params.node_colors_discrete)
        + px.colors.qualitative.Pastel1
        + px.colors.qualitative.Pastel2
        + px.colors.qualitative.Dark24
        + px.colors.qualitative.Light24
        + px.colors.qualitative.Set1
        + px.colors.qualitative.Set2
        + px.colors.qualitative.Set3
    )

    for node in nx_graph.nodes():
        group = nx_graph.nodes[node]["group"]
        nx_graph.nodes[node]["node_color"] = colors[group]
    return nx_graph
