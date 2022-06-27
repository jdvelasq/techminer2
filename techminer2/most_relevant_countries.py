"""
Most relevant countries (ok!)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_relevant_countries.html"

>>> most_relevant_countries(
...     directory,
...     top_n=20,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_relevant_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .plot_metric_by_item import plot_metric_by_item


def most_relevant_countries(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title="Most relevant countries",
    plot="bar",
):
    """Plots the number of documents by country using the specified plot."""

    return plot_metric_by_item(
        column="countries",
        metric="num_documents",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot=plot,
    )
