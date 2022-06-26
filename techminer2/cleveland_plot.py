"""Makes a cleveland plot from a dataframe."""

from .cleveland_px import cleveland_px
from .format_dataset_to_plot import format_dataset_to_plot


def cleveland_plot(
    dataframe,
    metric,
    title=None,
):
    """Makes a cleveland plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot(dataframe, metric)
    return cleveland_px(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
