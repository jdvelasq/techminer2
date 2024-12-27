# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Cleveland Dot Plot Mixin."""

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


@dataclass
class LinePlotParams:
    """:meta private:"""

    title_text: Optional[str] = None
    xaxes_label: Optional[str] = None
    yaxes_label: Optional[str] = None


class LinePlotMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for LinePlotParams: {key}")
        return self

    def build_line_plot(self, dataframe, y_col):

        metric_label = self.chart_params.metric_label
        field_label = self.chart_params.field_label
        title_text = self.chart_params.title_text

        data_frame = performance_metrics_frame(
            metric=metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        if metric_label is None:
            metric_label = metric.replace("_", " ").upper()

        if field_label is None:
            field_label = self.item_params.field.replace("_", " ").upper()

        if title_text is None:
            title_text = ""

        fig = px.line(
            data_frame,
            x=None,
            y=metric,
            hover_data=data_frame.columns.to_list(),
            markers=True,
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title_text,
        )
        fig.update_traces(
            marker=dict(size=9, line={"color": "#465c6b", "width": 2}),
            marker_color=MARKER_COLOR,
            line={"color": MARKER_LINE_COLOR},
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=270,
            title_text=field_label,
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title_text=metric_label,
        )

        return fig
