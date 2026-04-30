"""
StrategicDiagram
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_struct.co_occur.dir_simil_netw.strategic_diagram.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.enum import Scaling  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import StrategicDiagram  # type: ignore
    >>> fig = (
    ...     StrategicDiagram()
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
    ...     # MAP:
    ...     .using_colorscale(
    ...         [
    ...             [0.00, "#2C7BB6"],
    ...             [0.35, "#00A6CA"],
    ...             [0.65, "#4EBA6F"],
    ...             [1.00, "#F28E2B"],
    ...         ]
    ...     )    
    ...     .using_node_size_range(20, 80)
    ...     .using_node_scaling(Scaling.LOG)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'    
    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_struct.co_occur.dir_simil_netw.strategic_diagram.html")
    

"""

from collections import defaultdict

import networkx as nx  # type: ignore
import numpy as np
import pandas as pd  # type: ignore
import plotly.graph_objects as go
from duckdb import df
from plotly.colors import sample_colorscale  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.nx import (
    remove_selfloop_edges,
    set_node_group,
    set_node_size_properties,
)
from tm2p.enum import Field, Scaling

from .cluster_activity import ClusterActivity
from .cluster_composition import ClusterComposition
from .cluster_interpretation import ClusterInterpretation
from .dir_matrix import DirectMatrix as SimilarityMatrix
from .matrix import Matrix as CoOccurrenceMatrix
from .unit_to_cluster import UnitToCluster

CLUSTER = "CLUSTER"
# GROUP = "GROUP"
# REC_ID = "REC_ID"

# # direct metrics
# N_UNITS = "N_UNITS"
# OCC = "OCC"
# TLS = "TLS"
N_DOCS = "N_DOCS"
# N_DOCS_PERCENTAGE = "N_DOCS_PERCENTAGE"
# GCS = "GCS"
# MEAN_GCS = "MEAN_GCS"

# # activity metrics
# YEAR = Field.YEAR.value
# FIRST_YEAR = "FIRST_YEAR"
# LAST_YEAR = "LAST_YEAR"
# MEAN_YEAR = "MEAN_YEAR"
# MEDIAN_YEAR = "MEDIAN_YEAR"

# # stragetic diagram metrics
CENTRALITY = "CENTRALITY"
DENSITY = "DENSITY"
# STRATEGIC_ROLE = "STRATEGIC_ROLE"

# # Emergence metrics
# GROWTH_RATE = "GROWTH_RATE"
# RECENCY = "RECENCY"
# PERSISTENCE = "PERSISTENCE"

# Z_GROWTH_RATE = "Z_GROWTH_RATE"
# Z_RECENCY = "Z_RECENCY"
# Z_PERSISTENCE = "Z_PERSISTENCE"

EMERGENCE_SCORE = "EMERGENCE_SCORE"

UNITS = "UNITS"

NODE_COLOR = "NODE_COLOR"
NODE_SIZE = "NODE_SIZE"
LABEL = "LABEL"


class StrategicDiagram(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> go.Figure:
        """:meta private:"""

        df = self._compute_metrics()
        df = self._scale_node_size(df)
        df = self._set_node_color(df)
        df = self._add_node_labels(df)

        fig = self._build_plot(df)
        fig = self._add_quadrant_lines(fig, df)
        fig = self._add_quadrant_labels(fig)
        fig = self._add_node_colorscale(fig, df)

        return fig

    def _add_quadrant_labels(self, fig: go.Figure) -> go.Figure:
        labels = [
            (0.02, 0.98, "<b>Specialized / Niche</b>", "left", "top"),
            (0.98, 0.98, "<b>Motor</b>", "right", "top"),
            (0.02, 0.02, "<b>Emerging / Declining</b>", "left", "bottom"),
            (0.98, 0.02, "<b>Basic / Transversal</b>", "right", "bottom"),
        ]

        for x, y, text, xanchor, yanchor in labels:
            fig.add_annotation(
                x=x,
                y=y,
                xref="paper",
                yref="paper",
                text=text,
                showarrow=False,
                xanchor=xanchor,
                yanchor=yanchor,
                font=dict(size=10),
                bgcolor="rgba(255,255,255,0.75)",
            )

        return fig

    def _add_node_labels(self, df: pd.DataFrame) -> pd.DataFrame:
        df[LABEL] = (
            "<b>C"
            + df[CLUSTER].astype(str)
            + "</b><br>"
            + df[UNITS].str.split("; ").str[:3].str.join("<br>")
        )
        return df

    def _add_node_colorscale(self, fig: go.Figure, df: pd.DataFrame) -> go.Figure:

        colorscale = self.params.colorscale  # your custom scale

        score = df[EMERGENCE_SCORE].tolist()
        score = [round(s, 1) for s in score]
        score = sorted(score)

        score_min = min(score)
        score_max = max(score)

        fig.add_trace(
            go.Scatter(
                x=[None],
                y=[None],
                mode="markers",
                marker=dict(
                    colorscale=colorscale,
                    cmin=score_min,
                    cmax=score_max,
                    color=[score_min, score_max],  # needed to activate colorscale
                    showscale=True,
                    colorbar={
                        "title": {"text": "Emergence<br>Score", "font": {"size": 12}},
                        "thickness": 10,
                        "len": 0.45,
                        "tickfont": {"size": 12},
                    },
                ),
                hoverinfo="none",
                showlegend=False,
            )
        )

        return fig

    def _set_node_color(self, df: pd.DataFrame) -> pd.DataFrame:

        score = df[EMERGENCE_SCORE].tolist()
        score = [round(s, 1) for s in score]

        score_min = min(score)
        score_max = max(score)

        if score_max == score_min:
            score_norm = [0.5] * len(df)
        else:
            score_norm = [(s - score_min) / (score_max - score_min) for s in score]

        rgb_colors = sample_colorscale(self.params.colorscale, score_norm)
        hex_colors = [rgb_to_hex(c) for c in rgb_colors]

        mapping = dict(zip(score, hex_colors))

        df[NODE_COLOR] = df[EMERGENCE_SCORE].apply(lambda x: mapping[round(x, 1)])

        return df

    def _scale_node_size(self, df: pd.DataFrame) -> pd.DataFrame:

        df[NODE_SIZE] = df[N_DOCS].copy()

        if self.params.node_scaling == Scaling.SQRT:
            df[NODE_SIZE] = df[NODE_SIZE].apply(np.sqrt)  # type: ignore
        if self.params.node_scaling == Scaling.LOG:
            df[NODE_SIZE] = df[NODE_SIZE].apply(np.log1p)  # type: ignore

        min_size = df[NODE_SIZE].min()
        max_size = df[NODE_SIZE].max()

        df[NODE_SIZE] = df[NODE_SIZE].apply(
            lambda x: (x - min_size) / (max_size - min_size)
        )

        df[NODE_SIZE] = df[NODE_SIZE].apply(
            lambda x: self.params.node_size_range[0]
            + x * (self.params.node_size_range[1] - self.params.node_size_range[0])
        )

        return df

    def _compute_metrics(self):
        df = (
            ClusterInterpretation()
            .update(**self.params.__dict__)
            .using_counters(True)
            .run()
        )

        return df

    def _build_plot(self, df: pd.DataFrame) -> go.Figure:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df[CENTRALITY],
                y=df[DENSITY],
                mode="markers+text",
                hoverinfo="text",
                # textposition=textpositions,
                text=df[LABEL],
                marker=dict(
                    line=dict(color="#b8c6d0", width=1),
                    opacity=0.8,
                    size=df[NODE_SIZE],
                    color=df[NODE_COLOR].tolist(),
                ),
                showlegend=False,
                # opacity=0.8,
            )
        )

        x_length = df[CENTRALITY].max() - df[CENTRALITY].min()
        x_delta = x_length * 0.15
        x_range = [df[CENTRALITY].min() - x_delta, df[CENTRALITY].max() + x_delta]

        y_length = df[DENSITY].max() - df[DENSITY].min()
        y_delta = y_length * 0.15
        y_range = [df[DENSITY].min() - y_delta, df[DENSITY].max() + y_delta]

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )

        fig.update_xaxes(
            title="Centrality",
            showticklabels=False,
            range=x_range,
        )

        fig.update_yaxes(
            title="Density",
            showticklabels=False,
            range=y_range,
        )

        return fig

    def _add_quadrant_lines(self, fig: go.Figure, df: pd.DataFrame) -> go.Figure:
        x_ref = df[CENTRALITY].median()
        y_ref = df[DENSITY].median()

        fig.add_vline(
            x=x_ref,
            line_width=2,
            line_color="lightgray",
            layer="below",
            opacity=0.8,
        )

        fig.add_hline(
            y=y_ref,
            line_width=2,
            line_color="lightgray",
            layer="below",
            opacity=0.8,
        )

        return fig


def rgb_to_hex(rgb_str):
    r, g, b = map(int, rgb_str.strip("rgb()").split(","))
    return f"#{r:02x}{g:02x}{b:02x}"
