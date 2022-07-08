"""
Most Global Cited Sources in `documents`
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_global_cited_sources.html"

>>> most_global_cited_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_global_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_global_cited_items import most_global_cited_items


def most_global_cited_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    title="Most Global Cited Sources",
):
    """Most global cited sources in `documents`."""

    return most_global_cited_items(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot=plot,
        database="documents",
    )
