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
from ..._time_plot import time_plot
from ...techminer.indicators.indicators_by_year import indicators_by_year


def bibliometrix__annual_scientific_production(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes annual scientific production (number of documents per year)."""

    indicators = indicators_by_year(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    return time_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )
