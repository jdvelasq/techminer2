"""Primitive to make a bar plot."""

import plotly.express as px


def make_bar_plot(
    dataframe,
    x_label,
    y_label,
    title,
):
    """Makes a bar plot."""
    fig = px.bar(
        dataframe,
        x=x_label,
        y=y_label,
        hover_data=dataframe.columns.to_list(),
        title=title,
        orientation="h",
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(
        marker_color="rgb(171,171,171)", marker_line={"color": "darkslategray"}
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
