"""Make a  bar plot from a dataframe."""

from ..px.column_px import column_px
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def column_plot(
    dataframe,
    metric="OCC",
    title=None,
):
    """
    Make a  bar plot from a dataframe.

    :param dataframe: Dataframe
    :param column: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return column_px(
        dataframe=dataframe,
        x_label=column,
        y_label=metric,
        title=title,
    )
