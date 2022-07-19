"""
Most Global Cited References
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_global_cited_references.html"

>>> from techminer2 import most_global_cited_references
>>> most_global_cited_references(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/most_global_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_xxx_cited_documents import most_xxx_cited_documents


def most_global_cited_references(
    top_n=20,
    directory="./",
):
    """Plots the most global cited references."""

    return most_xxx_cited_documents(
        metric="global_citations",
        top_n=top_n,
        directory=directory,
        title="Most global cited references",
        database="references",
        use_filter=False,
    )
