"""
Most local cited authors in references
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. Use the following code:


.. code:: python

    column_indicators(
        column="authors", 
        directory=directory, 
        file_name="references.csv",
    )


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_local_cited_authors.html"

>>> most_local_cited_authors(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .cleveland_chart import cleveland_chart


def most_local_cited_authors(
    top_n=20,
    directory="./",
):

    return cleveland_chart(
        column="authors",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        metric="local_citations",
        title="Most local cited authors",
        file_name="references.csv",
    )
