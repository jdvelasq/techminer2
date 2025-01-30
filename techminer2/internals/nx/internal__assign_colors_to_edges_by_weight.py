# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import numpy as np

COLOR_PALETTE = (
    "#dedfe2",
    "#c4c7cb",
    "#aaaeb3",
    "#91959c",
    "#777c85",
    "#60646b",
    "#494c51",
    "#323438",
    "#1b1c1e",
)


def internal__assign_colors_to_edges_by_weight(
    nx_graph,
    color_palette=COLOR_PALETTE,
):
    #
    #
    widths = np.array([nx_graph.edges[edge]["weight"] for edge in nx_graph.edges()])

    #
    # Computes the color
    min_width = min(widths)
    max_width = max(widths)
    widths = widths - min_width
    widths /= max_width
    colors = [color_palette[int(width * (len(color_palette) - 1))] for width in widths]

    #
    # Sets the link color
    for edge, color in zip(nx_graph.edges(), colors):
        nx_graph.edges[edge]["color"] = color
    return nx_graph
