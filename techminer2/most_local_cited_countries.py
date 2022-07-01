"""
Most local cited countries (from reference lists)
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="countries",
        directory=directory,
        database="references",
    )


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_local_cited_countries.html"

>>> most_local_cited_countries(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart
from .circle_chart import circle_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .word_cloud import word_cloud


def most_local_cited_countries(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most local cited countries from reference lists."""

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "circle": circle_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    return plot_function(
        column="countries",
        min_occ=None,
        max_occ=None,
        top_n=top_n,
        directory=directory,
        metric="local_citations",
        title="Most local cited countries from reference lists",
        database="references",
    )
