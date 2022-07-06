"""
Countries' Cum Production over Time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/countries_production_over_time.html"

>>> countries_production_over_time(
...    top_n=5, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cum_production_over_time_chart import cum_production_over_time_chart


def countries_production_over_time(
    top_n=5,
    directory="./",
):
    """Cumulative Countries Production over Time."""

    return cum_production_over_time_chart(
        column="countries",
        top_n=top_n,
        directory=directory,
        title="Countires' Cumulative Production over Time",
    )
