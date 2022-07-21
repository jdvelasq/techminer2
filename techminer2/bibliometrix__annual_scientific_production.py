"""
Annual Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__annual_scientific_production.html"

>>> from techminer2 import bibliometrix__annual_scientific_production
>>> bibliometrix__annual_scientific_production(directory).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ._time_plot import time_plot
from .annual_indicators import annual_indicators


def bibliometrix__annual_scientific_production(directory="./"):
    """Computes annual scientific production (number of documents per year)."""

    indicators = annual_indicators(directory)
    return time_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )
