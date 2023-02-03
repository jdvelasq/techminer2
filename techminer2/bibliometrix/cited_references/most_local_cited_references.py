"""
Most Local Cited References
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_references.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.cited_references.most_local_cited_references(
...     topics_length=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ..cited_documents import bibiometrix_cited_documents


def most_local_cited_references(
    directory="./",
    topics_length=20,
    title="Most Local Cited References",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the most local cited references."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        directory=directory,
        database="references",
        top_n=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
