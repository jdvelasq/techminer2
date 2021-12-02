import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoMinorLocator
from scipy.spatial import ConvexHull

# from techminer.core.sort_axis import sort_axis
# from techminer.plots import expand_ax_limits
# from techminer.plots.set_spines_invisible import set_spines_invisible

_COLORS = [
    "tab:blue",
    "tab:gray",
    "tab:green",
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:orange",
    "tab:pink",
    "tab:olive",
    "tab:cyan",
    "cornflowerblue",
    "lightsalmon",
    "limegreen",
    "tomato",
    "mediumvioletred",
    "darkgoldenrod",
    "lightcoral",
    "silver",
    "darkkhaki",
    "skyblue",
    "dodgerblue",
    "orangered",
    "turquoise",
    "crimson",
    "violet",
    "goldenrod",
    "thistle",
    "grey",
    "yellowgreen",
    "lightcyan",
] * 3


def _get_quadrant(x, y, x_axis_at, y_axis_at):
    if x >= x_axis_at and y >= y_axis_at:
        return 0
    if x < x_axis_at and y >= y_axis_at:
        return 1
    if x < x_axis_at and y < y_axis_at:
        return 2
    return 3


def _encircle(x, y, ax, **kw):
    p = np.c_[x, y]
    hull = ConvexHull(p, qhull_options="QJ")
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)


def conceptual_structure_map(words_by_cluster, top_n, figsize):

    # Creates the plot in memory
    matplotlib.rc("font", size=9)
    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.yaxis.set_ticks_position("both")
    ax.xaxis.set_ticks_position("both")

    # Plot the points of each cluster
    factor = 0.005
    n_clusters = len(set(words_by_cluster.Cluster))
    for i_cluster in range(n_clusters):

        words = words_by_cluster[words_by_cluster.Cluster == i_cluster].copy()
        words.sort_index(axis="index", level=1, ascending=False, inplace=True)

        x_points = words["Dim-1"]
        y_points = words["Dim-2"]

        ax.scatter(
            x_points,
            y_points,
            marker="o",
            s=10,
            alpha=0.9,
            c=_COLORS[i_cluster],
        )

        if len(words) > 2:
            _encircle(
                x_points, y_points, ax=ax, ec="k", fc=_COLORS[i_cluster], alpha=0.2
            )

        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        for x_, y_, text in zip(
            x_points.head(top_n).tolist(),
            y_points.head(top_n).tolist(),
            words.head(top_n).index.get_level_values(0).tolist(),
        ):

            quadrant = _get_quadrant(x=x_, y=y_, x_axis_at=0, y_axis_at=0)

            delta_x = {
                0: +factor * (xlim[1] - xlim[0]),
                1: -factor * (xlim[1] - xlim[0]),
                2: -factor * (xlim[1] - xlim[0]),
                3: +factor * (xlim[1] - xlim[0]),
            }[quadrant]

            delta_y = {
                0: +factor * (ylim[1] - ylim[0]),
                1: -factor * (ylim[1] - ylim[0]),
                2: -factor * (ylim[1] - ylim[0]),
                3: +factor * (ylim[1] - ylim[0]),
            }[quadrant]

            ha = {
                0: "left",
                1: "right",
                2: "right",
                3: "left",
            }[quadrant]

            va = {
                0: "bottom",
                1: "bottom",
                2: "top",
                3: "top",
            }[quadrant]

            ax.text(
                x_ + delta_x,
                y_ + delta_y,
                s=text,
                fontsize=9,
                color=_COLORS[i_cluster],
                horizontalalignment=ha,
                verticalalignment=va,
            )

    #
    # 3.-- Generic
    #
    ax.axhline(
        y=words_by_cluster[words_by_cluster.columns[0]].mean(),
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=-1,
    )
    ax.axvline(
        x=words_by_cluster[words_by_cluster.columns[1]].mean(),
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=-1,
    )

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="mayor", color="k", length=5)
    ax.tick_params(which="minor", color="k", length=2)

    for spine in ["top", "right", "bottom", "left"]:
        ax.spines[spine].set_color("gray")

    # ax.set_aspect("equal")
    # ax.grid(axis="both", color="gray", linestyle="--", linewidth=0.5)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.text(
        x=xlim[1],
        y=0.01 * (ylim[1] - ylim[0]),
        s="Dim-1",
        fontsize=7,
        color="gray",
        horizontalalignment="right",
        verticalalignment="bottom",
    )
    ax.text(
        x=0.01 * (xlim[1] - xlim[0]),
        y=ylim[1],
        s="Dim-2",
        fontsize=7,
        color="gray",
        horizontalalignment="left",
        verticalalignment="top",
    )

    for side in ["top", "right", "bottom", "left"]:
        ax.spines[side].set_visible(False)

    fig.set_tight_layout(True)

    return fig
