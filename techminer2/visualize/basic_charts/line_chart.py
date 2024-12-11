# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Line Chart
===============================================================================

>>> from techminer2.visualize.basic_charts.line_chart import LineChart
>>> plot = (
...     LineChart()
...     .set_item_params(
...         field="author_keywords",
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_chart_params(
...         title_text="Most Frequent Author Keywords",
...         metric_label=None,
...         field_label=None,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(metric="OCC")
... )
>>> # plot.write_html("sphinx/_generated/visualize/basic_charts/line_chart.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_charts/line_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...metrics.performance_metrics_frame import performance_metrics_frame

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


@dataclass
class ChartParams:
    """:meta private:"""

    title_text: Optional[str] = None
    metric_label: Optional[str] = None
    field_label: Optional[str] = None


class LineChart(
    ItemParamsMixin,
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.chart_params = ChartParams()
        self.database_params = DatabaseParams()
        self.item_params = ItemParams()

    def set_chart_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.chart_params, key):
                setattr(self.chart_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ChartParams: {key}")
        return self

    def build(self, metric: str = "OCC"):

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
