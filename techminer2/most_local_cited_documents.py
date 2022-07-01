"""
Most local cited documents
===============================================================================

See :doc:`document indicators <document_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_local_cited_documents.html"

>>> most_local_cited_documents(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_cited_documents import most_cited_documents


def most_local_cited_documents(
    top_n=20,
    directory="./",
):
    """Most local cited documents."""

    return most_cited_documents(
        metric="local_citations",
        top_n=top_n,
        directory=directory,
        title="Most local cited documents",
        use_filter=False,
    )
