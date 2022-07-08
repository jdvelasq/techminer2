"""
Sources' Cum Production over Time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/sources_cum_production_over_time.html"

>>> sources_cum_production_over_time(
...    top_n=5, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/sources_cum_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cum_production_over_time_chart import cum_production_over_time_chart


def sources_cum_production_over_time(
    top_n=5,
    directory="./",
):
    """Sources' Cumulative Production over Time."""

    return cum_production_over_time_chart(
        column="authors",
        top_n=top_n,
        directory=directory,
        title="Sources' Cumulative Production over Time",
    )
