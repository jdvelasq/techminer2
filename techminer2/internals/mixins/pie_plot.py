# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"""Pie Plot Mixin."""

import plotly.express as px  # type: ignore


class PiePlotMixin:

    def build_pie_plot(self, data_frame):

        hover_data = data_frame.columns.to_list()
        names = data_frame.index.to_list()
        title_text = self.params.title_text
        hole = self.params.pie_hole
        values = self.params.terms_order_by

        fig = px.pie(
            data_frame,
            values=values,
            names=names,
            hole=hole,
            hover_data=hover_data,
            title=title_text,
        )

        fig.update_traces(textinfo="percent+value")

        fig.update_layout(legend={"y": 0.5})

        return fig
