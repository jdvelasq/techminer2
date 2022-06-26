"""
Cleveland plot
===============================================================================


>>> from techminer2 import *
>>> from techminer2.cleveland_plot import cleveland_plot
>>> directory = "data/"
>>> file_name = "sphinx/_static/cleveland_plot.html"
>>> dataframe = column_indicators(
...     column="countries",
...     directory=directory,
... ).head(20)

>>> cleveland_plot(
...     dataframe,
...     metric="num_documents",
...     title="Most relevant countries",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/cleveland_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .format_dataset_to_plot import format_dataset_to_plot
from .cleveland_px import cleveland_px


def cleveland_plot(
    dataframe,
    metric,
    title=None,
):

    metric, column, dataframe = format_dataset_to_plot(dataframe, metric)
    return cleveland_px(
        dataframe=dataframe,
        x_label=metric,
        y_label=column,
        title=title,
    )
