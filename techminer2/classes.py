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
