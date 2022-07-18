"""
Cleveland Plot
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/cleveland_plot.html"

>>> indicators = list_view(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> cleveland_plot(indicators).write_html(file_name)

.. raw:: html

    <iframe src="_static/cleveland_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""

from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly
from ..px.cleveland_px import cleveland_px


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
