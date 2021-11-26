"""
Co-citation network
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_citation_network(directory)


.. image:: images/co_citation_network.png
    :width: 700px
    :align: center

>>> co_citation_network(directory, min_edges=4).communities().head()
group              CLUST_0                  CLUST_1             CLUST_2  \\
rn                                                                        
0              Lee I, 2018        Di Pietro R, 2021   Puschmann T, 2017   
1           Haddad C, 2019           Buchak G, 2018    Rabbani MR, 2020   
2      Dorfleitner G, 2017  Anagnostopoulos I, 2018       Zalan T, 2017   
3          Meiling L, 2021         Jagtiani J, 2018    Rabbani MR, 2021   
4        Mention A-L, 2019       Patwardhan A, 2018  Dospinescu O, 2021   
.
group            CLUST_3             CLUST_4                    CLUST_5  \\
rn                                                                        
0          Leong C, 2017     Milian EZ, 2019            Sangwan V, 2020   
1            Alt R, 2018      Takeda A, 2021              Tasca P, 2016   
2      Mackenzie A, 2015        Iman N, 2020             Adhami S, 2018   
3             Hu Z, 2019      Hasan MM, 2020               Cai CW, 2018   
4         Barbu CM, 2021  Zavolokina L, 2016  Fernandez-Vazquez S, 2019   
.
group         CLUST_6           CLUST_7            CLUST_8            CLUST_9  
rn                                                                             
0      Gomber P, 2017  Suryono RR, 2020  Schueffel P, 2016      Chen MA, 2019  
1      Wojcik D, 2021  Suryono RR, 2021        Kim Y, 2016  Goldstein I, 2019  
2       Gabor D, 2017      Li B/1, 2021     Junger M, 2020      Cheng M, 2020  
3      Ozili PK, 2018      Iman N, 2018      Baber H, 2020    Wexler MN, 2020  
4      Knight E, 2020     Najib M, 2021      Maier E, 2016    Chishti S, 2016

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
        self._make_node_id()
        self._make_edges()
        self._make_nodes()
        self._remove_edges()
        self._clustering()

    def _make_node_id(self):

        self.documents["authors"] = self.documents.authors.apply(
            lambda x: "[Anonymous]" if pd.isna(x) else x
        )

        self.documents = self.documents.assign(
            author_year=self.documents.authors.apply(lambda x: x.split("; ")[0])
            + ", "
            + self.documents.pub_year.astype(str)
        )

        author_year = self.documents[["author_year", "record_no"]]
        author_year = author_year.groupby("author_year", as_index=False).agg(
            {"record_no": list}
        )
        author_year = author_year.assign(length=author_year.record_no.apply(len))
        author_year = author_year[author_year.length > 1]
        author_year = author_year.assign(
            record_no=author_year.record_no.apply(lambda x: x[1:])
        )
        author_year = author_year.explode("record_no")
        author_year = author_year.assign(
            rn=author_year.groupby("record_no").cumcount() + 1
        )
        author_year = author_year.assign(
            author_year=author_year.author_year + "/" + author_year.rn.astype(str)
        )
        author_year = author_year.set_index("record_no")
        self.documents.index = self.documents.record_no
        self.documents.loc[author_year.index, "author_year"] = author_year.author_year

    def _make_edges(self):

        # remove documents without co-citations
        self.edges_ = self.documents[["author_year", "local_references"]]
        self.edges_ = self.edges_.dropna()
        self.edges_["local_references"] = self.edges_.local_references.apply(
            lambda x: x.split("; ")
        )
        self.edges_ = self.edges_.explode("local_references")

        document_id2author_year = dict(
            zip(self.documents.record_no, self.documents.author_year)
        )

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

    def communities(self):
        groups = self.nodes_.copy()

        groups = groups[["name", "node_size", "group"]]
        groups = groups.sort_values(by=["group", "node_size"], ascending=False)
        groups["rn"] = groups.groupby("group")["node_size"].cumcount()
        groups["group"] = groups.group.map(lambda x: f"CLUST_{x}")
        groups = groups.pivot(index="rn", columns="group", values="name")
        groups = groups.fillna("")

        return groups


def co_citation_network(directory, column=None, algorithm="louvain", min_edges=2):

    if column is None:
        return Co_citation_network_documents(
            directory, algorithm=algorithm, min_edges=min_edges
        )
