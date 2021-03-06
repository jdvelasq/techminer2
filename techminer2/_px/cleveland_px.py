"""Primitive to make a cleveland plot."""

import plotly.express as px


def cleveland_px(
    dataframe,
    x_label,
    y_label,
    title,
):
    """Makes a cleveland plot."""

    fig = px.scatter(
        dataframe,
        x=x_label,
        y=y_label,
        hover_data=dataframe.columns.to_list(),
        title=title,
        size=x_label,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_traces(
        marker=dict(
            size=12,
            line=dict(color="black", width=2),
        ),
        marker_color="slategray",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
    )
    return fig
