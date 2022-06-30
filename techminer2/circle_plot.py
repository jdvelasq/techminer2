"""Makes a cicle plot from a dataframe."""

from .circle_px import circle_px
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def circle_plot(
    dataframe,
    metric,
    title=None,
    hole=0.5,
):
    """Makes a cleveland plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)
    return circle_px(
        dataframe=dataframe,
        values=metric,
        names=column,
        title=title,
        hole=hole,
    )
