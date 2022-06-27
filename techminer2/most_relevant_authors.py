"""
Most relevant authors
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_relevant_authors.html"


>>> most_relevant_authors(
...     directory,
...     top_n=20,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_relevant_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .plot_metric_by_item import plot_metric_by_item


def most_relevant_authors(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title="Most relevant authors",
    plot="bar",
):
    """Plots the number of documents by author using the specified plot."""

    return plot_metric_by_item(
        column="authors",
        metric="num_documents",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot=plot,
        file_name="documents.csv",
    )
