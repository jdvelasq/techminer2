"""Makes a bar plot from a dataframe."""

from .bar_px import bar_px
from .format_dataset_to_plot import format_dataset_to_plot


def bar_plot(
    dataframe,
    metric,
    title=None,
):
    """
    Make a  bar plot from a dataframe.

    :param dataframe: Dataframe
    :param metric: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    metric, column, dataframe = format_dataset_to_plot(dataframe, metric)
    return bar_px(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
