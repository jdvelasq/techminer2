import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def ranking_chart(
    params: Params,
    dataframe: pd.DataFrame,
) -> go.Figure:

    fig = px.line(
        dataframe,
        x="Rank",
        y=params.items_order_by.value,
        hover_data=dataframe.columns.to_list(),
        markers=True,
    )

    fig.update_traces(
        marker={
            "size": params.marker_size,
            "line": {
                "color": MARKER_LINE_COLOR,
                "width": 1,
            },
        },
        marker_color=MARKER_COLOR,
        line={
            "color": MARKER_LINE_COLOR,
            "width": params.line_width,
        },
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=params.title_text,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=params.yaxes_title_text,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=params.xaxes_title_text,
    )

    for name, row in dataframe.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row[params.items_order_by.value],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={
                "size": params.textfont_size,
            },
            yshift=params.yshift,
        )

    return fig
