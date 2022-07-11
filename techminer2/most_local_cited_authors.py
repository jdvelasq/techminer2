"""
Most Local Cited Authors
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="authors",
        directory=directory,
        database="references",
    )


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_local_cited_authors.html"

>>> most_local_cited_authors(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .chart import chart


def most_local_cited_authors(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most Local Cited Authors (from Reference Lists)."""

    return chart(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited Authors (from Reference Lists)",
        plot=plot,
        database="references",
        metric="local_citations",
    )
