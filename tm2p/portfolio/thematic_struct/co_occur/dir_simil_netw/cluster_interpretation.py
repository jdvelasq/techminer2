"""
ClusterInterpretation
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import ClusterInterpretation  # type: ignore
    >>> df = (
    ...     ClusterInterpretation()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string()) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
       CLUSTER  N_UNITS   OCC    TLS  CENTRALITY  DENSITY  N_DOCS N_DOCS_PERCENTAGE  MEAN_YEAR  MEDIAN_YEAR  FIRST_YEAR  LAST_YEAR  GROWTH_RATE  EMERGENCE_SCORE      STRATEGIC_ROLE                                                             UNITS
    0        0       28  4127  26155     12.5674   1.4144    1042           71.22 %     2023.8         2024        2020       2025         5.90            -0.50               Motor                   tinyml; machine learning; tiny machine learning
    1        1       19  1576  11031      9.9776   1.3850     156           10.66 %     2023.9         2024        2020       2025         5.50            -0.34               Motor             internet of things; edge computing; energy efficiency
    2        2       17  1510  10462      9.4214   1.1360     154           10.53 %     2023.4         2024        2020       2025         2.58            -2.03               Motor  neural networks; microcontrollers; convolutional neural networks
    3        3       15   772   5684      8.5490   1.5489      53            3.62 %     2023.5         2024        2020       2025         2.12            -1.89   Specialized/Niche          deep neural networks; quantization; network architecture
    4        4       14   802   5579      7.8727   1.2934      42            2.87 %     2024.5         2025        2021       2025        13.00             2.43  Emerging/Declining                      artificial intelligence; real- time; edge ai
    5        5        7   254   1871      4.3599   1.5927      16            1.09 %     2024.3         2025        2022       2025        15.00             2.34   Specialized/Niche              computer vision; object detection; objects detection

    
"""

from collections import defaultdict

import networkx as nx  # type: ignore
import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.nx import (
    remove_selfloop_edges,
    set_node_group,
    set_node_size_properties,
)
from tm2p.enum import Field

from .cluster_activity import ClusterActivity
from .cluster_composition import ClusterComposition
from .dir_matrix import DirectMatrix as SimilarityMatrix
from .matrix import Matrix as CoOccurrenceMatrix
from .unit_to_cluster import UnitToCluster

CLUSTER = "CLUSTER"
GROUP = "GROUP"
REC_ID = "REC_ID"

# direct metrics
N_UNITS = "N_UNITS"
OCC = "OCC"
TLS = "TLS"
N_DOCS = "N_DOCS"
N_DOCS_PERCENTAGE = "N_DOCS_PERCENTAGE"
GCS = "GCS"
MEAN_GCS = "MEAN_GCS"

# activity metrics
YEAR = Field.YEAR.value
FIRST_YEAR = "FIRST_YEAR"
LAST_YEAR = "LAST_YEAR"
MEAN_YEAR = "MEAN_YEAR"
MEDIAN_YEAR = "MEDIAN_YEAR"

# stragetic diagram metrics
CENTRALITY = "CENTRALITY"
DENSITY = "DENSITY"
STRATEGIC_ROLE = "STRATEGIC_ROLE"

# Emergence metrics
GROWTH_RATE = "GROWTH_RATE"
RECENCY = "RECENCY"
PERSISTENCE = "PERSISTENCE"

Z_GROWTH_RATE = "Z_GROWTH_RATE"
Z_RECENCY = "Z_RECENCY"
Z_PERSISTENCE = "Z_PERSISTENCE"

EMERGENCE_SCORE = "EMERGENCE_SCORE"

UNITS = "UNITS"


class ClusterInterpretation(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> pd.DataFrame:
        """:meta private:"""

        nx_graph = self._build_nx_graph()

        df = self._compute_n_units(nx_graph)
        df = self._compute_occ(df, nx_graph)
        df = self._compute_tls(df, nx_graph)
        df = self._compute_centrality_and_density(df, nx_graph)
        df = self._compute_n_docs(df)
        df = self._compute_strategic_role(df)
        df = self._aggregate_top_terms(df)

        df = df[
            [
                CLUSTER,
                N_UNITS,
                OCC,
                TLS,
                CENTRALITY,
                DENSITY,
                N_DOCS,
                N_DOCS_PERCENTAGE,
                MEAN_YEAR,
                MEDIAN_YEAR,
                FIRST_YEAR,
                LAST_YEAR,
                GROWTH_RATE,
                EMERGENCE_SCORE,
                STRATEGIC_ROLE,
                UNITS,
            ]
        ]

        return df  # type: ignore

    def _build_nx_graph(self):

        simil_matrix = (
            SimilarityMatrix().update(**self.params.__dict__).using_counters(True).run()
        )

        co_occ_matrix = (
            CoOccurrenceMatrix()
            .update(**self.params.__dict__)
            .using_counters(True)
            .run()
        )

        i2c = UnitToCluster().update(**self.params.__dict__).using_counters(True).run()

        nx_graph = nx.from_pandas_adjacency(simil_matrix)
        nx_graph = remove_selfloop_edges(nx_graph)
        nx_graph = set_node_size_properties(self.params, nx_graph, co_occ_matrix)
        nx_graph = set_node_group(nx_graph, i2c)

        return nx_graph

    def _compute_n_units(self, nx_graph) -> pd.DataFrame:

        n_units = {}
        for _, data in nx_graph.nodes(data=True):
            cluster = data["group"]
            if cluster not in n_units:
                n_units[cluster] = 0
            n_units[cluster] += 1

        clusters = sorted(n_units.keys())
        values = [n_units[k] for k in clusters]

        df = pd.DataFrame(
            {
                CLUSTER: clusters,
                N_UNITS: values,
            }
        )

        return df

    def _compute_occ(self, df, nx_graph) -> pd.DataFrame:

        occ = {}
        for _, data in nx_graph.nodes(data=True):
            cluster = data["group"]
            occ_node = data[OCC]
            if cluster not in occ:
                occ[cluster] = 0
            occ[cluster] += occ_node

        clusters = sorted(occ.keys())
        values = [occ[k] for k in clusters]

        df[OCC] = values

        return df

    def _compute_tls(self, df, nx_graph) -> pd.DataFrame:

        tls = {}
        for _, data in nx_graph.nodes(data=True):
            cluster = data["group"]
            tls_node = data[TLS]
            if cluster not in tls:
                tls[cluster] = 0
            tls[cluster] += tls_node

        clusters = sorted(tls.keys())
        values = [tls[k] for k in clusters]

        df[TLS] = values

        return df

    def _compute_centrality_and_density(self, df, nx_graph) -> pd.DataFrame:

        cluster_nodes = defaultdict(set)
        internal_tls: dict[int, float] = defaultdict(float)
        external_tls: dict[int, float] = defaultdict(float)

        cluster_assignment = {
            node: data["group"] for node, data in nx_graph.nodes(data=True)
        }

        for node, cluster in cluster_assignment.items():
            cluster_nodes[cluster].add(node)

        for u, v, data in nx_graph.edges(data=True):
            cu = cluster_assignment[u]
            cv = cluster_assignment[v]
            weight = data.get("weight", 1.0)

            if cu == cv:
                internal_tls[cu] += weight
            else:
                external_tls[cu] += weight
                external_tls[cv] += weight

        density = {
            cluster: 100 * internal_tls[cluster] / len(nodes)
            for cluster, nodes in cluster_nodes.items()
        }

        centrality = {cluster: 10 * external_tls[cluster] for cluster in cluster_nodes}

        clusters = sorted(cluster_nodes.keys())
        density_values = [round(density[k], 4) for k in clusters]
        centrality_values = [round(centrality[k], 4) for k in clusters]

        df[CENTRALITY] = centrality_values
        df[DENSITY] = density_values

        return df

    def _compute_n_docs(self, df) -> pd.DataFrame:

        activity = ClusterActivity().update(**self.params.__dict__).run()

        df[N_DOCS] = 0
        for col in activity.columns:
            df.loc[col, N_DOCS] = activity[col].sum()

        df[N_DOCS_PERCENTAGE] = df[N_DOCS] / df[N_DOCS].sum() * 100
        df[N_DOCS_PERCENTAGE] = [f"{p:.2f} %" for p in df[N_DOCS_PERCENTAGE]]

        #
        # Annual metrics
        #
        df[MEAN_YEAR] = 0.0
        for col in activity.columns:
            df.loc[col, MEAN_YEAR] = (
                sum(year * occ for year, occ in activity[col].items())
                / activity[col].sum()
            )
        df[MEAN_YEAR] = df[MEAN_YEAR].round(1)

        for col in activity.columns:
            values = []
            for year, occ in activity[col].items():
                values.extend([year] * occ)
            if values:
                df.loc[col, MEDIAN_YEAR] = round(pd.Series(values).median(), 1)
                df.loc[col, FIRST_YEAR] = pd.Series(values).min()
                df.loc[col, LAST_YEAR] = pd.Series(values).max()
            else:
                df.loc[col, MEDIAN_YEAR] = 0.0
                df.loc[col, FIRST_YEAR] = 0
                df.loc[col, LAST_YEAR] = 0
        df[MEDIAN_YEAR] = df[MEDIAN_YEAR].astype(int)
        df[FIRST_YEAR] = df[FIRST_YEAR].astype(int)
        df[LAST_YEAR] = df[LAST_YEAR].astype(int)

        #
        # Emergence score
        #
        y_min = activity.index.min()
        y_max = activity.index.max()
        span = y_max - y_min + 1
        recent_window = max(3, int(round(0.3 * span)))

        recent_years = list(range(y_max - recent_window + 1, y_max + 1))
        previous_years = list(range(y_min, y_max - recent_window + 1))

        for col in activity.columns:
            recent_docs = activity.loc[recent_years, col].sum()
            previous_docs = activity.loc[previous_years, col].sum()

            growth_rate = recent_docs / (previous_docs + 1e-9)
            recency = df.loc[col, MEAN_YEAR] - y_min
            recent_active_years = sum(activity.loc[recent_years, col] > 0)
            persistence = recent_active_years / recent_window

            df.loc[col, GROWTH_RATE] = round(growth_rate, 2)
            df.loc[col, RECENCY] = round(recency, 1)
            df.loc[col, PERSISTENCE] = round(persistence, 2)

        #
        # Z-score normalization of emergence score
        #
        mean_growth_rate = df[GROWTH_RATE].mean()
        std_growth_rate = df[GROWTH_RATE].std()
        df[Z_GROWTH_RATE] = (
            (df[GROWTH_RATE] - mean_growth_rate) / (std_growth_rate + 1e-9)
            if std_growth_rate > 0
            else 0.0
        )
        df[Z_GROWTH_RATE] = df[Z_GROWTH_RATE].round(2)

        mean_recency = df[RECENCY].mean()
        std_recency = df[RECENCY].std()
        df[Z_RECENCY] = (
            (df[RECENCY] - mean_recency) / (std_recency + 1e-9)
            if std_recency > 0
            else 0.0
        )
        df[Z_RECENCY] = df[Z_RECENCY].round(2)

        mean_persistence = df[PERSISTENCE].mean()
        std_persistence = df[PERSISTENCE].std()
        df[Z_PERSISTENCE] = (
            (df[PERSISTENCE] - mean_persistence) / (std_persistence + 1e-9)
            if std_persistence > 0
            else 0.0
        )
        df[Z_PERSISTENCE] = df[Z_PERSISTENCE].round(2)

        df[EMERGENCE_SCORE] = (
            df[Z_GROWTH_RATE] + df[Z_RECENCY] + df[Z_PERSISTENCE]
        ).to_list()

        return df

    def _compute_strategic_role(self, df) -> pd.DataFrame:

        centrality_threshold = df[CENTRALITY].median()
        density_threshold = df[DENSITY].median()

        df[STRATEGIC_ROLE] = None

        for idx, row in df.iterrows():

            centrality = row[CENTRALITY]
            density = row[DENSITY]

            high_c = centrality >= centrality_threshold
            high_d = density >= density_threshold

            if high_c and density >= high_d:
                df.at[idx, STRATEGIC_ROLE] = "Motor"
            elif high_c and not high_d:
                df.at[idx, STRATEGIC_ROLE] = "Basic"
            elif not high_c and high_d:
                df.at[idx, STRATEGIC_ROLE] = "Specialized/Niche"
            else:
                df.at[idx, STRATEGIC_ROLE] = "Emerging/Declining"

        return df

    def _aggregate_top_terms(self, df) -> pd.DataFrame:

        composition = (
            ClusterComposition()
            .update(**self.params.__dict__)
            .using_counters(False)
            .run()
        )

        composition[UNITS] = composition[UNITS].str.split("; ")
        composition[UNITS] = composition[UNITS].str[:3]
        composition[UNITS] = composition[UNITS].str.join("; ")

        df = df.merge(
            composition[[CLUSTER, UNITS]],
            on=CLUSTER,
            how="left",
        )

        return df
