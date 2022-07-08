"""
Most frequent sources in references
===============================================================================

Most frequent sources in references database (with non duplicated entries).

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_sources_in_references.html"

>>> most_frequent_sources_in_references(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_sources_in_references.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_frequent_items import most_frequent_items


def most_frequent_sources_in_references(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
):
    """Plots the number of documents by source (in references database) using the specified plot."""

    return most_frequent_items(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Sources (in References)",
        plot=plot,
        database="references",
    )
