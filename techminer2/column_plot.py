"""
Column plot
===============================================================================

>>> from techminer2 import *
>>> from techminer2.column_plot import column_plot
>>> directory = "data/"
>>> file_name = "sphinx/_static/column_plot.html"
>>> dataframe = column_indicators(
...     column="countries",
...     directory=directory,
... ).head(20)


>>> column_plot(
...     dataframe,
...     metric="num_documents",
...     title="Most relevant countries",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/column_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .column_px import column_px
from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def column_plot(
    dataframe,
    metric,
    title=None,
):
    """
    Make a  bar plot from a dataframe.

    :param dataframe: Dataframe
    :param column: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)
    return column_px(
        dataframe=dataframe,
        x_label=column,
        y_label=metric,
        title=title,
    )
