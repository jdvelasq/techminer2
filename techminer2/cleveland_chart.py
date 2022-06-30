"""
Cleveland Chart
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/cleveland_chart.html"

>>> cleveland_chart(
...    column="author_keywords", 
...    top_n=20,
...    directory=directory,
...     metric="num_documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/cleveland_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cleveland_plot import cleveland_plot
from .column_indicators import column_indicators


def cleveland_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    database="documents",
):
    """Makes a cleveland chart from a dataframe."""

    indicators = column_indicators(
        column=column,
        directory=directory,
        database=database,
        use_filter=True if database == "documents" else False,
        sep=";",
    )

    indicators = indicators.sort_values(metric, ascending=False)

    if min_occ is not None:
        indicators = indicators[indicators.num_documents >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.num_documents <= max_occ]
    if top_n is not None:
        indicators = indicators.head(top_n)

    return cleveland_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
