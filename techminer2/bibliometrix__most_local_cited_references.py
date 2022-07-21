"""
Most Local Cited References
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_references.html"

>>> from techminer2 import bibliometrix__most_local_cited_references
>>> bibliometrix__most_local_cited_references(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bibliometrix__cited_documents import bibiometrix_cited_documents


def bibliometrix__most_local_cited_references(
    directory="./",
    top_n=20,
):
    """Most local cited references."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        top_n=top_n,
        directory=directory,
        title="Most Local Cited References",
        database="references",
        use_filter=False,
    )
