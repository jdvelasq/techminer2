"""Primitive to make a scatter plot."""

import plotly.express as px


def scatter_px(
    dataframe,
    x_label,
    y_label,
    size,
    title,
):
    """Makes a scatter plot."""

    fig = px.scatter(
        dataframe,
        x=x_label,
        y=y_label,
        size=size,
        hover_data=dataframe.columns.to_list(),
        title=title,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_traces(
        marker=dict(
            line=dict(color="darkslategray", width=2),
        ),
        marker_color="lightgrey",
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
