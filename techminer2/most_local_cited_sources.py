"""
Most Local Cited Sources (in References)
===============================================================================

Plot the most local cited sources in the references.

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="iso_source_name",
        directory=directory,
        file_name="references.csv",
    )


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_local_cited_sources.html"

>>> most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cleveland_chart import cleveland_chart


def most_local_cited_sources(directory="./", top_n=20):

    return cleveland_chart(
        column="iso_source_name",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        metric="num_documents",
        title="Most local cited sources",
        file_name="references.csv",
    )
