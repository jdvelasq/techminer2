"""
Most global cited documents
===============================================================================

See :doc:`document indicators <document_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_global_cited_documents.html"

>>> most_global_cited_documents(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_global_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_cited_documents import most_cited_documents


def most_global_cited_documents(
    top_n=20,
    directory="./",
):
    return most_cited_documents(
        metric="global_citations",
        top_n=top_n,
        directory=directory,
        title="Most global cited documents",
        use_filter=True,
    )
