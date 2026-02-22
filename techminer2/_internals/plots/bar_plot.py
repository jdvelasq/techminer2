import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore

from techminer2._internals import Params

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def bar_plot(
    params: Params,
    df: pd.DataFrame,
) -> go.Figure:

    fig = px.bar(
        df,
        x=params.items_order_by.value,
        y=None,
        hover_data=df.columns.to_list(),
        orientation="h",
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=params.title_text,
    )
    fig.update_traces(
        marker_color=MARKER_COLOR,
        marker_line={"color": MARKER_LINE_COLOR},
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=params.xaxes_title_text,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        title_text=params.yaxes_title_text,
    )

    return fig
