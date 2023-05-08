"""
Annual Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__annual_scientific_production.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.overview.annual_scientific_production(directory)
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
year
2016     1
2017     4
2018     3
2019     6
2020    14
Name: OCC, dtype: int64

"""
from ..._lib._time_plot import time_plot
from ...techminer.indicators.indicators_by_year import indicators_by_year
from dataclasses import dataclass


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None


def annual_scientific_production(
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

    results = _Results()
    results.table_ = indicators["OCC"]
    results.plot_ = time_plot(
        indicators,
        metric="OCC",
        title="Annual Scientific Production",
    )

    return results
