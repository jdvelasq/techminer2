"""
Annual Scientific Production
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/annual_scientific_production.html"

>>> from techminer2.bbx.overview import annual_scientific_production
>>> annual_scientific_production(directory).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...tm2.plots.time_plot import time_plot
from ...tm2.indicators.annual_indicators import annual_indicators


def annual_scientific_production(directory="./"):
    """Computes annual scientific production (number of documents per year)."""

    indicators = annual_indicators(directory)
    return time_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )
