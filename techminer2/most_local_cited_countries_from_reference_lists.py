"""
Most local cited countries from reference lists
===============================================================================


See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="countries",
        directory=directory,
        file_name="references.csv",
    )


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_local_cited_countries_from_reference_lists.html"

>>> most_local_cited_countries_from_reference_lists(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_countries_from_reference_lists.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .plot_metric_by_item import plot_metric_by_item


def most_local_cited_countries_from_reference_lists(
    directory="./",
    top_n=20,
    plot="bar",
):
    """Most local cited countries from reference lists."""

    return plot_metric_by_item(
        column="countries",
        metric="local_citations",
        directory=directory,
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        title="Most local cited countries from reference lists",
        plot=plot,
        file_name="references.csv",
    )
