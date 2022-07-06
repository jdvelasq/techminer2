"""
Most local cited sources (from reference lists)
===============================================================================

Plot the most local cited sources in the references.

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="source_abbr",
        directory=directory,
        database="references",
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
from .bar_chart import bar_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .make_list import make_list
from .pie_chart import pie_chart
from .word_cloud import word_cloud


def most_local_cited_sources(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most local cited sources from reference lists."""

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "circle": pie_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    indicators = make_list(
        column="source_abbr",
        metric="local_citations",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        database="references",
    )

    title = "Most local cited sources from reference lists"

    return plot_function(
        dataframe=indicators,
        metric="local_citations",
        title=title,
    )
