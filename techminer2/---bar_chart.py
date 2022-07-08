"""
Bar chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bar_chart.html"


>>> indicators = terms_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> bar_chart(indicators).write_html(file_name)

.. raw:: html

    <iframe src="_static/bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
# from .bar_chart import bar_plot
from .column_indicators import column_indicators


def bar_chart(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
    directory="./",
    metric="num_documents",
    title=None,
    database="documents",
):
    """Plots a bar chart from a column of a dataframe."""

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

    return bar_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
