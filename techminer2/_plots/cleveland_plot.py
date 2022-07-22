"""Makes a cleveland plot from a dataframe."""

from .._px.cleveland_px import cleveland_px
from ..format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def cleveland_plot(
    dataframe,
    metric="OCC",
    title=None,
):
    """Makes a cleveland plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return cleveland_px(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
