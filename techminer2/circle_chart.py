"""
Circle Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/circle_chart.html"

>>> circle_chart(
...     'author_keywords',
...     top_n=15,
...     directory=directory,
...     hole=0.5,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/circle_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .circle_plot import circle_plot
from .column_indicators_by_metric import column_indicators_by_metric


def circle_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    file_name="documents.csv",
    hole=0.0,
):
    """Makes a circle chart from a dataframe."""

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        file_name=file_name,
    )

    return circle_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
        hole=hole,
    )
