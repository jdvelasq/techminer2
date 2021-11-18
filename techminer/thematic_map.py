"""
Thematic map
===============================================================================

Implements a thematic map based on bibliometrix/conceptual structure/thematic map.
Source code: thematicMap.R in bibliometrix/R/


Cobo, M. J., Lopez-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011). 
An approach for detecting, quantifying,  and visualizing the evolution of a 
research field: A practical application to the fuzzy sets theory field. 
Journal of Informetrics, 5(1), 146-166.

"""
import numpy as np
import pandas as pd

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network_analysis import co_occurrence_network_analysis
from .plots import bubble_map


class ThematicMap:
    def __init__(
        self,
        directory,
        column,
        min_occ=1,
        sep="; ",
    ):
        self.directory = directory
        self.column = column
        self.min_occ = min_occ
        self.sep = sep
        #
        self.run()

    def run(self):

        # ---< co-occurrence matrix >------------------------------------------
        self.co_occurrence_matrix = co_occurrence_matrix(
            directory=self.directory,
            column=self.column,
            min_occ=self.min_occ,
            association="association",
            # association="equivalence",
            sep=self.sep,
        )

        # ---< co-occurrence network >-----------------------------------------
        self.co_occurrence_network = co_occurrence_network(
            matrix=self.co_occurrence_matrix,
            algorithm="louvain",
        )

        # ---< data >----------------------------------------------------------
        # table[node, num_documents, global_citattions, cluster, betweenness, closeness]
        data = self.co_occurrence_network.table()
        data = data[["num_documents", "cluster"]]
        data = data.groupby("cluster").agg(np.sum)  # data is a pd.DataFrame

        # ---< number of terms by node >---------------------------------------
        # table with (name, group)
        clusters = self.co_occurrence_network.nodes_.copy()
        # clusters.pop("size")

        # ---< compute links >-------------------------------------------------
        links = self.co_occurrence_matrix.copy()

        # fills upper triangle with 0
        n_cols = len(links.columns)
        for i in range(n_cols):
            for j in range(i, n_cols):
                links.iloc[i, j] = 0.0

        # links matrix (source, target, value)
        links = pd.melt(
            links,
            var_name="target",
            value_name="value",
            ignore_index=False,
        )
        links = links[links.value > 0]
        links = links.reset_index()
        links = links.rename(columns={links.columns[0]: "source"})

        clusters_dic = dict(zip(clusters.name, clusters.group))
        links["cluster_source"] = links.source.map(clusters_dic)
        links["cluster_target"] = links.target.map(clusters_dic)

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

        communities = self.co_occurrence_network.communities().loc[0, :].tolist()
        data["name"] = communities

        self.clusters_ = data

    def map(self, color_scheme="clusters", figsize=(8, 8)):

        median_density = self.clusters_.density.median()
        median_centrality = self.clusters_.centrality.median()

        return bubble_map(
            node_x=self.clusters_["centrality"],
            node_y=self.clusters_["density"],
            node_clusters=range(len(self.clusters_)),
            # node_texts=[f"CLTR_{i}" for i in self.clusters_.index],
            node_texts=self.clusters_.name,
            node_sizes=self.clusters_["num_documents"],
            x_axis_at=median_centrality,
            y_axis_at=median_density,
            color_scheme=color_scheme,
            xlabel="centrality",
            ylabel="density",
            figsize=figsize,
            fontsize=7,
        )

    def table(self):
        return self.co_occurrence_network.table()

    def network(self):
        return self.co_occurrence_network.plot()

    def clusters(self):
        return self.clusters_


def thematic_map(
    directory,
    column,
    min_occ=1,
    sep="; ",
):

    return ThematicMap(
        directory=directory,
        column=column,
        min_occ=min_occ,
        sep=sep,
    )
