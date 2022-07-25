"""
Most Local Cited Sources (from reference lists)
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_sources.html"

>>> from techminer2 import bibliometrix__most_local_cited_sources
>>> bibliometrix__most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_local_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_local_cited_sources(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most Local Cited Sources (from Reference Lists)."""

    return vantagepoint__chart(
        criterion="source_abbr",
        directory=directory,
        topics_length=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited Sources (from Reference Lists)",
        plot=plot,
        database="references",
        metric="local_citations",
    )
