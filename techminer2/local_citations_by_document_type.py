"""
Local Citations by Document Type
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/local_citations_by_document_type.html"

>>> local_citations_by_document_type(
...     directory,
...     plot="bar",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/local_citations_by_type.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart
from .pie_chart import pie_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .word_cloud import word_cloud


def local_citations_by_document_type(
    directory="./",
    plot="cleveland",
    database="documents",
):
    """Plots the number of local citations by document type using the specified plot."""

    if database == "documents":
        title = "Local Citations by Document Type"
    elif database == "references":
        title = "Local Citations in References by Document Type"
    elif database == "cited_by":
        title = "Local Citations in Citing Documents by Document Type"
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
        column="document_type",
        min_occ=None,
        max_occ=None,
        top_n=None,
        directory=directory,
        metric="local_citations",
        title=title,
        database=database,
    )
