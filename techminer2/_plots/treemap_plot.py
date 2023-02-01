"""Treemap"""


import plotly.express as px

from .format_dataset_to_plot_with_plotly import \
    format_dataset_to_plot_with_plotly


def treemap_plot(
    dataframe,
    metric="OCC",
    title=None,
    colormap="Greys",
):
    """Makes a treemap."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    fig = px.treemap(
        dataframe,
        path=[column],
        values=metric,
        color=metric,
        color_continuous_scale=colormap,
        title=title,
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=1, l=1, r=1, b=1))
    return fig
