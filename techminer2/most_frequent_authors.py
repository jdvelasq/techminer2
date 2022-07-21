"""
Most Frequent Authors
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_authors.html"

>>> from techminer2 import most_frequent_authors
>>> most_frequent_authors(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/most_frequent_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def most_frequent_authors(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Plots the number of documents by author using the specified plot."""

    return vantagepoint__chart(
        column="authors",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Authors",
        plot=plot,
        database=database,
    )
