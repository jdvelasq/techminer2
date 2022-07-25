"""
Most Local Cited Institutions
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_institutions.html"

>>> from techminer2 import bibliometrix__most_local_cited_institutions
>>> bibliometrix__most_local_cited_institutions(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_institutions.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_local_cited_institutions(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most Local Cited Sources (from Reference Lists)."""

    return vantagepoint__chart(
        criterion="institutions",
        directory=directory,
        topics_length=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited Institutions (from Reference Lists)",
        plot=plot,
        database="references",
        metric="local_citations",
    )
