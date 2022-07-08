"""
Most Global Cited Authors in References
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_global_cited_authors_in_refs.html"

>>> most_global_cited_authors_in_refs(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_global_cited_authors_in_refs.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_global_cited_items import most_global_cited_items


def most_global_cited_authors_in_refs(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    title="Most Global Cited Authors in References",
):
    """Most global cited authors in references."""

    return most_global_cited_items(
        column="authors",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot=plot,
        database="references",
    )
