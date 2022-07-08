"""
Most Frequent Cititng Authors
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_citing_authors.html"

>>> most_frequent_citing_authors(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_citing_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_frequent_items import most_frequent_items


def most_frequent_citing_authors(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
):
    """Plots the number of documents by author using the specified plot."""

    return most_frequent_items(
        column="authors",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Citing Authors",
        plot=plot,
        database="cited_by",
    )
