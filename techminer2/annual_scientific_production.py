"""
Annual Scientific Production
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/annual_scientific_production.html"

>>> annual_scientific_production(directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators import annual_indicators
from .time_plot import time_plot


def annual_scientific_production(directory="./"):
    """Computes annual scientific production (number of documents per year)."""

    indicators = annual_indicators(directory)
    return time_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )
