import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore

from techminer2._internals import Params

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def line_plot(params: Params, dataframe: pd.DataFrame) -> go.Figure:

    y_col = params.items_order_by

    hover_data = dataframe.columns.to_list()
    title_text = params.title_text
    xaxes_title_text = params.xaxes_title_text
    yaxes_title_text = params.yaxes_title_text

    fig = px.line(
        dataframe,
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
