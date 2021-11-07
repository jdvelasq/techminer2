"""
Auto-correlation map
===============================================================================

"""
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from ._corr_map import corr_map
from .auto_corr_matrix import auto_corr_matrix
from .tf_matrix import tf_matrix
from .utils import adds_counters_to_axis
from .utils.io import load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def auto_corr_map(
    directory,
    column,
    method="pearson",
    min_occ=1,
    max_occ=None,
    scheme=None,
    sep="; ",
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

    ## Networkx
    fig = plt.Figure(figsize=figsize)
    cmap = plt.cm.get_cmap(cmap)
    ax = fig.subplots()
    G = nx.Graph(ax=ax)
    G.clear()

    ## computos
    matrix = auto_corr_matrix(
        directory=directory,
        column=column,
        method=method,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        sep=sep,
    )

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

    # for label, size in zip(terms, column_node_sizes + index_node_sizes):
    #     x_point, y_point = pos[label]
    #     delta_x = 0.05 * (xlim[1] - xlim[0]) + 0.001 * size / 300 * (
    #         xlim[1] - xlim[0]
    #     )
    #     delta_y = 0.05 * (ylim[1] - ylim[0]) + 0.001 * size / 300 * (
    #         ylim[1] - ylim[0]
    #     )

    #     delta_x = delta_x if x_point > x_mean else -delta_x
    #     delta_y = delta_y if y_point > y_mean else -delta_y

    #     ax.text(

    #
    #
    ax.axis("off")
    return fig

    # X = self.X_

    # ## Data preparation
    # terms = X.columns.tolist() + X.index.tolist()

    # node_sizes = counters_to_node_sizes(x=terms)
    # column_node_sizes = node_sizes[: len(X.index)]
    # index_node_sizes = node_sizes[len(X.index) :]

    # node_colors = counters_to_node_colors(x=terms, cmap=lambda w: w)
    # column_node_colors = node_colors[: len(X.index)]
    # index_node_colors = node_colors[len(X.index) :]

    # cmap = pyplot.cm.get_cmap(self.colormap_col)
    # cmap_by = pyplot.cm.get_cmap(self.colormap_by)

    # index_node_colors = [cmap_by(t) for t in index_node_colors]
    # column_node_colors = [cmap(t) for t in column_node_colors]

    # # if self.layout == "Spring":
    # #     pos = nx.spring_layout(G, iterations=self.nx_iterations)
    # # else:
    # #     pos = {
    # #         "Circular": nx.circular_layout,
    # #         "Kamada Kawai": nx.kamada_kawai_layout,
    # #         "Planar": nx.planar_layout,
    # #         "Random": nx.random_layout,
    # #         "Spectral": nx.spectral_layout,
    # #         "Spring": nx.spring_layout,
    # #         "Shell": nx.shell_layout,
    # #     }[self.layout](G)

    # ## links
    # m = X.stack().to_frame().reset_index()
    # m.columns = ["from_", "to_", "link_"]
    # m = m[m.link_ > 0.0]
    # m = m.reset_index(drop=True)

    # max_width = m.link_.max()

    # for idx in range(len(m)):

    #     edge = [(m.from_[idx], m.to_[idx])]
    #     width = 0.1 + 2.9 * m.link_[idx] / max_width
    #     nx.draw_networkx_edges(
    #         G,
    #         pos=pos,
    #         ax=ax,
    #         node_size=1,
    #         #  with_labels=False,
    #         edge_color="k",
    #         edgelist=edge,
    #         width=width,
    #     )

    # #
    # # Draw column nodes
    # #
    # nx.draw_networkx_nodes(
    #     G,
    #     pos,
    #     ax=ax,
    #     #  edge_color="k",
    #     nodelist=X.columns.tolist(),
    #     node_size=column_node_sizes,
    #     node_color=column_node_colors,
    #     node_shape="o",
    #     edgecolors="k",
    #     linewidths=1,
    # )

    # #
    # # Draw index nodes
    # #
    # nx.draw_networkx_nodes(
    #     G,
    #     pos,
    #     ax=ax,
    #     #  edge_color="k",
    #     nodelist=X.index.tolist(),
    #     node_size=index_node_sizes,
    #     node_color=index_node_colors,
    #     node_shape="o",
    #     edgecolors="k",
    #     linewidths=1,
    # )

    # node_sizes = column_node_sizes + index_node_sizes

    # xlim = ax.get_xlim()
    # ylim = ax.get_ylim()

    # x_points = [pos[label][0] for label in terms]
    # y_points = [pos[label][1] for label in terms]
    # x_mean = sum(x_points) / len(x_points)
    # y_mean = sum(y_points) / len(y_points)

    # for label, size in zip(terms, column_node_sizes + index_node_sizes):
    #     x_point, y_point = pos[label]
    #     delta_x = 0.05 * (xlim[1] - xlim[0]) + 0.001 * size / 300 * (
    #         xlim[1] - xlim[0]
    #     )
    #     delta_y = 0.05 * (ylim[1] - ylim[0]) + 0.001 * size / 300 * (
    #         ylim[1] - ylim[0]
    #     )
    #     ha = "left" if x_point > x_mean else "right"
    #     va = "top" if y_point > y_mean else "bottom"
    #     delta_x = delta_x if x_point > x_mean else -delta_x
    #     delta_y = delta_y if y_point > y_mean else -delta_y

    #     ax.text(
    #         x_point + delta_x,
    #         y_point + delta_y,
    #         s=label,
    #         fontsize=10,
    #         bbox=dict(
    #             facecolor="w",
    #             alpha=1.0,
    #             edgecolor="gray",
    #             boxstyle="round,pad=0.5",
    #         ),
    #         horizontalalignment=ha,
    #         verticalalignment=va,
    #     )

    # #  ax_text_node_labels(ax=ax, labels=terms, dict_pos=pos, node_sizes=node_sizes)
    # expand_ax_limits(ax)
    # #  ax.set_aspect("equal")
    # ax.axis("off")
    # set_spines_invisible(ax)
    # return fig
