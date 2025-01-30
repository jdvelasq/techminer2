# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node degree plot

"""
from dataclasses import dataclass
from typing import Optional

import networkx as nx  # type: ignore
import pandas as pd
import plotly.express as px  # type: ignore


@dataclass
class NxDegreePlotParams:
    """:meta private:"""

    textfont_size: float = 10
    marker_size: float = 7
    line_color: str = "black"
    line_width: float = 1.5
    yshift = (4,)


class NxDegreeMixin:
    """:meta private:"""

    def set_plot_params(self, **kwargs):
        """:meta private:"""

        for key, value in kwargs.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for NxDegreePlotParams: {key}")
        return self

    def nx_degree_plot(self, node_degrees_dataframe):

        fig = px.line(
            node_degrees_dataframe,
            x="Node",
            y="Degree",
            hover_data="Name",
            markers=True,
        )
        fig.update_traces(
            marker={
                "size": self.plot_params.marker_size,
                "line": {"color": self.plot_params.line_color, "width": 0},
            },
            marker_color=self.plot_params.line_color,
            line={
                "color": self.plot_params.line_color,
                "width": self.plot_params.line_width,
            },
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Degree",
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Node",
        )

        for _, row in node_degrees_dataframe.iterrows():
            fig.add_annotation(
                x=row["Node"],
                y=row["Degree"],
                text=row["Name"],
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": self.plot_params.textfont_size},
                yshift=self.plot_params.yshift,
            )

        return fig
