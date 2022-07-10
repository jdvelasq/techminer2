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
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_local_cited_countries.html"

>>> most_local_cited_countries(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_local_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_plot import bar_plot
from .cleveland_plot import cleveland_plot
from .column_plot import column_plot
from .line_plot import line_plot
from .pie_plot import pie_plot
from .list_view import list_view
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
        "circle": pie_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    indicators = list_view(
        column="countries",
        metric="local_citations",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        database="references",
    )

    title = "Most local cited countries from reference lists"

    return plot_function(
        dataframe=indicators,
        metric="local_citations",
        title=title,
    )
