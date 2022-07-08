"""
Sources' Production over Time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/sources_production_over_time.html"

>>> sources_production_over_time(
...    top_n=10, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/sources_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .production_over_time_chart import production_over_time_chart


def sources_production_over_time(
    top_n=10,
    directory="./",
):
    """Plots source production over time."""

    return production_over_time_chart(
        column="source_abbr",
        top_n=top_n,
        directory=directory,
        title="Sources' production over time",
    )
