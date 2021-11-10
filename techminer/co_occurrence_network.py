"""
Co-occurrence netowrk
===============================================================================

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import networkx as nx

from .networkx import network_clustering, network_plot

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


class _CoOccurrenceNetwork:
    def __init__(self, matrix, algorithm="louvain"):
        self.matrix = matrix.copy()
        self.algorithm = algorithm

        self.matrix = self.matrix.astype(float)

        # checks if matris is ordered
        self.matrix.sort_index(axis="columns", level=[0, 1, 2], inplace=True)
        self.matrix.sort_index(axis="index", level=[0, 1, 2], inplace=True)

        #

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


def co_occurrence_network(matrix, algorithm="louvain"):

    return _CoOccurrenceNetwork(matrix, algorithm=algorithm)
