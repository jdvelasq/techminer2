"""
Institutions' Cum Production over Time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/institutions_cum_production_over_time.html"

>>> institutions_cum_production_over_time(
...    top_n=5, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/institutions_cum_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cum_production_over_time_chart import cum_production_over_time_chart


def institutions_cum_production_over_time(
    top_n=5,
    directory="./",
):
    """Cumulative Institutions Production over Time."""

    return cum_production_over_time_chart(
        column="institutions",
        top_n=top_n,
        directory=directory,
        title="Institutions' Cumulative Production over Time",
    )
