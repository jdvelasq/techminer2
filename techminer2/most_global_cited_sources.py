"""
Most Global Cited Sources
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
from .vp.report.chart import chart


def most_global_cited_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Most global cited sources."""

    return chart(
        column="source_abbr",
        directory=directory,
        metric="global_citations",
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Global Cited Sources",
        plot=plot,
        database=database,
    )
