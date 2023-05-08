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
      local_citations  ...  mean_local_citations_per_year
year                   ...                               
2016              0.0  ...                           0.00
2017              3.0  ...                           0.11
2018             30.0  ...                           1.67
2019             19.0  ...                           0.63
2020             29.0  ...                           0.52
<BLANKLINE>
[5 rows x 9 columns]

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
    results.table_ = indicators[
        [col for col in indicators.columns if col not in ["OCC", "cum_OCC"]]
    ]
    results.plot_ = time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )

    return results
