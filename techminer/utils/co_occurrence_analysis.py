import numpy as np
import pandas as pd

from ..networkx import (
    betweenness_centrality,
    closeness_centrality,
    network_plot,
    node_degrees_plot,
)
from ..plots.bubble_map import bubble_map


class Co_occurrence_analysis:
    def __init__(
        self,
        co_occurrence_matrix,
        clustering_method,
        manifold_method,
    ):
        self.co_occurrence_matrix = co_occurrence_matrix.copy()
        self.co_occurrence_matrix = self.co_occurrence_matrix.astype(float)
        self.clustering_method = clustering_method
        self.manifold_method = manifold_method

    def _sort_co_occurrence_matrix(self):
        self.co_occurrence_matrix.sort_index(
            axis="columns", level=[0, 1, 2], inplace=True
        )
        self.co_occurrence_matrix.sort_index(
            axis="index", level=[0, 1, 2], inplace=True
        )

    def _make_nodes(self):
        nodes = pd.DataFrame(
            {"name": self.co_occurrence_matrix.columns.get_level_values(0)}
        )
        nodes["size"] = self.co_occurrence_matrix.index.get_level_values(1)
        max_size = nodes["size"].max()
        nodes["size"] = nodes["size"] / max_size
        max_size = 1.0
        min_size = nodes["size"].min()
        if max_size == min_size:
            nodes["size"] = 500
        else:
            nodes["size"] = 100 + 1400 * (nodes["size"] - min_size) / (
                max_size - min_size
            )
        self.nodes_ = nodes.copy()

    def _make_edges(self):

        matrix = self.co_occurrence_matrix.copy()
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

    def make_manifold_data(self):
        transformed_matrix = self.manifold_method.fit_transform(
            self.co_occurrence_matrix
        )
        words_by_cluster = pd.DataFrame(
            transformed_matrix,
            columns=["Dim-0", "Dim-1"],
            index=self.co_occurrence_matrix.index,
        )
        words_by_cluster["Cluster"] = self.labels_.tolist()

        self.words_by_cluster_ = words_by_cluster

    def network(self, figsize=(7, 7), k=0.2, iterations=50):

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
                "node": self.co_occurrence_matrix.index.get_level_values(0),
                "num_documents": self.co_occurrence_matrix.index.get_level_values(1),
                "global_citations": self.co_occurrence_matrix.index.get_level_values(2),
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

        cluster_members = self.table().copy()
        cluster_members = cluster_members.sort_values(by=["cluster", "num_documents"])
        cluster_members = cluster_members.assign(
            rn=cluster_members.groupby("cluster").cumcount(())
        )

        num_docs = cluster_members.num_documents.values
        cited_by = cluster_members.global_citations.values
        n_zeros_docs = int(np.log10(max(num_docs))) + 1
        n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

        fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
        text = [
            fmt.format(name, int(nd), int(tc))
            for name, nd, tc in zip(cluster_members.node, num_docs, cited_by)
        ]

        cluster_members = cluster_members.assign(node=text)
        cluster_members = cluster_members.assign(
            cluster=cluster_members.cluster.map(lambda x: "CLUST_{:0d}".format(x))
        )
        cluster_members = cluster_members[["rn", "node", "cluster"]]
        cluster_members = cluster_members.pivot(
            index="rn", columns="cluster", values="node"
        )
        cluster_members = cluster_members.fillna("")
        return cluster_members

    def words_by_cluster(self):
        return self.words_by_cluster_.copy()

    def manifold_map(
        self,
        color_scheme="clusters",
        figsize=(7, 7),
        fontsize=7,
    ):

        return bubble_map(
            node_x=self.words_by_cluster_["Dim-0"],
            node_y=self.words_by_cluster_["Dim-1"],
            node_clusters=self.words_by_cluster_["Cluster"],
            node_texts=self.words_by_cluster_.index.get_level_values(0),
            node_sizes=self.words_by_cluster_.index.get_level_values(1),
            x_axis_at=0,
            y_axis_at=0,
            color_scheme=color_scheme,
            xlabel="X-Axis",
            ylabel="Y-Axis",
            figsize=figsize,
            fontsize=fontsize,
        )

    def _compute_centrality_density(self):

        # ---< data >----------------------------------------------------------
        data = self.table()
        data = data[["num_documents", "cluster"]]
        data = data.groupby("cluster").agg(np.sum)  # data is a pd.DataFrame

        # ---< network structure >---------------------------------------------
        clusters = self.nodes_.copy()
        links = self.edges_.copy()

        # -----< callon's density >-------------------------------------------
        density_links = links.cluster_source == links.cluster_target
        density = links[density_links].copy()
        density = density[["cluster_source", "value"]]
        density = density.groupby("cluster_source").value.sum()
        density.index = density.index.rename("cluster")
        density = density.to_frame(name="density")

        # -----< collect results >---------------------------------------------
        data = pd.concat([data, density], axis=1)
        data["density"] = (
            100 * data.density / len(links.cluster_source.drop_duplicates())
        )

        # -----< callon's centrality >-----------------------------------------
        centrality_links = links.cluster_source != links.cluster_target
        centrality = links[centrality_links].copy()
        centrality = centrality[["cluster_source", "cluster_target", "value"]]
        centrality = centrality.reset_index(drop=True)

        dup = centrality.copy()
        dup = dup.rename(
            columns={
                "cluster_source": "cluster_target",
                "cluster_target": "cluster_source",
            }
        )
        centrality = centrality.append(dup)
        centrality.reset_index(inplace=True, drop=True)
        centrality = centrality.rename(columns={"cluster_source": "cluster"})
        centrality = centrality.groupby("cluster").agg(np.sum)[["value"]]
        centrality = centrality.rename(columns={"value": "centrality"})
        centrality = centrality.centrality

        # -----< collect results >---------------------------------------------
        data = pd.concat([data, centrality], axis=1)

        communities = self.communities().loc[0, :].tolist()
        data["name"] = communities

        self.centrality_density_ = data

    def centrality_density_table(self):
        return self.centrality_density_.copy()

    def centrality_density_map(self, color_scheme="clusters", figsize=(8, 8)):
        """

        Implements a thematic map based on bibliometrix/conceptual structure/thematic map.
        Source code: thematicMap.R in bibliometrix/R/


        Cobo, M. J., Lopez-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011).
        An approach for detecting, quantifying,  and visualizing the evolution of a
        research field: A practical application to the fuzzy sets theory field.
        Journal of Informetrics, 5(1), 146-166.

        """

        median_density = self.centrality_density_.density.median()
        median_centrality = self.centrality_density_.centrality.median()

        return bubble_map(
            node_x=self.centrality_density_["centrality"],
            node_y=self.centrality_density_["density"],
            node_clusters=range(len(self.centrality_density_)),
            # node_texts=[f"CLTR_{i}" for i in self.clusters_.index],
            node_texts=self.centrality_density_.name,
            node_sizes=self.centrality_density_["num_documents"],
            x_axis_at=median_centrality,
            y_axis_at=median_density,
            color_scheme=color_scheme,
            xlabel="centrality",
            ylabel="density",
            figsize=figsize,
            fontsize=7,
        )
