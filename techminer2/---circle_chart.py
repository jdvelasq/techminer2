"""
Circle Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/circle_chart.html"

>>> circle_chart(
...     'author_keywords',
...     top_n=15,
...     directory=directory,
...     hole=0.5,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/circle_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
# from .circle_plot import circle_plot
from .column_indicators import column_indicators


def circle_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    database="documents",
    hole=0.0,
):
    """Makes a circle chart from a dataframe."""

    indicators = column_indicators(
        column=column,
        directory=directory,
        database=database,
        use_filter=(database == "documents"),
        sep=";",
    )

    indicators = indicators.sort_values(metric, ascending=False)

    if min_occ is not None:
        indicators = indicators[indicators.num_documents >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.num_documents <= max_occ]
    if top_n is not None:
        indicators = indicators.head(top_n)

    return circle_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
        hole=hole,
    )
