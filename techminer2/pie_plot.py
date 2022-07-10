"""
Pie Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/pie_plot.html"

>>> indicators = list_view(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> pie_plot(indicators, hole=0.5).write_html(file_name)

.. raw:: html

    <iframe src="_static/pie_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly
from .pie_px import pie_px


def pie_plot(
    dataframe,
    metric="OCC",
    title=None,
    hole=0.5,
):
    """Makes a cleveland plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return pie_px(
        dataframe=dataframe,
        values=metric,
        names=column,
        title=title,
        hole=hole,
    )
