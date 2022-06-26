"""
Line chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/line_chart.html"

>>> line_chart(
...     'author_keywords',
...     top_n=15,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/line_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .column_indicators_by_metric import column_indicators_by_metric
from .line_plot import line_plot


def line_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    file_name="documents.csv",
):
    """Makes a line chart from a dataframe."""

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        file_name=file_name,
    )
    return line_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
