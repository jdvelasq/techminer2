"""
Define classes for retorning the results of the functions.
"""

from dataclasses import dataclass

import pandas as pd
import plotly.graph_objs as go


@dataclass(init=False)
class NetworkStatistics:
    """Network statistics."""

    table_: pd.DataFrame
    prompt_: str


@dataclass(init=False)
class RecordStatistics:
    table_: pd.DataFrame
    plot_: go.Figure
    prompt_: str


@dataclass(init=False)
class ColumnViewer:
    table_: pd.DataFrame
    plot_: go.Figure
    prompt_: str
    topic_: str
