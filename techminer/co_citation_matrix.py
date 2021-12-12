"""
Co-citation Matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> matrix = co_citation_matrix(directory=directory)
>>> matrix.head()
                   1989-0000 2000-0000 2003-0002  ... 2020-0031 2020-0131 2020-0225
                       25830     9760      16860  ...     76        26        15   
                          14        7         9   ...        11        11        6 
1989-0000 25830 14      14.0       4.0       5.0  ...       1.0       0.0       0.0
2000-0000 9760  7        4.0       7.0       3.0  ...       1.0       0.0       1.0
2003-0002 16860 9        5.0       3.0       9.0  ...       2.0       1.0       1.0
2009-0013 876   9        4.0       1.0       4.0  ...       0.0       0.0       0.0
2013-0009 553   6        0.0       0.0       0.0  ...       1.0       0.0       0.0
<BLANKLINE>
[5 rows x 50 columns]


"""
from os.path import join

import numpy as np
import pandas as pd


def co_citation_matrix(top_n=50, directory="./"):

    # ---< obtains the most local cited references >-------------------------------------
    references = pd.read_csv(join(directory, "references.csv"))
    references = references.sort_values("local_citations", ascending=False)
    record_no = references.record_no
    record_no = record_no.head(top_n)

    # ---< obtains the document-reference table >----------------------------------------
    cited_references_table = pd.read_csv(join(directory, "cited_references_table.csv"))
    cited_references_table = cited_references_table[
        cited_references_table.cited_id.isin(record_no)
    ]

    # ---< document-reference table >----------------------------------------------------
    cited_references_table["n_citations"] = 1
    ## to check >>>
    cited_references_table = cited_references_table.drop_duplicates()
    ## <<<
    document_reference = cited_references_table.pivot(
        index="citing_id", columns="cited_id", values="n_citations"
    ).fillna(0)

    matrix_values = np.matmul(
        document_reference.transpose().values, document_reference.values
    )

    # ---< index based on citations >----------------------------------------------------
    record_no2global_citations = dict(
        zip(references.record_no, references.global_citations)
    )
    record_no2local_citations = dict(
        zip(references.record_no, references.local_citations)
    )
    global_citations = [
        record_no2global_citations[record_no]
        for record_no in document_reference.columns
    ]
    local_citations = [
        record_no2local_citations[record_no] for record_no in document_reference.columns
    ]
    new_index = pd.MultiIndex.from_tuples(
        [
            (record_no, global_citation, local_citation)
            for record_no, global_citation, local_citation in zip(
                document_reference.columns, global_citations, local_citations
            )
        ],
    )

    # -----------------------------------------------------------------------------------

    co_occ_matrix = pd.DataFrame(
        matrix_values,
        columns=new_index,
        index=new_index,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    co_occ_matrix = co_occ_matrix.loc[:, (co_occ_matrix != 0).any(axis=0)]
    co_occ_matrix = co_occ_matrix.loc[(co_occ_matrix != 0).any(axis=1), :]

    return co_occ_matrix


# import numpy as np
# import pandas as pd

# from .networkx import (
#     betweenness_centrality,
#     closeness_centrality,
#     network_clustering,
#     network_plot,
#     node_degrees_plot,
# )
# from .utils import load_filtered_documents

# cluster_colors = [
#     "tab:blue",
#     "tab:orange",
#     "tab:green",
#     "tab:red",
#     "tab:purple",
#     "tab:brown",
#     "tab:pink",
#     "tab:gray",
#     "tab:olive",
#     "tab:cyan",
#     "cornflowerblue",
#     "lightsalmon",
#     "limegreen",
#     "tomato",
#     "mediumvioletred",
#     "darkgoldenrod",
#     "lightcoral",
#     "silver",
#     "darkkhaki",
#     "skyblue",
# ] * 5


# class Co_citation_network_documents:
#     def __init__(self, directory, algorithm="louvain", min_edges=2):

#         self.documents = load_filtered_documents(directory)
#         self.algorithm = algorithm
#         self.min_edges = min_edges

#         # ---< processings >-----------------------------------------------------
#         self._make_node_id()
#         self._make_edges()
#         self._make_nodes()
#         self._remove_edges()
#         self._clustering()

#     def _make_node_id(self):

#         self.documents["authors"] = self.documents.authors.apply(
#             lambda x: "[Anonymous]" if pd.isna(x) else x
#         )

#         self.documents = self.documents.assign(
#             author_year=self.documents.authors.apply(lambda x: x.split("; ")[0])
#             + ", "
#             + self.documents.pub_year.astype(str)
#         )

#         author_year = self.documents[["author_year", "record_no"]]
#         author_year = author_year.groupby("author_year", as_index=False).agg(
#             {"record_no": list}
#         )
#         author_year = author_year.assign(length=author_year.record_no.apply(len))
#         author_year = author_year[author_year.length > 1]
#         author_year = author_year.assign(
#             record_no=author_year.record_no.apply(lambda x: x[1:])
#         )
#         author_year = author_year.explode("record_no")
#         author_year = author_year.assign(
#             rn=author_year.groupby("record_no").cumcount() + 1
#         )
#         author_year = author_year.assign(
#             author_year=author_year.author_year + "/" + author_year.rn.astype(str)
#         )
#         author_year = author_year.set_index("record_no")
#         self.documents.index = self.documents.record_no
#         self.documents.loc[author_year.index, "author_year"] = author_year.author_year

#     def _make_edges(self):

#         # remove documents without co-citations
#         self.edges_ = self.documents[["author_year", "local_references"]]
#         self.edges_ = self.edges_.dropna()
#         self.edges_["local_references"] = self.edges_.local_references.apply(
#             lambda x: x.split("; ")
#         )
#         self.edges_ = self.edges_.explode("local_references")

#         document_id2author_year = dict(
#             zip(self.documents.record_no, self.documents.author_year)
#         )

#         self.edges_["local_references"] = self.edges_.local_references.map(
#             document_id2author_year
#         )

#         self.edges_ = self.edges_.rename(
#             columns={"author_year": "source", "local_references": "target"}
#         )

#         different_nodes = self.edges_.source != self.edges_.target
#         self.edges_ = self.edges_[different_nodes]

#         self.edges_ = self.edges_.assign(value=1)

#     def _make_nodes(self):
#         nodes = pd.concat(
#             [self.edges_.source, self.edges_.target],
#         ).drop_duplicates()

#         # counts the number of links
#         edges = self.edges_.copy()
#         edges = edges.rename(columns={"source": "target", "target": "source"})
#         edges = pd.concat([edges, self.edges_])
#         edges = edges.drop_duplicates()

#         num_links = edges.groupby("source").size().reset_index(name="size")
#         num_links = dict(zip(num_links.source, num_links["size"]))

#         self.nodes_ = pd.DataFrame(nodes, columns=["name"])
#         self.nodes_["node_size"] = self.nodes_.name.map(num_links)

#     def _clustering(self):

#         nodes = self.nodes_.copy()
#         nodes["size"] = 50 + 950 * self.nodes_.node_size / self.nodes_.node_size.max()

#         self.nodes_, self.edges_ = network_clustering(
#             nodes,
#             self.edges_,
#             self.algorithm,
#         )

#     def _remove_edges(self):

#         # remove edges with less than min_edges
#         self.nodes_ = self.nodes_[self.nodes_["node_size"] >= self.min_edges]

#         # remove links to to removed nodes
#         exists = (self.edges_.source.isin(self.nodes_.name)) & (
#             self.edges_.target.isin(self.nodes_.name)
#         )
#         self.edges_ = self.edges_[exists]

#     def plot(self, figsize=(7, 7), k=0.2, iterations=50):

#         return network_plot(
#             self.nodes_,
#             self.edges_,
#             figsize=figsize,
#             k=k,
#             iterations=iterations,
#         )

#     def node_degrees(self, figsize=(6, 6)):

#         return node_degrees_plot(self.nodes_, self.edges_, figsize)

#     def table(self):

#         table_ = pd.DataFrame(
#             {
#                 "node": self.matrix.index.get_level_values(0),
#                 "num_documents": self.matrix.index.get_level_values(1),
#                 "global_citations": self.matrix.index.get_level_values(2),
#             }
#         )

#         node2cluster = dict(zip(self.nodes_.name, self.nodes_.group))
#         table_["cluster"] = table_.node.map(node2cluster)

#         betweenness = betweenness_centrality(self.nodes_, self.edges_)
#         closeness = closeness_centrality(self.nodes_, self.edges_)

#         table_["betweenness"] = table_.node.map(betweenness)
#         table_["closeness"] = table_.node.map(closeness)

#         return table_

#     def communities(self):
#         groups = self.nodes_.copy()

#         groups = groups[["name", "node_size", "group"]]
#         groups = groups.sort_values(by=["group", "node_size"], ascending=False)
#         groups["rn"] = groups.groupby("group")["node_size"].cumcount()
#         groups["group"] = groups.group.map(lambda x: f"CLUST_{x}")
#         groups = groups.pivot(index="rn", columns="group", values="name")
#         groups = groups.fillna("")

#         return groups


# def co_citation_network(directory, column=None, algorithm="louvain", min_edges=2):

#     if column is None:
#         return Co_citation_network_documents(
#             directory, algorithm=algorithm, min_edges=min_edges
#         )
