"""
Manifold 2D map 




"""
import plotly.graph_objects as go

from .._network_lib import (
    nx_compute_node_textposition_from_node_coordinates,
    nx_node_occ_to_node_textfont_color,
    nx_scale_node_occ,
)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def manifold_2d_map(
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

    textfont_sizes = nx_scale_node_occ(
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
            mode="markers",
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
        textfont_size=textfont_sizes,
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

    for pos_x, pos_y, name, textfont_size, textpos, node_occ in zip(
        node_x, node_y, node_text, textfont_sizes, textposition, node_size
    ):
        if textpos == "top right":
            xanchor = "left"
            yanchor = "bottom"
            xshift = 4
            yshift = 4
        elif textpos == "top left":
            xanchor = "right"
            yanchor = "bottom"
            xshift = -4
            yshift = 4
        elif textpos == "bottom right":
            xanchor = "left"
            yanchor = "top"
            xshift = 4
            yshift = -4
        elif textpos == "bottom left":
            xanchor = "right"
            yanchor = "top"
            xshift = -4
            yshift = -4
        else:
            xanchor = "center"
            yanchor = "center"

        fig.add_annotation(
            x=pos_x,
            y=pos_y,
            text=name,
            showarrow=False,
            font={"size": textfont_size},
            bordercolor="grey",
            bgcolor="white",
            xanchor=xanchor,
            yanchor=yanchor,
            xshift=xshift,
            yshift=yshift,
        )

    if xaxes_range is not None:
        fig.update_xaxes(range=xaxes_range)

    if yaxes_range is not None:
        fig.update_yaxes(range=yaxes_range)

    return fig
