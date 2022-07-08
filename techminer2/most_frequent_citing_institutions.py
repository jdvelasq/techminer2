"""
Most Frequent Citing Institutions
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_citing_institutions.html"

>>> most_frequent_citing_institutions(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_citing_institutions.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_frequent_items import most_frequent_items


def most_frequent_citing_institutions(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
):
    """Plots the number of documents by institutions using the specified plot."""

    return most_frequent_items(
        column="institutions",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Citing Institutions",
        plot=plot,
        database="cited_by",
    )
