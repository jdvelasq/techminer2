"""
Authors' Production over Time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/authors_production_over_time.html"

>>> authors_production_over_time(
...    top_n=10, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .production_over_time_chart import production_over_time_chart


def authors_production_over_time(
    top_n=10,
    directory="./",
):
    """Author production over time."""

    return production_over_time_chart(
        column="authors",
        top_n=top_n,
        directory=directory,
        title="Authors' production over time",
    )
