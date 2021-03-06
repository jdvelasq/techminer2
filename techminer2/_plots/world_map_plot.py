"""Makes a cloropleth plot from a dataframe."""

from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly
from .._px.world_map_px import world_map_px


def world_map_plot(
    dataframe,
    metric,
    title=None,
    colormap="Blues",
):
    """Makes a cloropleth plot from a dataframe."""

    metric, _, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)
    return world_map_px(
        dataframe,
        metric=metric,
        title=title,
        colormap=colormap,
    )
