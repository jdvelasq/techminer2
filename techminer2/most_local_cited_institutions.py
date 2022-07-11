"""
Most Local Cited Institutions
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="institutions",
        directory=directory,
        database="references",
    )


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_local_cited_institutions.html"

>>> most_local_cited_institutions(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_institutions.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .chart import chart


def most_local_cited_institutions(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most Local Cited Sources (from Reference Lists)."""

    return chart(
        column="institutions",
        directory=directory,
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited Institutions (from Reference Lists)",
        plot=plot,
        database="references",
        metric="local_citations",
    )
