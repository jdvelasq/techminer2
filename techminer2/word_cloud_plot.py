"""Makes a word cloud from a dataframe."""

from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly
from .word_cloud_py import word_cloud_py

TEXTLEN = 40


def word_cloud_plot(
    dataframe,
    metric,
    title=None,
    figsize=(8, 8),
):
    """Makes a cleveland plot from a dataframe."""
    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)
    return word_cloud_py(
        dataframe=dataframe,
        metric=metric,
        column=column,
        title=title,
        figsize=figsize,
    )
