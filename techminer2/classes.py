"""
Define classes for retorning the results of the functions.
"""

from dataclasses import dataclass

import pandas as pd
import plotly.graph_objs as go


@dataclass(init=False)
class ColumnViewer:
    """Column viewer."""

    table_: pd.DataFrame
    plot_: go.Figure
    prompt_: str
    topic_: str


@dataclass(init=False)
class CoOccurrenceMatrix:
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
    criterion_for_columns_: str
    criterion_for_rows_: str
