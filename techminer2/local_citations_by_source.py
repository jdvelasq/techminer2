"""
Local citations by source
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/local_citations_by_source.html"


>>> local_citations_by_source(
...     directory,
...     top_n=20,
...     plot="bar",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/local_citations_by_source.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .plot_metric_by_item import plot_metric_by_item


def local_citations_by_source(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title="local citations by source",
    plot="bar",
):
    """Plots the number of local citations by source name using the specified plot."""

    return plot_metric_by_item(
        column="iso_source_name",
        metric="local_citations",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot=plot,
    )
