"""Make a  bar cbart from a dataframe."""

from .._px.bar_px import bar_px
from ..format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def bar_plot(
    dataframe,
    metric="OCC",
    title=None,
):
    """
    Make a  bar cbart from a dataframe.

    :param dataframe: Dataframe with indicators
    :param metric: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return bar_px(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
