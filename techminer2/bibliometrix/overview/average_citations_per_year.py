"""
Average Citations per Year
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__average_citations_per_year.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.overview.average_citations_per_year(directory)
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()    
year
2016    30.000000
2017    40.500000
2018    60.666667
2019     7.833333
2020     6.642857
Name: mean_global_citations, dtype: float64

"""
from dataclasses import dataclass
from ..._lib._time_plot import time_plot
from ...techminer.indicators.indicators_by_year import indicators_by_year


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None


def average_citations_per_year(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Average citations per year."""

    indicators = indicators_by_year(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results = _Results()
    results.table_ = indicators["mean_global_citations"]
    results.plot_ = time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )

    return results
