"""
Most Frequent Countries in References
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_countries_in_references.html"

>>> most_frequent_countries(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_countries_in_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_frequent_items import most_frequent_items


def most_frequent_countries_in_references(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
):
    """Plots the number of documents by country using the specified plot."""

    return most_frequent_items(
        column="countries",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Countries in References",
        plot=plot,
        database="documents",
    )
