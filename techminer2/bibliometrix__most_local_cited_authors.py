"""
Most Local Cited Authors
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_authors.html"


>>> from techminer2 import bibliometrix__most_local_cited_authors
>>> bibliometrix__most_local_cited_authors(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_local_cited_authors(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most Local Cited Authors (from Reference Lists)."""

    return vantagepoint__chart(
        criterion="authors",
        directory=directory,
        topics_length=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited Authors (from Reference Lists)",
        plot=plot,
        database="references",
        metric="local_citations",
    )
