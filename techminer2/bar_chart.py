"""
Bar chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/bar_chart.html"

>>> bar_chart(
...     column='author_keywords',
...     top_n=15,
...     directory=directory,
...     metric="num_documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_plot import bar_plot
from .column_indicators_by_metric import column_indicators_by_metric


def bar_chart(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
    directory="./",
    metric="num_documents",
    title=None,
    file_name="documents.csv",
):
    """Plots a bar chart from a column of a dataframe."""

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        file_name=file_name,
    )

    return bar_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
