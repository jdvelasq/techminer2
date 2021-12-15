"""
Network Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/network_plot.png"
>>> coc_matrix = co_occurrence_matrix(column='author_keywords', min_occ=7,directory=directory)
>>> network_ = network(coc_matrix)
>>> network_plot(network_).savefig(file_name)

.. image:: images/network_plot.png
    :width: 700px
    :align: center

"""
from operator import itemgetter

import matplotlib.pyplot as plt
import numpy as np

import networkx as nx

group_colors = [
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
] * 5


def network_plot(
    network,
    figsize=(7, 7),
    k=0.20,
    iterations=50,
    max_labels=50,
):

    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    options = {
        "width": 1,
        "with_labels": False,
        "font_size": 7,
        "font_weight": "regular",
        "alpha": 0.7,
    }

    # --------------------------------------------------------------------------------
    G = network["G"]
    nodes = network["nodes"]
    edges = network["edges"]

    # --------------------------------------------------------------------------------
    pos = nx.spring_layout(G, k=k, iterations=iterations)

    colors = [node[1]["group"] for node in nodes]
    colors = [group_colors[color] for color in colors]

    sizes = [node[1]["size"] for node in G.nodes.data()]
    sizes = [size / max(sizes) for size in sizes]
    max_size = max(sizes)
    min_size = min(sizes)
    if max_size == min_size:
        sizes = [500 for size in sizes]
    else:
        sizes = [
            (size - min_size) / (max_size - min_size) * 1400 + 100 for size in sizes
        ]

    edge_colors = ["silver"] * len(edges)

    # draws the network
    nx.draw(
        G,
        node_color=colors,
        node_size=sizes,
        edge_color=edge_colors,
        pos=pos,
        **options,
    )

    # edge color of nodes
    ax.collections[0].set_edgecolor("k")

    # plot centers as black dots
    x_points = [value[0] for value in pos.values()]
    y_points = [value[1] for value in pos.values()]

    size = [
        (node[0], node[1]["size"], pos[node[0]][0], pos[node[0]][1])
        for node in G.nodes.data()
    ]
    size = sorted(size, key=itemgetter(1), reverse=True)
    x_points_marked = [value[2] for value in size[:max_labels]]
    y_points_marked = [value[3] for value in size[:max_labels]]

    ax.scatter(
        x_points_marked,
        y_points_marked,
        marker="o",
        s=20,
        c="k",
        alpha=1.0,
        zorder=10,
    )

    #  Center of the plot
    x_mean = sum(x_points) / len(x_points)
    y_mean = sum(y_points) / len(y_points)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    factor = 0.05
    rx = factor * (xlim[1] - xlim[0])
    ry = factor * (ylim[1] - ylim[0])
    radious = np.sqrt(rx ** 2 + ry ** 2)

    for label in size[:max_labels]:

        label = label[0]

        x_point, y_point = pos[label]

        x_c = x_point - x_mean
        y_c = y_point - y_mean
        angle = np.arctan(np.abs(y_c / x_c))
        x_label = x_point + np.copysign(radious * np.cos(angle), x_c)
        y_label = y_point + np.copysign(radious * np.sin(angle), y_c)

        ha = "left" if x_point > x_mean else "right"
        va = "center"

        ax.text(
            x_label,
            y_label,
            s=label,
            fontsize=7,
            bbox=dict(
                facecolor="w",
                alpha=1.0,
                edgecolor="gray",
                boxstyle="round,pad=0.5",
            ),
            horizontalalignment=ha,
            verticalalignment=va,
            alpha=0.9,
            zorder=13,
        )

        ax.plot(
            [x_point, x_label],
            [y_point, y_label],
            lw=1,
            ls="-",
            c="k",
            zorder=13,
        )

    fig.set_tight_layout(True)

    return fig
