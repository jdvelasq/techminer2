# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Bubble plot."""

import plotly.express as px  # type: ignore


def internal__bubble_plot(params, x_name, y_name, size_col, data_frame):

    fig = px.scatter(
        data_frame,
        x=x_name,
        y=y_name,
        size=size_col,
        hover_data=data_frame.columns.to_list(),
        title=params.title_text,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        yaxis_title=params.yaxes_title_text,
        xaxis_title=params.xaxes_title_text,
        margin={"l": 1, "r": 1, "t": 1, "b": 1},
    )
    fig.update_traces(
        marker={"line": {"color": "black", "width": 2}},
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
