"""
Most Global Cited Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_sources.html"

>>> from techminer2 import bibliometrix__most_global_cited_sources
>>> bibliometrix__most_global_cited_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_global_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_global_cited_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Most global cited sources."""

    return vantagepoint__chart(
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
