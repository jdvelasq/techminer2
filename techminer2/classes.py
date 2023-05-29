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
    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class ColumnViewer:
    """Column viewer."""

    table_: pd.DataFrame
    plot_: go.Figure
    prompt_: str
    topic_: str


@dataclass(init=False)
class CooccurrenceMatrix:
    """Occurrence matrix."""

    matrix_: pd.DataFrame
    prompt_: str
    metric_: str
    criterion_: str
    other_criterion_: str


@dataclass(init=False)
class ListCellsInMatrix:
    """List cells in matrix."""

    cells_list_: pd.DataFrame
    prompt_: str
    metric_: str
    criterion_: str
    other_criterion_: str


@dataclass(init=False)
class ListView:
    """List view."""

    table_: pd.DataFrame
    prompt_: str
    metric_: str
    criterion_: str


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

    plot_: go.Figure
    graph_: nx.Graph
    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class NetworkStatistics:
    """Network statistics."""

    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class RecordStatistics:
    """Record statistics."""

    table_: pd.DataFrame
    plot_: go.Figure
    prompt_: str


@dataclass(init=False)
class TermsByYear:
    """Terms by year."""

    table_: pd.DataFrame
    prompt_: str
    metric_: str
    cumulative_: bool
    criterion_: str
    other_criterion_: str
