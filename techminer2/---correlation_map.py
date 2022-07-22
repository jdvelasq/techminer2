"""
Correlation Map
===============================================================================

# >>> from techminer2 import *
# >>> directory = "data/regtech/"
# >>> file_name = "sphinx/images/auto_corr_map.png"
# >>> matrix = auto_corr_matrix('authors', min_occ=2, directory=directory)
# >>> correlation_map(matrix).savefig(file_name)

# .. image:: images/auto_corr_map.png
#     :width: 700px
#     :align: center

"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def _get_edges(matrix):

    # build network matrices for plotting with networkx
    matrix = matrix.copy()

    # diag sup = 0
    n_cols = len(matrix.columns)
    for i in range(n_cols):
        for j in range(i, n_cols):
            matrix.iloc[i, j] = 0.0

    # selects lower diagonal of the matrix
    edges = pd.melt(
        matrix,
        var_name="target",
        value_name="value",
        ignore_index=False,
    )
    edges = edges.reset_index()
    edges = edges.rename(columns={edges.columns[0]: "source"})
    edges = edges[edges.value > 0]

    # line width
    edges = edges.assign(weight=edges.value.map(lambda x: 2 if x > 0.75 else 1))

    # line style
    edges = edges.assign(
        style=edges.value.map(
            lambda x: "-" if x >= 0.50 else ("--" if x > 0.25 else ":")
        )
    )

    return edges


def _get_nodes(matrix):

    nodes = [(a, b, c) for a, b, c in matrix.columns]
    nodes = pd.DataFrame(nodes, columns=["name", "num_documents", "global_citations"])

    # node sizes
    nodes = nodes.assign(node_size=nodes.num_documents / nodes.num_documents.max())
    nodes = nodes.assign(node_size=100 + 900 * nodes.node_size)

    # node colors
    nodes = nodes.assign(alpha=nodes.global_citations / nodes.global_citations.max())
    nodes = nodes.assign(alpha=0.2 + 0.6 * nodes.alpha)

    return nodes


def correlation_map(
    correlation_matrix,
    cmap="Greys",
    nx_iterations=200,
    nx_k=1e-3,
    nx_scale=1.0,
    nx_random_state=None,
    figsize=(6, 6),
):

    # computos
    matrix = correlation_matrix.copy()

    nodes = _get_nodes(matrix)
    edges = _get_edges(matrix)

    # Networkx
    fig = plt.Figure(figsize=figsize)
    cmap = plt.cm.get_cmap(cmap)
    ax = fig.subplots()
    G = nx.Graph(ax=ax)
    G.clear()

    # add nodes
    for _, row in nodes.iterrows():
        G.add_node(
            row["name"],
            node_size=row["node_size"],
        )

    # add edges
    for _, row in edges.iterrows():
        G.add_edge(
            row["source"],
            row["target"],
            weight=row["weight"],
            style=row["style"],
        )

    # plot ---------------

    node_sizes = list(nx.get_node_attributes(G, "node_size").values())

    edge_styles = nx.get_edge_attributes(G, "style").values()
    edge_weights = list(nx.get_edge_attributes(G, "weight").values())

    ## node positions
    pos = nx.spring_layout(
        G,
        iterations=nx_iterations,
        k=nx_k,
        scale=nx_scale,
        seed=nx_random_state,
    )

    # draws the network
    nx.draw(
        G,
        with_labels=False,
        font_size=7,
        font_weight="regular",
        node_color="k",
        width=edge_weights,
        # node_color=colors,
        node_size=node_sizes,
        edge_color="grey",
        style=edge_styles,
        alpha=0.6,
        pos=pos,
        ax=ax,
    )

    ax.collections[0].set_edgecolor("k")

    # plot centers as black dots
    x_points = [value[0] for value in pos.values()]
    y_points = [value[1] for value in pos.values()]
    ax.scatter(
        x_points,
        y_points,
        marker="o",
        s=30,
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
    radious = np.sqrt(rx**2 + ry**2)

    for label in nodes.name:

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
