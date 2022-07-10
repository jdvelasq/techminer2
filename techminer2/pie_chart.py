"""
Pie Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/pie_chart.html"

>>> pie_chart(
...     'author_keywords',
...     top_n=15,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/pie_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .chart import chart


def pie_chart(
    column,
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title=None,
    database="documents",
):
    """Plots a bar chart from a column of a dataframe."""

    return chart(
        column=column,
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title=title,
        plot="pie",
        database=database,
    )
