"""
Most Relevant Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_relevant_sources.html"

>>> from techminer2 import most_relevant_sources
>>> most_relevant_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/most_relevant_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def most_relevant_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
    database="documents",
):
    """Most Relevant Sources."""

    return vantagepoint__chart(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Relevant Sources",
        plot=plot,
        database=database,
    )
