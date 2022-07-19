"""
Most Global Cited Documents
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_global_cited_documents.html"

>>> from techminer2 import most_global_cited_documents
>>> most_global_cited_documents(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/most_global_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_xxx_cited_documents import most_xxx_cited_documents


def most_global_cited_documents(
    top_n=20,
    directory="./",
):
    """Plots the most global cited documents in the main collection."""

    return most_xxx_cited_documents(
        metric="global_citations",
        top_n=top_n,
        directory=directory,
        title="Most global cited documents",
        database="documents",
        use_filter=True,
    )
