"""
Co-occurrence Matrix / Topics Comparison Network
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_matrix_topics_comparison_network.png"
>>> co_occurrence_matrix_topics_comparison_network(
...     'block-chain',
...     'fintech',
...     'author_keywords', 
...      min_occ=5,
...      directory=directory,
... ).savefig(file_name)

.. image:: images/co_occurrence_matrix_topics_comparison_network.png
    :width: 700px
    :align: center




"""

import networkx as nx

from .co_occurrence_matrix import co_occurrence_matrix
from .network_plot import network_plot


def co_occurrence_matrix_topics_comparison_network(
    topic_a,
    topic_b,
    column,
    min_occ=1,
    directory="./",
    figsize=(7, 7),
    k=0.20,
    iterations=50,
    max_labels=50,
    plot=True,
):

    matrix = co_occurrence_matrix(
        column,
        min_occ=min_occ,
        max_occ=None,
        normalization=None,
        scheme=None,
        directory=directory,
    )

    matrix = matrix.iloc[
        (matrix.iloc[:, matrix.columns.get_level_values(0) == topic_a].values > 0)
        | (matrix.iloc[:, matrix.columns.get_level_values(0) == topic_b].values > 0),
        :,
    ]
    matrix = matrix.transpose()
    matrix = matrix.iloc[
        (matrix.iloc[:, matrix.columns.get_level_values(0) == topic_a].values > 0)
        | (matrix.iloc[:, matrix.columns.get_level_values(0) == topic_b].values > 0),
        :,
    ]

    columns = matrix.columns.get_level_values(0)
    indexes = matrix.index.get_level_values(0)

    for i_row in range(len(matrix.index)):
        for i_col in range(len(matrix.columns)):
            if i_row == i_col:
                continue
            if columns[i_col] == topic_a:
                continue
            if columns[i_col] == topic_b:
                continue
            if indexes[i_row] == topic_a:
                continue
            if indexes[i_row] == topic_b:
                continue
            matrix.iloc[i_row, i_col] = 0

    if plot is False:
        return matrix

    if plot is False:
        return matrix

    # -------------------------------------------------------------------------
    matrix.sort_index(axis="columns", level=[0, 1, 2], inplace=True)
    matrix.sort_index(axis="index", level=[0, 1, 2], inplace=True)

    # -------------------------------------------------------------------------
    names = matrix.columns.get_level_values(0)
    n_cols = matrix.shape[1]
    edges = []
    for i_row in range(1, n_cols):
        for i_col in range(0, i_row):
            if matrix.iloc[i_row, i_col] > 0:
                edges.append(
                    {
                        "source": names[i_row],
                        "target": names[i_col],
                        "weight": matrix.iloc[i_row, i_col],
                    }
                )

    # -------------------------------------------------------------------------
    size = {name: 0 for name in names}
    for edge in edges:
        size[edge["source"]] += edge["weight"]
        size[edge["target"]] += edge["weight"]
    nodes = [
        (
            name,
            dict(
                size=size[name],
                group=(1 if name == topic_a else (2 if name == topic_b else 0)),
            ),
        )
        for name in size.keys()
    ]

    # -------------------------------------------------------------------------
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(
        [(edge["source"], edge["target"], edge["weight"]) for edge in edges]
    )

    network_ = {
        "nodes": nodes,
        "edges": edges,
        "G": G,
    }

    return network_plot(
        network_,
        figsize=figsize,
        k=k,
        iterations=iterations,
        max_labels=max_labels,
    )
