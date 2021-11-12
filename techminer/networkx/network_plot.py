"""
Networkx plot

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cdlib import algorithms

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
    nodes,
    edges,
    figsize=(7, 7),
    k=0.20,
    iterations=50,
    max_labels=50,
):
    """

    nodes: pandas.DataFrame
    - name
    - group
    - size

    edges: pandas.DataFrame
    - source
    - target
    - value

    """

    # creates a networkx graph
    G = nx.Graph()

    # add nodes
    for _, row in nodes.iterrows():
        G.add_node(
            row["name"],
            group=row["group"],
            size=row["size"],
        )

    # add edges
    for _, row in edges.iterrows():
        G.add_edge(
            row["source"],
            row["target"],
            weight=row["value"],
            color=group_colors[row["group"]],
            alpha=0.5,
        )

    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    options = {
        "width": 1,
        "with_labels": False,
        "font_size": 7,
        "font_weight": "regular",
        "alpha": 0.7,
    }

    colors = [group_colors[node[1]["group"]] for node in G.nodes.data()]
    sizes = [node[1]["size"] for node in G.nodes.data()]
    edge_colors = nx.get_edge_attributes(G, "color").values()
    edge_colors = ["silver"] * len(edge_colors)

    pos = nx.spring_layout(G, k=k, iterations=iterations)

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

    x_points_marked = [
        pos[label][0]
        for label in nodes.sort_values("size", ascending=False).name.head(max_labels)
    ]
    y_points_marked = [
        pos[label][1]
        for label in nodes.sort_values("size", ascending=False).name.head(max_labels)
    ]

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

    for label in nodes.sort_values("size", ascending=False).name.head(max_labels):

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
