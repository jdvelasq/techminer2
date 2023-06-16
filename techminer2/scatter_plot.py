"""
Scatter plot.




"""

import plotly.graph_objects as go

from .network_utils import (
    nx_compute_node_textposition_from_node_coordinates,
    nx_node_occ_to_node_textfont_color,
    nx_scale_node_occ,
)


def scatter_plot(
    node_x,
    node_y,
    node_text,
    node_occ=None,
    node_color=None,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """Makes a scatter plot."""

    def remove_counters(node_text):
        node_text = [" ".join(text.split(" ")[:-1]) for text in node_text]
        return node_text

    textfont_size = nx_scale_node_occ(
        occ=node_occ,
        max_size=textfont_size_max,
        min_size=textfont_size_min,
    )

    node_size = nx_scale_node_occ(
        occ=node_occ,
        max_size=node_size_max,
        min_size=node_size_min,
    )

    textposition = nx_compute_node_textposition_from_node_coordinates(
        node_x, node_y
    )
    textfont_color = nx_node_occ_to_node_textfont_color(node_occ)

    node_text = remove_counters(node_text)

    if node_color is None:
        node_color = "#8da4b4"

    fig = go.Figure(
        layout=go.Layout(
            xaxis={"mirror": "allticks"},
            yaxis={"mirror": "allticks"},
        )
    )

    fig.add_trace(
        go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            hoverinfo="text",
            textposition=textposition,
            text=node_text,
        )
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=1, r=1, t=1, b=1),
    )

    fig.update_traces(
        marker=dict(
            line=dict(color="darkslategray", width=1),
        ),
        marker_color=node_color,
        marker_size=node_size,
        textfont_size=textfont_size,
        textfont_color=textfont_color,
    )

    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
    )

    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
    )

    if xaxes_range is not None:
        fig.update_xaxes(range=xaxes_range)

    if yaxes_range is not None:
        fig.update_yaxes(range=yaxes_range)

    return fig
