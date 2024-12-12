# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bubble Chart
===============================================================================

>>> from techminer2.visualize.advanced_charts.bubble_chart import BubbleChart
>>> plot = (
...     BubbleChart()
...     .set_column_params(
...         field="author_keywords",
...         top_n=10,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_row_params(
...         field=None,
...         top_n=None,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_chart_params(
...         title_text=None,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
>>> plot.write_html("sphinx/_generated/visualize/advanced_charts/bubble_chart.html")

.. raw:: html

    <iframe src="../../_generated/visualize/advanced_charts/bubble_chart.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

"""
from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

from ...co_occurrence_matrix.co_occurrence_matrix import co_occurrence_matrix
from ...internals.params.column_and_row_params import ColumnAndRowParamsMixin
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams


@dataclass
class ChartParams:
    """:meta private:"""

    title_text: Optional[str] = None


class BubbleChart(
    ColumnAndRowParamsMixin,
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.chart_params = ChartParams()
        self.column_params = ItemParams()
        self.database_params = DatabaseParams()
        self.row_params = ItemParams()

    def set_chart_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.chart_params, key):
                setattr(self.chart_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ChartParams: {key}")
        return self

    def build(self):

        matrix = co_occurrence_matrix(
            #
            # COLUMN PARAMS:
            columns=self.column_params.field,
            col_top_n=self.column_params.top_n,
            col_occ_range=self.column_params.occ_range,
            col_gc_range=self.column_params.gc_range,
            col_custom_terms=self.column_params.custom_terms,
            #
            # ROW PARAMS:
            rows=self.row_params.field,
            row_top_n=self.row_params.top_n,
            row_occ_range=self.row_params.occ_range,
            row_gc_range=self.row_params.gc_range,
            row_custom_terms=self.row_params.custom_terms,
            #
            # DATABASE PARAMS:
            **self.database_params.__dict__,
        )

        matrix = matrix.melt(value_name="VALUE", var_name="column", ignore_index=False)
        matrix = matrix.reset_index()
        matrix = matrix.rename(columns={matrix.columns[0]: "row"})
        matrix = matrix.sort_values(by=["VALUE", "row", "column"], ascending=[False, True, True])
        matrix = matrix.reset_index(drop=True)

        fig = px.scatter(
            matrix,
            x="row",
            y="column",
            size="VALUE",
            hover_data=matrix.columns.to_list(),
            title=self.chart_params.title_text,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            yaxis_title=None,
            xaxis_title=None,
            margin=dict(l=1, r=1, t=1, b=1),
        )
        fig.update_traces(
            marker=dict(
                line=dict(
                    color="black",
                    width=2,
                ),
            ),
            marker_color="darkslategray",
            mode="markers",
        )
        fig.update_xaxes(
            side="top",
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )
        fig.update_yaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
            autorange="reversed",
        )

        return fig
