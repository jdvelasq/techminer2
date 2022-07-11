"""
Most Local Cited References
===============================================================================

See :doc:`document indicators <document_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_local_cited_references.html"

>>> most_local_cited_references(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .chart import chart


def most_local_cited_references(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most local cited references."""

    return chart(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited References",
        plot=plot,
        database="references",
        metric="local_citations",
    )
