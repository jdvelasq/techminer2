"""
Bubble Map.




"""

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import sequential


def bubble_map(
    node_x,
    node_y,
    node_text,
    node_size=None,
    node_color=None,
    delta=0.2,
):
    """Makes a map chart."""

    textfont_size = _compute_textfont_size(node_size)
    textfont_color = _compute_textfont_color(node_size)
    node_text = _compute_node_text(node_text)
    textposition = _compute_textposition(node_x, node_y)

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

    x_max = node_x.max()
    x_min = node_x.min()
    x_range = x_max - x_min

    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
        range=[x_min - delta * x_range, x_max + delta * x_range],
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
    return fig


def _compute_node_text(node_text):
    node_text = [" ".join(text.split(" ")[:-1]) for text in node_text]
    return node_text


def _compute_textposition(node_x, node_y):
    x_mean = node_x.mean()
    y_mean = node_y.mean()
    textposition = []
    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition.append("top right")
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition.append("top left")
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition.append("bottom left")
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition.append("bottom right")
    return textposition


def _compute_textfont_color(node_size):
    colors = px.colors.sequential.Greys
    color_index = np.array(
        [
            0.4 + 0.60 * (size - node_size.min()) / (node_size.max() - node_size.min())
            for size in node_size
        ]
    )
    textfont_color = np.array(colors)[
        np.round(color_index * (len(colors) - 1)).astype(int)
    ]

    return textfont_color


def _compute_textfont_size(node_size):
    "Computes the textfont_size parameter."

    max_textfont_size = 40
    min_textfont_size = 2

    textfont_size = [
        min_textfont_size
        + (max_textfont_size - min_textfont_size)
        * (size - node_size.min())
        / (node_size.max() - node_size.min())
        for size in node_size
    ]

    return textfont_size
