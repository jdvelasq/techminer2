import networkx as nx  # type: ignore
import plotly.express as px  # type: ignore

from tm2p._intern import Params


def set_node_color_by_group(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    colors = (
        list(params.node_colors_discrete)
        + rgb_colors_to_hex(px.colors.qualitative.Pastel1)
        + rgb_colors_to_hex(px.colors.qualitative.Pastel2)
        + px.colors.qualitative.Dark24
        + px.colors.qualitative.Light24
        + rgb_colors_to_hex(px.colors.qualitative.Set1)
        + rgb_colors_to_hex(px.colors.qualitative.Set2)
        + rgb_colors_to_hex(px.colors.qualitative.Set3)
    )

    for node in nx_graph.nodes():
        group = nx_graph.nodes[node]["group"]
        nx_graph.nodes[node]["node_color"] = colors[group]
    return nx_graph


def rgb_colors_to_hex(colors):
    hex_colors = []
    for color in colors:
        r, g, b = map(int, color.lstrip("rgb(").rstrip(")").split(","))
        hex_colors.append(rgb_to_hex(r, g, b))
    return hex_colors


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02X}{g:02X}{b:02X}"
