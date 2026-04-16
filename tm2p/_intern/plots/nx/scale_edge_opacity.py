import numpy as np


def scale_edge_opacity(
    params,
    nx_graph,
):

    widths = np.array([nx_graph.edges[edge]["width"] for edge in nx_graph.edges()])
    if widths.max() == widths.min():
        return nx_graph

    node_opacity = nx_graph.graph["node_opacity"]  # type: ignore
    edge_opacity_range = (
        params.edge_opacity_range[0] * node_opacity,
        params.edge_opacity_range[1] * node_opacity,
    )

    length = edge_opacity_range[1] - edge_opacity_range[0]
    prop = (widths - widths.min()) / (widths.max() - widths.min())
    opacities = edge_opacity_range[0] + prop * length

    for opacity, edge in zip(opacities, nx_graph.edges()):

        color = nx_graph.edges[edge]["color"]
        color = _apply_opacity_to_color(color, opacity)
        nx_graph.edges[edge]["color"] = color

    return nx_graph


def _apply_opacity_to_color(hex_color, opacity):

    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    return f"rgba({r}, {g}, {b}, {round(opacity, 4)})"
