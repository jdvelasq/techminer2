"""
Bar plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/bar_plot.html"
>>> dataframe = column_indicators(
...     column="countries",
...     directory=directory,
... ).head(20)

>>> bar_plot(
...     dataframe,
...     metric="num_documents",
...     title="Annual Scientific Production",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/bar_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .make_bar_plot import make_bar_plot
from .prepare_plot import prepare_plot


def bar_plot(
    dataframe,
    metric,
    title=None,
):
    """
    Make a  bar plot from a dataframe.

    :param dataframe: Dataframe
    :param metric: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    metric, column, dataframe = prepare_plot(dataframe, metric)
    return make_bar_plot(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
