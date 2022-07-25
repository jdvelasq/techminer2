"""
Most Global Cited Documents
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_documents.html"

>>> from techminer2 import bibliometrix__most_global_cited_documents
>>> bibliometrix__most_global_cited_documents(
...     topics_length=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bibliometrix__cited_documents import bibiometrix_cited_documents


def bibliometrix__most_global_cited_documents(
    directory="./",
    topics_length=20,
    title="Most Global Cited Documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the most global cited documents in the main collection."""

    return bibiometrix_cited_documents(
        metric="global_citations",
        directory=directory,
        database="documents",
        topics_length=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
