# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Pie Plot Mixin."""

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore


@dataclass
class PiePlotParams:
    """:meta private:"""

    title_text: Optional[str] = None
    hole: Optional[float] = 0.4


class PiePlotMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for PiePlotParams: {key}")
        return self

    def build_pie_plot(self, dataframe, values_col):

        title_text = self.plot_params.title_text
        hole = self.plot_params.hole

        fig = px.pie(
            dataframe,
            values=values_col,
            names=dataframe.index.to_list(),
            hole=hole,
            hover_data=dataframe.columns.to_list(),
            title=title_text,
        )
        fig.update_traces(textinfo="percent+value")
        fig.update_layout(legend={"y": 0.5})

        return fig
