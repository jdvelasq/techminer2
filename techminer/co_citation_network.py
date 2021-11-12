"""
Co-citation network
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> co_citation_network(directory)


.. image:: images/co_citation_network.png
    :width: 700px
    :align: center

"""

import numpy as np
import pandas as pd

from .networkx import (
    betweenness_centrality,
    closeness_centrality,
    network_clustering,
    network_plot,
    node_degrees_plot,
)
from .utils import load_filtered_documents

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


class Co_citation_network_documents:
    def __init__(self, directory, algorithm="louvain", min_edges=2):

        self.documents = load_filtered_documents(directory)
        self.algorithm = algorithm
        self.min_edges = min_edges

        # ---< processings >-----------------------------------------------------
        self._make_edges()
        self._make_nodes()
        self._remove_edges()
        self._clustering()

    def _make_edges(self):

        self.documents["authors"] = self.documents.authors.apply(
            lambda x: "[Anonymous]" if pd.isna(x) else x
        )
        self.documents = self.documents.assign(
            author_year=self.documents.authors.apply(lambda x: x.split("; ")[0])
            + ", "
            + self.documents.pub_year.astype(str)
        )
        document_id2author_year = dict(
            zip(self.documents.document_id, self.documents.author_year)
        )

        # remove documents without co-citations
        self.edges_ = self.documents[["author_year", "local_references"]]
        self.edges_ = self.edges_.dropna()
        self.edges_["local_references"] = self.edges_.local_references.apply(
            lambda x: x.split("; ")
        )
        self.edges_ = self.edges_.explode("local_references")
        self.edges_["local_references"] = self.edges_.local_references.map(
            document_id2author_year
        )

        self.edges_ = self.edges_.rename(
            columns={"author_year": "source", "local_references": "target"}
        )

        different_nodes = self.edges_.source != self.edges_.target
        self.edges_ = self.edges_[different_nodes]

        self.edges_ = self.edges_.assign(value=1)

    def _make_nodes(self):
        nodes = pd.concat(
            [self.edges_.source, self.edges_.target],
        ).drop_duplicates()

        # counts the number of links
        edges = self.edges_.copy()
        edges = edges.rename(columns={"source": "target", "target": "source"})
        edges = pd.concat([edges, self.edges_])
        edges = edges.drop_duplicates()

        num_links = edges.groupby("source").size().reset_index(name="size")
        num_links = dict(zip(num_links.source, num_links["size"]))

        self.nodes_ = pd.DataFrame(nodes, columns=["name"])
        self.nodes_["node_size"] = self.nodes_.name.map(num_links)

    def _clustering(self):

        nodes = self.nodes_.copy()
        nodes["size"] = 50 + 950 * self.nodes_.node_size / self.nodes_.node_size.max()

        self.nodes_, self.edges_ = network_clustering(
            nodes,
            self.edges_,
            self.algorithm,
        )

    def _remove_edges(self):

        # remove edges with less than min_edges
        self.nodes_ = self.nodes_[self.nodes_["node_size"] >= self.min_edges]

        # remove links to to removed nodes
        exists = (self.edges_.source.isin(self.nodes_.name)) & (
            self.edges_.target.isin(self.nodes_.name)
        )
        self.edges_ = self.edges_[exists]

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


def co_citation_network(directory, column=None, algorithm="louvain", min_edges=2):

    if column is None:
        return Co_citation_network_documents(
            directory, algorithm=algorithm, min_edges=min_edges
        )
