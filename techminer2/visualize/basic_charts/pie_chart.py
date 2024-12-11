# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Pie Chart
===============================================================================


>>> from techminer2.visualize.basic_charts.pie_chart import PieChart
>>> plot = (
...     PieChart()
...     .set_item_params(
...         field="author_keywords",
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_chart_params(
...         title_text="Most Frequent Author Keywords",
...         hole=0.4,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(metric="OCC")
... )
>>> plot.write_html("sphinx/_generated/visualize/basic_charts/pie_chart.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_charts/pie_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...metrics.performance_metrics_frame import performance_metrics_frame


@dataclass
class ChartParams:
    """:meta private:"""

    title_text: Optional[str] = None
    hole: Optional[float] = 0.4


class PieChart(
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

        title_text = self.chart_params.title_text
        hole = self.chart_params.hole

        data_frame = performance_metrics_frame(
            metric=metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        fig = px.pie(
            data_frame,
            values=metric,
            names=data_frame.index.to_list(),
            hole=hole,
            hover_data=data_frame.columns.to_list(),
            title=title_text,
        )
        fig.update_traces(textinfo="percent+value")
        fig.update_layout(legend={"y": 0.5})

        return fig
