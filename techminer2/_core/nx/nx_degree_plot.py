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
import plotly.express as px  # type: ignore

from .nx_degree_frame import nx_degree_frame


def nx_degree_plot(
    #
    # NX GRAPH:
    nx_graph,
    #
    # CHART PARAMS:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
):
    """Compute and plots the degree of a co-occurrence matrix."""

    def plot(data, textfont_size, yshift):
        """Plots the degree of a co-occurrence matrix."""

        fig = px.line(
            data,
            x="Node",
            y="Degree",
            hover_data="Name",
            markers=True,
        )
        fig.update_traces(
            marker={
                "size": marker_size,
                "line": {"color": line_color, "width": 0},
            },
            marker_color=line_color,
            line={"color": line_color, "width": line_width},
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

        for _, row in data.iterrows():
            fig.add_annotation(
                x=row["Node"],
                y=row["Degree"],
                text=row["Name"],
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

        return fig

    #
    #
    # MAIN CODE:
    #
    #

    dataframe = nx_degree_frame(nx_graph)
    fig = plot(dataframe, textfont_size, yshift)

    return fig
