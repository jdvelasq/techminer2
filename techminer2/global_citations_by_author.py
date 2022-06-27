"""
Global citations by author
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/global_citations_by_author.html"


>>> global_citations_by_author(
...     directory,
...     top_n=20,
...     plot="bar",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/global_citations_by_author.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .plot_metric_by_item import plot_metric_by_item


def global_citations_by_author(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title="Global citations by author",
    plot="bar",
):
    """Plots the number of global citations by author using the specified plot."""

    return plot_metric_by_item(
        column="authors",
        metric="global_citations",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot=plot,
    )
