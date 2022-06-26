"""
Column chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/column_chart.html"

>>> column_chart(
...     column='author_keywords',
...     top_n=15,
...     directory=directory,
...     metric="num_documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/column_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .column_indicators_by_metric import column_indicators_by_metric
from .column_plot import column_plot


def column_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
):
    """Plots a column chart from a column of a dataframe."""

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
    )

    return column_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
