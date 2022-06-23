"""
Most relevant sources
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_relevant_sources.html"

>>> most_relevant_sources(
...     directory=directory,
...     top_n=10,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_relevant_sources.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .cleveland_chart import cleveland_chart


def most_relevant_sources(directory="./", top_n=20):

    return cleveland_chart(
        column="iso_source_name",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        metric="num_documents",
        title="Most relevant sources",
    )

    # from .column_indicators import column_indicators
    indicator = column_indicators(column="iso_source_name", directory=directory)
    indicator = indicator.sort_values(
        by=["num_documents", "global_citations", "local_citations"],
        ascending=False,
    )
    indicator = indicator.head(top_n)
    indicator = indicator.num_documents

    fig = cleveland_plot(
        series=indicator,
        x_label=None,
        y_label=None,
        title="Most relevant sources",
    )

    return fig
