"""
Most frequent authors
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_relevant_authors.html"


>>> most_frequent_authors(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     title="Most Frequent Authors",
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_relevant_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart
from .circle_chart import circle_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .word_cloud import word_cloud


def most_frequent_authors(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title="Most Frequent Authors",
    plot="bar",
    database="documents",
):
    """Plots the number of documents by author using the specified plot."""

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "circle": circle_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    return plot_function(
        column="authors",
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric="num_documents",
        title=title,
        database=database,
    )
