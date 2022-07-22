"""Makes a line plot from a dataframe."""

from ..format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly
from .._px.line_px import line_px


def line_plot(
    dataframe,
    metric="OCC",
    title=None,
):
    """Makes a line plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return line_px(
        dataframe=dataframe,
        x_label=column,
        y_label=metric,
        title=title,
    )
