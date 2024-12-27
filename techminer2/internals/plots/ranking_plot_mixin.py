# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"Ranking Plot Mixin."

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


@dataclass
class RankingPlotParams:
    """:meta private:"""

    line_width: float = 1.5
    marker_size: float = 7
    textfont_size: float = 10
    title_text: Optional[str] = None
    xaxes_title_text: Optional[str] = None
    yaxes_title_text: Optional[str] = None
    yshift: float = 4


class RankingPlotMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for RankingPlotParams: {key}")
        return self

    def build_ranking_plot(self, dataframe, y_col):

        line_width = self.plot_params.line_width
        marker_size = self.plot_params.marker_size
        textfont_size = self.plot_params.textfont_size
        title_text = self.plot_params.title_text
        xaxes_title_text = self.plot_params.xaxes_title_text
        yaxes_title_text = self.plot_params.yaxes_title_text
        yshift = self.plot_params.yshift

        fig = px.line(
            dataframe,
            x="Rank",
            y=y_col,
            hover_data=dataframe.columns.to_list(),
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
            title=yaxes_title_text,
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=xaxes_title_text,
        )

        for name, row in dataframe.iterrows():
            fig.add_annotation(
                x=row["Rank"],
                y=row[y_col],
                text=name,
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

        return fig
