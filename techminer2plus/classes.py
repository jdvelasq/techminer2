"""
Classes
=======

This module define the classes used by the :mod:`techminer2` package
for returning results.


"""

from dataclasses import dataclass

import matplotlib.figure
import networkx as nx
import numpy as np
import pandas as pd
import plotly.graph_objs as go

#
#
# -------------------------------- A N A L Y Z E --------------------------------
#
#


# pylint: disable=too-many-instance-attributes
@dataclass(init=False)
class ItemsList:
    """List view."""

    table_: pd.DataFrame
    prompt_: str
    #
    # Params:
    field_: str
    metric_: str
    #
    # Item filters:
    top_n_: int
    occ_range_: tuple
    gc_range_: tuple
    custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict


# pylint: disable=too-many-instance-attributes
@dataclass(init=False)
class CoocMatrix:
    """Co-cccurrence matrix."""

    matrix_: pd.DataFrame
    prompt_: str
    metric_: str
    #
    # Params:
    columns_: str
    rows_: str
    #
    # Columns item filters:
    col_top_n_: int
    col_occ_range_: tuple
    col_gc_range_: tuple
    col_custom_items_: list
    #
    # Rows item filters:
    row_top_n_: int
    row_occ_range_: tuple
    row_gc_range_: tuple
    row_custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict


# pylint: disable=too-many-instance-attributes
@dataclass(init=False)
class CouplingMatrix:
    """Document coupling matrix."""

    matrix_: pd.DataFrame
    prompt_: str
    metric_: str
    topics_: list
    #
    # Params:
    field_: str
    #
    # Item filters:
    top_n_: int
    occ_range_: tuple
    gc_range_: tuple
    custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict


@dataclass(init=False)
class NormCoocMatrix:
    """Normalized co-cccurrence matrix."""

    columns_: str
    rows_: str
    matrix_: pd.DataFrame
    metric_: str
    prompt_: str
    association_index_: str


@dataclass(init=False)
class AutoCorrMatrix:
    """Auto-correlation matrix."""

    rows_and_columns_: str
    method_: str
    matrix_: pd.DataFrame
    prompt_: str
    metric_: str


@dataclass(init=False)
class CrossCorrMatrix:
    """Cross-correlation matrix."""

    rows_and_columns_: str
    cross_with_: str
    method_: str
    matrix_: pd.DataFrame
    prompt_: str
    metric_: str


class TFMatrix:
    """Term-frequency matrix."""

    table_: pd.DataFrame
    prompt_: str
    #
    # Params:
    field_: str
    scheme_: str
    cooc_within_: int
    #
    # Item filters:
    top_n_: int
    occ_range_: tuple
    gc_range_: tuple
    custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict


# Analyze / Discover / Matrix / TF-IDF Matrix
@dataclass(init=False)
class TFIDFMatrix:
    """Term-frequency IDF matrix."""

    table_: pd.DataFrame
    prompt_: str
    #
    # Params:
    field_: str
    scheme_: str
    cooc_within_: int
    #
    # Item filters:
    top_n_: int
    occ_range_: tuple
    gc_range_: tuple
    custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict


@dataclass(init=False)
class PcaFactorMatrix:
    """PCA factor matrix."""

    field_: str
    table_: pd.DataFrame
    prompt_: str
    explained_variance_: np.ndarray
    explained_variance_ratio_: np.ndarray


@dataclass(init=False)
class KernelPcaFactorMatrix:
    """KernelPCA factor matrix."""

    field_: str
    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class SvdFactorMatrix:
    """PCA factor matrix."""

    field_: str
    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class MdsFactorMatrix:
    """MDS factor matrix."""

    field_: str
    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class ListCellsInMatrix:
    """List cells in matrix."""

    cells_list_: pd.DataFrame
    columns_: str
    is_matrix_subset_: bool
    metric_: str
    rows_: str
    prompt_: str


@dataclass(init=False)
class ManifoldMap:
    """Manifold map."""

    plot_: go.Figure
    table_: pd.DataFrame
    method_: str


################################


# Analyze / Discover / Matrix / Co-occurrence Matrix


# Analyze / Discover / Matrix / Factor Matrix


# Analyze / Discover / Matrix / TF Matrix
@dataclass(init=False)

# Analyze / Discover / Map / Correlation Map
@dataclass(init=False)
class CorrMap:
    """Correlation map."""

    plot_: go.Figure
    table_: pd.DataFrame
    prompt_: str


# Analyze / Discover / Map / Factor Map
@dataclass(init=False)
class FactorMap:
    """Factor Map."""

    plot_: go.Figure
    table_: pd.DataFrame
    prompt_: str


# Analyze / Discover / Terms by Year
@dataclass(init=False)
class TermsByYear:
    """Terms by year."""

    field_: str
    cumulative_: bool
    metric_: str
    prompt_: str
    table_: pd.DataFrame


# Analyze / Explore / Cluster Field
# Analyze / Explore / Cluster Items
# Analyze / Explore / Create Concept Grid
@dataclass(init=False)
class ConceptGrid:
    """Concept grid from PCA."""

    table_: pd.DataFrame
    promt_: str


# Analyze / Explore / Matrix Subset
@dataclass(init=False)
class MatrixSubset:
    """Matrix subset."""

    columns_: str
    rows_: str
    matrix_: pd.DataFrame
    metric_: str
    is_ego_matrix_: bool
    prompt_: str
    custom_items_: list


# Analyze / Explore / Matrix Viewer
@dataclass(init=False)
class MatrixViewer:
    """Matrix viewer."""

    graph_: nx.Graph
    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


# Analyze / Explore / Network Viewer
# Analyze / Calculate / Association Index
# Analyze / Calculate / Network Metrics
@dataclass(init=False)
class NetworkMetrics:
    """Network statistics."""

    prompt_: str
    table_: pd.DataFrame


# Analyze / Calculate / Network Degree Plot
@dataclass(init=False)
class NetworkDegreePlot:
    """Network degree plot."""

    graph_: nx.Graph
    plot_: go.Figure
    table_: pd.DataFrame
    prompt_: str


# Analyze / Main information
@dataclass(init=False)
class MainInformation:
    """Record information."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class RecordStatistics:
    """Record information."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


# Report / Column Chart
# Report / Bar Chart
# Report / Cleveland Dot Chart
# Report / Pie Chart
# Report / Line Chart
# Report / Ranking Chart
# Report / Gantt Chart
# Report / World Map
# Report / Treemap
@dataclass(init=False)
class BasicChart:
    """Basic Chart.

    Attributes:
        plot_ (go.Figure): Plotly figure.
        prompt_ (str): Prompt.
        table_ (pd.DataFrame): Table.
        custom_items_ (list): Custom items.

    """

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame
    custom_items_: list


# Report / Word Cloud
@dataclass(init=False)
class WordCloudChart:
    """WordCloud.

    Attributes:
        plot_ (matplotlib): Plotly figure.
        prompt_ (str): Prompt.
        table_ (pd.DataFrame): Table.

    """

    plot_: matplotlib.figure.Figure
    prompt_: str
    table_: pd.DataFrame


# Report / Bubble Chart
# Report / Heat map

#
# T-LAB
# =============================================================================
#


# Co-occurrence Analysis / Word Associations / Co-occurrence Plot: BasicChart
# Co-occurrence Analysis / Word Associations / Radial Diagram: None
# Co-occurrence Analysis / Word Associations / 2D MDS map
# Co-occurrence Analysis / Word Associations / 2D SVD map
# Co-occurrence Analysis / Word Associations / 2D TSNE map
@dataclass(init=False)
class RadialDiagram:
    """Radial diagram."""

    plot_: go.Figure
    nx_graph_: nx.Graph
    series_: pd.Series
    item_name_: str
    prompt_: str


# Co-occurrence Analysis / Word Associations / Co-occurrence Matrix: None
# Co-occurrence Analysis / Comparison betwen word pairs
@dataclass(init=False)
class WordComparison:
    """Word comparison."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


# Co-occurrence Analysis / Sequences and Network Analysis / Ego Graph : None
# Co-occurrence Analysis / Sequences and Network Analysis / Ego Network : None
# Co-occurrence Analysis / Concordances


@dataclass(init=False)
class Concordances:
    """Concordances."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame
    contexts_: str


# Thematic Analysis / Thematic Analysis of Context
# Thematic Analysis / Modeling of Emergent Themes
# Thematic Analysis / Thematic Document Classification
# Thematic Analysis / Dictionary-based Classificaation
# Thematic Analysis / Text and Discourses

# Comparative Analysis / Specificity Analysis
# Comparative Analysis / Correspondence Analysis
# Comparative Analysis / Multiple Correspondence Analysis
# Comparative Analysis / Cluster Analysis
# Comparative Analysis / Singular Value Decomposition: ManifoldMap
# Comparative Analysis / Multidimensinoa Scaling: ManifoldMap


#
# Bibliometrix
# =============================================================================
#


# Overview / Main Information
# overview / Annual Scientific Production
# Overview / Average Citations per Year
@dataclass(init=False)
class IndicatorByYearChart:
    """Indicator by year chart.

    Attributes:
        plot_ (go.Figure): Plotly figure.
        prompt_ (str): Prompt.
        table_ (pd.DataFrame): Table.

    """

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


# Overview / Three Fields Plot


# Sources / Most Frequent Sources
# Sources / Most Global Cited Sources
# Sources / Most Local Cited Sources
# Sources / Bradow's Law: BradfordLaw
@dataclass(init=False)
class BradfordLaw:
    """Bradford's Law."""

    plot_: go.Figure
    source_clustering_: pd.DataFrame
    core_sources_: pd.DataFrame


# Sources / Source Impact
# Sources / Source production over time


# Authors / Authors / Most Frequent Authors
# Authors / Authors / Most Global Cited Authors
# Authors / Authors / Most Local Cited Authors
# Authors / Authors / Authors Production over Time
@dataclass(init=False)
class ProductionOverTimeChart:
    """Production over time chart.

    Attributes:
        plot_ (go.Figure): Plotly figure.
        prompt_ (str): Prompt.
        table_ (pd.DataFrame): Table.

    """

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame
    documents_per_item_: pd.DataFrame
    production_per_year_: pd.DataFrame


# Authors / Authors / Lotka's Law
@dataclass(init=False)
class LotkaLaw:
    """Lotka's Law."""

    plot_: go.Figure
    table_: pd.DataFrame


# Authors / Authors / Author Impact


# Authors / Organizations / Most Frequent Organizations
# Authors / Organizations / Most Global Cited Organizations
# Authors / Organizations / Most Local Cited Organizations
# Authors / Organizations / Organizations Production over Time
# Authors / Organizations / Organization Impact
# Authors / Organizations / Corresponding Author Organization
@dataclass(init=False)
class CorresponingAuthorOrganization:
    """Corresponding author organization."""

    plot_: go.Figure
    table_: pd.DataFrame
    prompt__: str


# Authors / Countries / Corresponding Author Country
@dataclass(init=False)
class CorresponingAuthorCountry:
    """Corresponding author country."""

    plot_: go.Figure
    table_: pd.DataFrame
    prompt__: str


# Authors / Countries / Most Frequent Countries
# Authors / Countries / Most Global Cited Countries
# Authors / Countries / Most Local Cited Countries
# Authors / Countries / Countries Production over Time
# Authors / Countries / Country Impact
# Authors / Countries / Scientific Production


# Documents / Documents / Most Global Cited Documents
# Documents / Documents / Most Local Cited Documents
@dataclass(init=False)
class MostCitedDocuments:
    """Most cited documents"""

    plot_ = None
    table_ = None


# Documents / Cited References / Most Local Cited References
# Documents / Cited References / Most Global Cited References
# Documents / Cited References / RPYS

# Documents / Words / Most Frequent Words
# Documents / Words / Word Cloud
# Documents / Words / Treemap
# Documents / Words / Word Dynamics
# Documents / Words / Trend Topics

# Clustering / Coupling Matrix List
# Clustering / Clustering by Coupling


# Conceptual Structure / Network Approach / Co-occurrence Network
@dataclass(init=False)
class CoWordsNetwork:
    """Bibliometrix co-occurrence keywords network."""

    degree_plot__plot_: go.Figure
    degree_plot__table_: pd.DataFrame
    degree_plot__prompt_: str

    network_metrics__prompt_: str
    network_metrics__table_: pd.DataFrame

    communities_: pd.DataFrame
    graph_ = nx.Graph
    plot_: go.Figure


# Conceptual Structure / Network Approach / Thematic Map
# Conceptual Structure / Network Approach / Thematic Evolution Plot

# Conceptual Structure / Factorial Approach / Factorial Analysis

# Intellectual Structure / Co-citation Matrix List
# Intellectual Structure / Co-citation Network


@dataclass(init=False)
class CocitationNetwork:
    """Co-citation Network."""

    degree_plot__plot_: go.Figure
    degree_plot__table_: pd.DataFrame
    degree_plot__prompt_: str

    network_metrics__prompt_: str
    network_metrics__table_: pd.DataFrame

    communities_: pd.DataFrame
    graph_ = nx.Graph
    plot_: go.Figure


# Intellectual Structure / Historiograph
@dataclass(init=False)
class HistoriographResults:
    """Historiograph."""

    nx_graph_ = nx.Graph
    plot_: go.Figure
    links_: pd.DataFrame
    articles_: list


# Intellectual Structure / Main Path Analysis
# @dataclass(init=False)
# class MainPathAnalysisResults:
#     """Main path."""

#     nx_graph_ = nx.Graph
#     plot_: go.Figure
#     links_: pd.DataFrame
#     articles_: list


# Social Structure / Collaboration Network
@dataclass(init=False)
class CollaborationNetwork:
    """Collaboration Network."""

    degree_plot__plot_: go.Figure
    degree_plot__table_: pd.DataFrame
    degree_plot__prompt_: str

    network_metrics__prompt_: str
    network_metrics__table_: pd.DataFrame

    communities_: pd.DataFrame
    graph_ = nx.Graph
    plot_: go.Figure


# Social Structure / Collaboration World Map


#
# ScientoPy
# =============================================================================
#


# Bar Graph
@dataclass(init=False)
class ScientoPyGraph:
    """Scientopy bar."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


# Bar Trends
# Time Line
# Word Cloud
# Top Trending Topics
