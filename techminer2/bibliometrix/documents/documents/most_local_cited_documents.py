"""
Most Local Cited Documents
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_documents.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.documents.documents.most_local_cited_documents(
...     topics_length=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ..cited_documents import bibiometrix_cited_documents


def most_local_cited_documents(
    directory="./",
    topics_length=20,
    title="Most Local Cited Documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most local cited documents."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        directory=directory,
        database="documents",
        top_n=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
