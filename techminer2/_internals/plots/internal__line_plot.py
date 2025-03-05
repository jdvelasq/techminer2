# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"""Line Plot Mixin."""


import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def internal__line_plot(params, data_frame):

    y_col = params.terms_order_by

    hover_data = data_frame.columns.to_list()
    title_text = params.title_text
    xaxes_title_text = params.xaxes_title_text
    yaxes_title_text = params.yaxes_title_text

    fig = px.line(
        data_frame,
        x=None,
        y=y_col,
        hover_data=hover_data,
        markers=True,
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title_text,
    )
    fig.update_traces(
        marker={
            "size": 9,
            "line": {
                "color": "#465c6b",
                "width": 2,
            },
        },
        marker_color=MARKER_COLOR,
        line={
            "color": MARKER_LINE_COLOR,
        },
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        title_text=xaxes_title_text,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=yaxes_title_text,
    )

    return fig
