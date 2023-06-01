"""
Classes
=======

This module define the classes used by the :mod:`techminer2` package
for returning results.


"""

from dataclasses import dataclass

import matplotlib.figure
import networkx as nx
import pandas as pd
import plotly.graph_objs as go


@dataclass(init=False)
class BradfordLaw:
    """Bradford's Law."""

    plot_: go.Figure
    source_clustering_: pd.DataFrame
    core_sources_: pd.DataFrame


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


@dataclass(init=False)
class BasicChart:
    """Basic chart.

    Attributes:
        plot_ (go.Figure): Plotly figure.
        prompt_ (str): Prompt.
        table_ (pd.DataFrame): Table.

    """

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class CorrMatrix:
    """Correlation matrix."""

    matrix_: pd.DataFrame
    prompt_: str
    method_: str
    criterion_: str
    other_criterion_: str
    metric_: str


@dataclass(init=False)
class CorrMap:
    """Correlation map."""

    plot_: go.Figure
    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class ColumnViewer:
    """Column viewer."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame
    topic_: str


@dataclass(init=False)
class CocMatrix:
    """Co-cccurrence matrix."""

    criterion_: str
    matrix_: pd.DataFrame
    metric_: str
    other_criterion_: str
    prompt_: str


@dataclass(init=False)
class NormCocMatrix:
    """Normalized co-cccurrence matrix."""

    criterion_: str
    matrix_: pd.DataFrame
    metric_: str
    other_criterion_: str
    prompt_: str
    association_index_: str


@dataclass(init=False)
class ListCellsInMatrix:
    """List cells in matrix."""

    cells_list_: pd.DataFrame
    criterion_: str
    is_matrix_subset_: bool
    metric_: str
    other_criterion_: str
    prompt_: str


@dataclass(init=False)
class ListView:
    """List view."""

    field_: str
    metric_: str
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class ManifoldMap:
    """Manifold map."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class MatrixSubset:
    """Matrix subset."""

    criterion_: str
    is_ego_matrix_: bool
    matrix_: pd.DataFrame
    metric_: str
    other_criterion_: str
    prompt_: str
    topics_: list


@dataclass(init=False)
class MatrixViewer:
    """Matrix viewer."""

    graph_: nx.Graph
    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class NetworkStatistics:
    """Network statistics."""

    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class RecordStatistics:
    """Record statistics."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class ScientopyBar:
    """Scientopy bar."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class TermsByYear:
    """Terms by year."""

    criterion_: str
    cumulative_: bool
    metric_: str
    other_criterion_: str
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class TFMatrix:
    """Term-frequency matrix."""

    criterion_: str
    prompt_: str
    scheme_: str
    table_: pd.DataFrame


@dataclass(init=False)
class TFIDFMatrix:
    """Term-frequency IDF matrix."""

    criterion_: str
    prompt_: str
    table_: pd.DataFrame


@dataclass(init=False)
class WordComparison:
    """Word comparison."""

    plot_: go.Figure
    prompt_: str
    table_: pd.DataFrame
