# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Base Column Plot Class."""

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


@dataclass
class ColumnPlotParams:
    """:meta private:"""

    title_text: Optional[str] = None
    xaxes_title_text: Optional[str] = None
    yaxes_title_text: Optional[str] = None


class ColumnPlotMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ColumnPlotParams: {key}")
        return self

    def build_column_plot(self, dataframe, y_col):

        title_text = self.plot_params.title_text
        xaxes_title_text = self.plot_params.xaxes_title_text
        yaxes_title_text = self.plot_params.yaxes_title_text

        fig = px.bar(
            dataframe,
            x=None,
            y=y_col,
            hover_data=dataframe.columns.to_list(),
            orientation="v",
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title_text,
        )
        fig.update_traces(
            marker_color=MARKER_COLOR,
            marker_line={"color": MARKER_LINE_COLOR},
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=270,
            title_text=xaxes_title_text,
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title_text=yaxes_title_text,
        )

        return fig
