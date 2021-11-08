"""
Auto-correlation --- map
===============================================================================

"""
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from ._corr_map import corr_map
from .tf_matrix import tf_matrix
from .utils import adds_counters_to_axis
from .utils.io import load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def auto_corr_map(
    auto_corr_matrix,
    threshold=0.5,
    cmap="Greys",
    n_links=None,
    nx_iterations=200,
    nx_k=1e-3,
    nx_scale=1.0,
    nx_random_state=None,
    figsize=(6, 6),
    num_terms=None,
):
    # computos
    matrix = auto_corr_matrix.copy()

    # Networkx
    fig = plt.Figure(figsize=figsize)
    cmap = plt.cm.get_cmap(cmap)
    ax = fig.subplots()
    G = nx.Graph(ax=ax)
    G.clear()

    np.fill_diagonal(matrix.values, 0.0)
    matrix = pd.melt(
        matrix,
        var_name="to",
        value_name="value",
        ignore_index=False,
    )
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={matrix.columns[0]: "from"})

    matrix = matrix.assign(width=matrix.value.map(lambda x: 2 if x > 0.75 else 1))
    matrix = matrix.assign(
        style=matrix.value.map(
            lambda x: "-" if x > 0.50 else ("--" if x > 0.5 else ":")
        )
    )

    ## node sizes
    node_props = matrix[["from", "#nd", "#tc"]]
    node_props = node_props.drop_duplicates()
    min_size, max_size = float(node_props["#nd"].min()), float(node_props["#nd"].max())

    if min_size == max_size:
        node_props = node_props.assign(node_size=1000)
    else:
        node_props = node_props.assign(
            node_size=node_props["#nd"].map(
                lambda x: 100 + int(800 * (x - min_size) / (max_size - min_size))
            )
        )

    ## node colors
    min_tc, max_tc = float(node_props["#tc"].min()), float(node_props["#tc"].max())

    if min_tc == max_tc:
        node_props = node_props.assign(node_color=0.5)
    else:
        node_props = node_props.assign(
            node_color=node_props["#tc"].map(
                lambda x: cmap(0.2 + 0.60 * (x - min_tc) / (max_tc - min_tc))
            )
        )

    ## edges
    edges = matrix.copy()
    edges = edges[edges.value >= threshold]
    if n_links is not None:
        edges = edges.head(n_links)
    edgelist = [(a, b) for a, b in zip(edges["from"], edges.to)]

    ## Add nodes
    terms = matrix.to.copy()
    terms = terms.drop_duplicates()
    G.add_nodes_from(terms.tolist())

    ## node positions
    pos = nx.spring_layout(
        G,
        iterations=nx_iterations,
        k=nx_k,
        scale=nx_scale,
        seed=nx_random_state,
    )

    ## node edges
    nx.draw_networkx_edges(
        G,
        pos=pos,
        ax=ax,
        node_size=1,
        edge_color="k",
        edgelist=edgelist,
        width=matrix.width,
    )

    ## Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        ax=ax,
        nodelist=node_props["from"].tolist(),
        node_size=node_props["node_size"].tolist(),
        node_color=node_props["node_color"].tolist(),
        node_shape="o",
        edgecolors="k",
        linewidths=1,
    )

    ## Node labels
    x_mean = sum([pos[label][0] for label in terms]) / len(terms)
    y_mean = sum([pos[label][1] for label in terms]) / len(terms)

    if num_terms is not None:
        terms = terms.head(num_terms)

    for term in terms:
        x_point, y_point = pos[term]
        ha = "left" if x_point > x_mean else "right"
        va = "top" if y_point > y_mean else "bottom"

        ax.text(
            x_point,
            y_point,
            s=term,
            fontsize=6,
            bbox=dict(
                facecolor="w",
                alpha=1.0,
                edgecolor="gray",
                boxstyle="round,pad=0.5",
            ),
            horizontalalignment=ha,
            verticalalignment=va,
        )

    ax.axis("off")
    return fig
