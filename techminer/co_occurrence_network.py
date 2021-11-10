"""
Co-occurrence netowrk analysis
===============================================================================

TODO: pagerank

This module is eqivalent to:

* Bibliometrix' Conceptual Structure/Co-occurrence Network.
    - Network map
    - Table with (node, cluster, betweenness, closeness, pagerank)
    - Degree plot

* VantagePoint Co-occurrence map (newtork without clustering).

* T-LAB Co-occurrence analysis

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').plot()

.. image:: images/co_occurrence_network.png
    :width: 700px
    :align: center


>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').table().head()
                      node  num_documents  global_citations  cluster  \\
0  artificial intelligence             48               238        2   
1                  banking             38               258        0   
2                    banks             16                96        0   
3                 big data             30               163        2   
4                  bitcoin             39               236        0   
-
   betweenness  closeness  
0     0.020965   0.744186  
1     0.020708   0.744186  
2     0.002279   0.603774  
3     0.010653   0.695652  
4     0.004572   0.640000


>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').heat_map()

.. image:: images/co_occurrence_heat_map.png
    :width: 700px
    :align: center


>>> co_occurrence_network(co_occurrence_matrix(directory, 'author_keywords', min_occ=15), 'louvain').node_degrees()

.. image:: images/co_occurrence_degrees.png
    :width: 700px
    :align: center


"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import networkx as nx

from .networkx import (
    betweenness_centrality,
    closeness_centrality,
    network_clustering,
    network_plot,
    node_degrees_plot,
)

cluster_colors = [
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


class Co_occurrence_network:
    def __init__(self, matrix, algorithm="louvain"):
        self.matrix = matrix.copy()
        self.algorithm = algorithm

        self.matrix = self.matrix.astype(float)

        # ---< for auto-correlation matrix >---
        self.matrix = self.matrix.applymap(np.abs)

        # checks if matris is ordered
        self.matrix.sort_index(axis="columns", level=[0, 1, 2], inplace=True)
        self.matrix.sort_index(axis="index", level=[0, 1, 2], inplace=True)

        self._make_nodes()
        self._make_edges()
        self._clustering()

    def _make_nodes(self):

        nodes = pd.DataFrame({"name": self.matrix.columns.get_level_values(0)})
        nodes["size"] = self.matrix.values.diagonal()
        max_size = nodes["size"].max()
        nodes["size"] = nodes["size"] / max_size
        max_size = 1.0
        min_size = nodes["size"].min()
        nodes["size"] = 100 + 1400 * (nodes["size"] - min_size) / (max_size - min_size)
        self.nodes_ = nodes.copy()

    def _make_edges(self):

        matrix = self.matrix.copy()
        np.fill_diagonal(matrix.values, 0.0)
        n_cols = len(matrix.columns)
        for i in range(n_cols):
            for j in range(i, n_cols):
                matrix.iloc[i, j] = 0.0
        matrix = pd.melt(
            matrix,
            var_name="target",
            value_name="value",
            ignore_index=False,
        )
        matrix = matrix[matrix.value > 0]
        matrix = matrix.reset_index()
        matrix = matrix.rename(columns={matrix.columns[0]: "source"})

        # proportional node widths
        matrix["value"] = matrix.value / matrix.value.max() * 4

        matrix = matrix[["source", "target", "value"]]
        self.edges_ = matrix.copy()

    def _clustering(self):

        self.nodes_, self.edges_ = network_clustering(
            self.nodes_,
            self.edges_,
            self.algorithm,
        )

    def plot(self, figsize=(7, 7), k=0.2, iterations=50):

        return network_plot(
            self.nodes_,
            self.edges_,
            figsize=figsize,
            k=k,
            iterations=iterations,
        )

    def node_degrees(self, figsize=(6, 6)):

        return node_degrees_plot(self.nodes_, self.edges_, figsize)

    def table(self):

        table_ = pd.DataFrame(
            {
                "node": self.matrix.index.get_level_values(0),
                "num_documents": self.matrix.index.get_level_values(1),
                "global_citations": self.matrix.index.get_level_values(2),
            }
        )

        node2cluster = dict(zip(self.nodes_.name, self.nodes_.group))
        table_["cluster"] = table_.node.map(node2cluster)

        betweenness = betweenness_centrality(self.nodes_, self.edges_)
        closeness = closeness_centrality(self.nodes_, self.edges_)

        table_["betweenness"] = table_.node.map(betweenness)
        table_["closeness"] = table_.node.map(closeness)

        return table_

    def heat_map(self, cmap="Reds", figsize=(6, 6)):

        matrix = self.matrix.copy()

        matrix.columns = matrix.columns.get_level_values(0)
        matrix.index = matrix.index.get_level_values(0)

        fig = plt.figure(figsize=figsize)
        ax = fig.subplots()

        ax = sns.heatmap(
            matrix,
            ax=ax,
            cmap=cmap,
            square=True,
            linewidths=0.5,
            cbar=False,
            linecolor="gray",
        )

        fig.set_tight_layout(True)

        return fig


def co_occurrence_network(matrix, algorithm="louvain"):

    return Co_occurrence_network(matrix, algorithm=algorithm)
