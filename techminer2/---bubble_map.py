import math

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

COLORS = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
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
]

COLORS += COLORS * 4

#
# Check in order:
#   - latent semantic analysis module
#
#
def _get_quadrant(x, y, x_axis_at, y_axis_at):
    if x >= y_axis_at and y >= x_axis_at:
        return 0
    if x < y_axis_at and y >= x_axis_at:
        return 1
    if x < y_axis_at and y < x_axis_at:
        return 2
    return 3


def bubble_map(
    node_x,
    node_y,
    node_clusters,
    node_texts,
    node_sizes,
    x_axis_at,
    y_axis_at,
    color_scheme,
    xlabel,
    ylabel,
    figsize,
    fontsize,
):

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.yaxis.set_ticks_position("both")
    ax.xaxis.set_ticks_position("both")

    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.tick_params(which="major", color="k", length=5)
    ax.tick_params(which="minor", color="k", length=2)

    # quadrants
    quadrants = [
        _get_quadrant(x_, y_, x_axis_at, y_axis_at) for x_, y_ in zip(node_x, node_y)
    ]

    # Size of node proportional to number of documents
    max_node_size = max(node_sizes)
    min_node_size = min(node_sizes)
    if max_node_size == min_node_size:
        node_sizes = [1000 for _ in node_sizes]
    else:
        node_sizes = [
            400 + 5000 * (i - min_node_size) / (max_node_size - min_node_size)
            for i in node_sizes
        ]

    # Select node colors
    node_colors = None
    if color_scheme == "4q":
        node_colors = [COLORS[q] for q in quadrants]

    if color_scheme == "clusters":
        node_colors = [COLORS[i] for i in node_clusters]

    if node_colors is None:
        cmap = plt.cm.get_cmap(color_scheme)
        node_colors = [
            cmap(0.3 + 0.70 * (i - min_node_size) / (max_node_size - min_node_size))
            for i in node_sizes
        ]

    # plot bubbles
    ax.scatter(
        node_x,
        node_y,
        marker="o",
        s=node_sizes,
        c=node_colors,
        alpha=0.4,
        linewidths=1,
    )

    # plot centers as black dots
    ax.scatter(
        node_x,
        node_y,
        marker="o",
        s=20,
        c="k",
        alpha=1.0,
    )

    # plot node labels
    xlim = ax.get_xlim()
    #  ylim = ax.get_ylim()

    factor = 0.1

    for x_, y_, keyword, quadrant, color in zip(
        node_x, node_y, node_texts, quadrants, node_colors
    ):

        xlim = ax.get_xlim()

        ha = {
            0: "left",
            1: "right",
            2: "right",
            3: "left",
        }[quadrant]

        va = {
            0: "center",
            1: "center",
            2: "center",
            3: "center",
        }[quadrant]

        x_ = x_ - y_axis_at
        y_ = y_ - x_axis_at

        delta = factor * (xlim[1] - xlim[0])
        angle = math.atan(math.fabs(y_ / x_))
        radious = math.sqrt(x_ ** 2 + y_ ** 2) + delta
        x_label = math.copysign(radious * math.cos(angle), x_) + y_axis_at
        y_label = math.copysign(radious * math.sin(angle), y_) + x_axis_at

        ax.text(
            x_label,
            y_label,
            # s=" ".join(keyword.split(" ")[:-1]),
            s=keyword,
            fontsize=fontsize,
            bbox=dict(
                facecolor="w",
                alpha=0.7,
                boxstyle="round,pad=0.5",
                edgecolor="lightgray",
            ),
            horizontalalignment=ha,
            verticalalignment=va,
            c=color,
        )

        ax.plot(
            [x_ + y_axis_at, x_label],
            [y_ + x_axis_at, y_label],
            lw=1,
            ls="-",
            c="k",
            zorder=-1,
        )

    ## generic

    ax.axhline(
        y=x_axis_at,
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=-1,
    )
    ax.axvline(
        x=y_axis_at,
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=-1,
    )

    for side in ["top", "right", "bottom", "left"]:
        ax.spines[side].set_visible(False)

    ## adjust figure size
    ax.set_aspect("auto")
    fig.set_tight_layout(True)

    return fig
