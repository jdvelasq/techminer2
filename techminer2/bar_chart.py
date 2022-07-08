"""
Bar Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bar_chart.html"

>>> indicators = terms_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> bar_chart(indicators).write_html(file_name)

.. raw:: html

    <iframe src="_static/bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""

from .bar_px import bar_px
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def bar_chart(
    dataframe,
    metric="OCC",
    title=None,
):
    """
    Make a  bar cbart from a dataframe.

    :param dataframe: Dataframe with indicators
    :param metric: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return bar_px(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
