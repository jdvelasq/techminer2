"""Primitive to make a line plot."""

import plotly.express as px


def line_px(
    dataframe,
    x_label,
    y_label,
    title,
):
    """Makes a line plot."""

    fig = px.line(
        dataframe,
        x=x_label,
        y=y_label,
        hover_data=dataframe.columns.to_list(),
        title=title,
        markers=True,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_traces(
        marker=dict(size=10, line=dict(color="darkslategray", width=2)),
        marker_color="rgb(171,171,171)",
        # marker_line={"color": "darkslategray"},
        line=dict(color="darkslategray"),
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )
    return fig
