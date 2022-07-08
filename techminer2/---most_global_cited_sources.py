"""
Most Global Cited Sources
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_global_cited_sources.html"

>>> most_global_cited_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_global_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart
from .pie_chart import pie_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .word_cloud import word_cloud


def most_global_cited_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="bar",
    database="documents",
):
    """Plots the number of global citations by author using the specified plot."""

    if database == "documents":
        title = "Most Global Cited sources"
    elif database == "references":
        title = "Most Global Cited sources in References"
    elif database == "cited_by":
        title = "Most Global Cited sources in citing documents"
    else:
        raise ValueError(
            "Invalid database name. Database must be one of: 'documents', 'references', 'cited_by'"
        )

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "circle": pie_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    return plot_function(
        column="source_abbr",
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric="global_citations",
        title=title,
        database=database,
    )
