"""Treemap"""


import plotly.express as px
import plotly.graph_objects as go

from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def treemap_plot(
    dataframe,
    metric="OCC",
    title=None,
    colormap="Greys",
):
    """Makes a treemap."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)
    dataframe["parent"] = ""

    fig = go.Figure()
    fig.add_trace(
        go.Treemap(
            labels=dataframe[column],
            parents=dataframe["parent"],
            values=dataframe["OCC"],
            textinfo="label+value",
        )
    )
    fig.update_traces(marker={"cornerradius": 5})
    fig.update_layout(
        # template="simple_white",
        showlegend=False,
        margin={"t": 0, "l": 0, "r": 0, "b": 0},
    )

    # add title to plotly figure
    if title is not None:
        fig.update_layout(title=title)

    # Change the colors of the treemap white
    fig.update_traces(
        marker={"line": {"color": "darkslategray", "width": 1}},
        marker_colors=["white"] * len(dataframe[column]),
    )

    # Change the font size of the labels
    fig.update_traces(textfont_size=12)

    return fig
