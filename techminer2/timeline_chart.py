"""
Timeline Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/timeline_chart.html"

>>> timeline_chart(
...     column='author_keywords', 
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/timeline_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .production_over_time import production_over_time


def timeline_chart(
    column,
    top_n=10,
    directory="./",
):
    """Timeline chart."""
    return production_over_time(
        column=column,
        top_n=top_n,
        directory=directory,
        title=None,
    )
