# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"Ranking Plot Mixin."

import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


class RankingPlotMixin:

    def build_ranking_plot(self, data_frame):

        y_col = self.params.terms_order_by

        #
        hover_data = data_frame.columns.to_list()
        line_width = self.params.line_width
        marker_size = self.params.marker_size
        textfont_size = self.params.textfont_size
        title_text = self.params.title_text
        xaxes_title_text = self.params.xaxes_title_text
        yaxes_title_text = self.params.yaxes_title_text
        yshift = self.params.yshift

        fig = px.line(
            data_frame,
            x="Rank",
            y=y_col,
            hover_data=hover_data,
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

        for name, row in data_frame.iterrows():
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
