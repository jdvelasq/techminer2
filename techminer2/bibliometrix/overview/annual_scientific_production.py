"""
Annual Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/annual_scientific_production.html"

>>> from techminer2.bibliometrix.overview import annual_scientific_production
>>> annual_scientific_production(directory).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

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
