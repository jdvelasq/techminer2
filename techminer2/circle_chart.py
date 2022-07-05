"""
Circle Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/circle_chart.html"

>>> indicators = make_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> circle_chart(indicators, hole=0.5).write_html(file_name)

.. raw:: html

    <iframe src="_static/circle_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""

from .circle_px import circle_px
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def circle_chart(
    dataframe,
    metric="OCC",
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
