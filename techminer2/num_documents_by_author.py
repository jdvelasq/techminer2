"""
Num documents by author (Most relevant authors)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/num_documents_by_author.html"


>>> num_documents_by_author(
...     directory,
...     top_n=20,
...     plot="column",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/num_documents_by_author.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart
from .column_chart import column_chart


def num_documents_by_author(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title="Num documents by author",
    plot="bar",
):
    """Plots the number of documents by author using the specified plot."""

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
    }[plot]

    return plot_function(
        column="authors",
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric="num_documents",
        title=title,
    )
