"""
Slope chart
===============================================================================
"""
import textwrap

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .plots.multiindex2text import multindex2text

TEXTLEN = 35


def slope_chart(
    matrix,
    figsize=(6, 6),
    cmap="Greys",
    cmap_by="Reds",
    fontsize=9,
):

    matrix = matrix.copy()
    if isinstance(matrix.columns, pd.MultiIndex):
        matrix.columns = multindex2text(matrix.columns)

    if isinstance(matrix.index, pd.MultiIndex):
        matrix.index = multindex2text(matrix.index)

    matplotlib.rc("font", size=fontsize)

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    cmap = plt.cm.get_cmap(cmap)
    cmap_by = plt.cm.get_cmap(cmap_by)

    m = len(matrix.index)
    n = len(matrix.columns)
    maxmn = max(m, n)
    yleft = (maxmn - m) / 2.0 + np.linspace(0, m, m)
    yright = (maxmn - n) / 2.0 + np.linspace(0, n, n)

    ax.vlines(
        x=1,
        ymin=-1,
        ymax=maxmn + 1,
        color="gray",
        alpha=0.7,
        linewidth=1,
        linestyles="dotted",
    )

    ax.vlines(
        x=3,
        ymin=-1,
        ymax=maxmn + 1,
        color="gray",
        alpha=0.7,
        linewidth=1,
        linestyles="dotted",
    )

    #
    # Dibuja los ejes para las conexiones
    #
    ax.scatter(x=[1] * m, y=yleft, s=1)
    ax.scatter(x=[3] * n, y=yright, s=1)

    #
    # Dibuja las conexiones
    #
    maxlink = matrix.max().max()
    minlink = matrix.values.ravel()
    minlink = min([v for v in minlink if v > 0])
    for idx, index in enumerate(matrix.index):
        for icol, col in enumerate(matrix.columns):
            link = matrix.loc[index, col]
            if link > 0:
                ax.plot(
                    [1, 3],
                    [yleft[idx], yright[icol]],
                    c="k",
                    linewidth=0.5 + 4 * (link - minlink) / (maxlink - minlink),
                    alpha=0.5 + 0.5 * (link - minlink) / (maxlink - minlink),
                )

    #
    # Sizes
    #
    left_sizes = [int(t.split(" ")[-1].split(":")[0]) for t in matrix.index]
    right_sizes = [int(t.split(" ")[-1].split(":")[0]) for t in matrix.columns]

    min_size = min(left_sizes + right_sizes)
    max_size = max(left_sizes + right_sizes)

    left_sizes = [
        150 + 2000 * (t - min_size) / (max_size - min_size) for t in left_sizes
    ]
    right_sizes = [
        150 + 2000 * (t - min_size) / (max_size - min_size) for t in right_sizes
    ]

    #
    # Colors
    #
    left_colors = [int(t.split(" ")[-1].split(":")[1]) for t in matrix.index]
    right_colors = [int(t.split(" ")[-1].split(":")[1]) for t in matrix.columns]

    min_color = min(left_colors + right_colors)
    max_color = max(left_colors + right_colors)

    left_colors = [
        cmap_by(0.1 + 0.9 * (t - min_color) / (max_color - min_color))
        for t in left_colors
    ]
    right_colors = [
        cmap(0.1 + 0.9 * (t - min_color) / (max_color - min_color))
        for t in right_colors
    ]

    ax.scatter(
        x=[1] * m,
        y=yleft,
        s=left_sizes,
        c=left_colors,
        zorder=10,
        linewidths=1,
        edgecolors="k",
    )

    for idx, text in enumerate(matrix.index):
        ax.plot([0.7, 1.0], [yleft[idx], yleft[idx]], "-", c="grey")

    for idx, text in enumerate(matrix.index):
        ax.text(
            0.7,
            yleft[idx],
            text,
            fontsize=10,
            ha="right",
            va="center",
            zorder=10,
            bbox=dict(
                facecolor="w",
                alpha=1.0,
                edgecolor="gray",
                boxstyle="round,pad=0.5",
            ),
        )

    #
    # right y-axis
    #

    ax.scatter(
        x=[3] * n,
        y=yright,
        s=right_sizes,
        c=right_colors,
        zorder=10,
        linewidths=1,
        edgecolors="k",
    )

    for idx, text in enumerate(matrix.columns):
        ax.plot([3.0, 3.3], [yright[idx], yright[idx]], "-", c="grey")

    for idx, text in enumerate(matrix.columns):
        ax.text(
            3.3,
            yright[idx],
            text,
            fontsize=10,
            ha="left",
            va="center",
            bbox=dict(
                facecolor="w",
                alpha=1.0,
                edgecolor="gray",
                boxstyle="round,pad=0.5",
            ),
            zorder=11,
        )

    #
    # Figure size
    #
    # expand_ax_limits(ax)
    ax.invert_yaxis()
    ax.axis("off")
    fig.set_tight_layout(True)

    return fig
