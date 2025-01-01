# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Line Plot Mixin."""

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


@dataclass
class LinePlotParams:
    """:meta private:"""

    title_text: Optional[str] = None
    xaxes_title_text: Optional[str] = None
    yaxes_title_text: Optional[str] = None


class LinePlotMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for LinePlotParams: {key}")
        return self

    def build_line_plot(self, dataframe, y_col):

        title_text = self.plot_params.title_text
        xaxes_title_text = self.plot_params.xaxes_title_text
        yaxes_title_text = self.plot_params.yaxes_title_text

        fig = px.line(
            dataframe,
            x=None,
            y=y_col,
            hover_data=dataframe.columns.to_list(),
            markers=True,
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title_text,
        )
        fig.update_traces(
            marker={"size": 9, "line": {"color": "#465c6b", "width": 2}},
            marker_color=MARKER_COLOR,
            line={"color": MARKER_LINE_COLOR},
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
