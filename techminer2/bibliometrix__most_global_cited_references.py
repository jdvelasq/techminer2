"""
Most Global Cited References
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_references.html"

>>> from techminer2 import bibliometrix__most_global_cited_references
>>> bibliometrix__most_global_cited_references(
...     topics_length=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bibliometrix__cited_documents import bibiometrix_cited_documents


def bibliometrix__most_global_cited_references(
    directory="./",
    topics_length=20,
    title="Most Global Cited References",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the most global cited references."""

    return bibiometrix_cited_documents(
        metric="global_citations",
        directory=directory,
        database="references",
        top_n=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
