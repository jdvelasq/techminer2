# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Ranking Chart
===============================================================================


>>> from techminer2.visualize.basic_charts.ranking_chart import RankingChart
>>> plot = (
...     RankingChart()
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
...         textfont_size=10,
...         marker_size=7,
...         line_width=1.5,
...         yshift=4,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(metric="OCC")
... )
>>> # plot.write_html("sphinx/_generated/visualize/basic_charts/ranking_chart.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_charts/ranking_chart.html" 
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
    textfont_size: float = 10
    marker_size: float = 7
    line_width: float = 1.5
    yshift: float = 4


class RankingChart(
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
        textfont_size = self.chart_params.textfont_size
        marker_size = self.chart_params.marker_size
        line_width = self.chart_params.line_width
        yshift = self.chart_params.yshift

        data_frame = performance_metrics_frame(
            metric=metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        table = data_frame.copy()
        table["Rank"] = list(range(1, len(table) + 1))

        if metric_label is None:
            metric_label = metric.replace("_", " ").upper()

        if field_label is None:
            field_label = self.item_params.field.replace("_", " ").upper()

        if title_text is None:
            title_text = ""

        fig = px.line(
            table,
            x="Rank",
            y=metric,
            hover_data=data_frame.columns.to_list(),
            markers=True,
        )

        fig.update_traces(
            marker={
                "size": marker_size,
                "line": {"color": MARKER_LINE_COLOR, "width": 1},
            },
            marker_color=MARKER_COLOR,
            line={"color": MARKER_LINE_COLOR, "width": line_width},
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title_text,
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=metric_label,
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=field_label,
        )

        for name, row in table.iterrows():
            fig.add_annotation(
                x=row["Rank"],
                y=row[metric],
                text=name,
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

        return fig
