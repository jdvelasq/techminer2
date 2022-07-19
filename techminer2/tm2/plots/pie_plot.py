"""Makes a pie plot from a dataframe."""

from ..px.pie_px import pie_px
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def pie_plot(
    dataframe,
    metric="OCC",
    title=None,
    hole=0.5,
):
    """Makes a pie plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return pie_px(
        dataframe=dataframe,
        values=metric,
        names=column,
        title=title,
        hole=hole,
    )
