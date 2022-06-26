"""Primitive to make a column plot."""

import plotly.express as px

TEXTLEN = 40


def make_column_plot(
    dataframe,
    x_label=None,
    y_label=None,
    title=None,
):
    """Makes a column plot."""
    fig = px.bar(
        dataframe,
        x=x_label,
        y=y_label,
        hover_data=dataframe.columns.to_list(),
        title=title,
        orientation="v",
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
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(tickangle=270)
    return fig
