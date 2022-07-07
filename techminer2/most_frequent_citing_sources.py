"""
Most frequent citing sources
===============================================================================

Most frequent citing sources in citing documents database.

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_frequent_citing_sources.html"

>>> most_frequent_citing_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_citing_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_frequent_items import most_frequent_items


def most_frequent_citing_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
):
    """Plots the number of documents by source (in citing documents database) using the specified plot."""

    return most_frequent_items(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Sources (in Citing Documents)",
        plot=plot,
        database="cited_by",
    )
