"""
Define classes for retorning the results of the functions.
"""

from dataclasses import dataclass

import networkx as nx
import pandas as pd
import plotly.graph_objs as go


@dataclass(init=False)
class Chart:
    """VantagePointChart."""

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


@dataclass(init=False)
class ListCellsInMatrix:
    """List cells in matrix."""

    cells_list_: pd.DataFrame
    criterion_: str
    metric_: str
    other_criterion_: str
    prompt_: str


@dataclass(init=False)
class ListView:
    """List view."""

    criterion_: str
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
