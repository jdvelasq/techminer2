"""
Most Relevant Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_relevant_sources.html"

>>> from techminer2 import bibliometrix__most_relevant_sources
>>> bibliometrix__most_relevant_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_relevant_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_relevant_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Most Relevant Sources."""

    return vantagepoint__chart(
        criterion="source_abbr",
        directory=directory,
        topics_length=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Relevant Sources",
        plot=plot,
        database=database,
    )
