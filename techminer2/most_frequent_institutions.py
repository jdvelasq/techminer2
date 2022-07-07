"""
Most frequent institutions
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_frequent_institutions.html"

>>> most_frequent_institutions(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_institutions.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .pie_chart import pie_chart
from .word_cloud import word_cloud
from .terms_list import terms_list


def most_frequent_institutions(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="bar",
    database="documents",
):
    """Plots the number of documents by institutions using the specified plot."""

    if database == "documents":
        title = "Most Frequent Institutions"
    elif database == "references":
        title = "Most Frequent Institutions in References"
    elif database == "cited_by":
        title = "Most Frequent Institutions in Citing Documents"
    else:
        raise ValueError(
            "Invalid database name. Database must be one of: 'documents', 'references', 'cited_by'"
        )
    indicators = terms_list(
        column="institutions",
        metric="OCC",
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database=database,
    )
    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "pie": pie_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    return plot_function(
        dataframe=indicators,
        metric="OCC",
        title=title,
    )
