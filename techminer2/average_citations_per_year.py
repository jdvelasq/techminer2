"""
Average Citations per Year
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/average_citations_per_year.html"

>>> average_citations_per_year(directory).plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> average_citations_per_year(directory).table_
   year  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
0  2016        2  ...                    5                           -0.0
1  2017        7  ...                   12                           -0.0
2  2018       23  ...                   44                           -0.0
3  2019       37  ...                   57                           -0.0
4  2020       62  ...                   73                           -0.0
5  2021       84  ...                   76                           -0.0
6  2022       94  ...                   76                           -0.0
<BLANKLINE>
[7 rows x 12 columns]

"""
from .annual_indicators import annual_indicators
from .time_plot import time_plot


class _Result:
    """Class for general reporting."""

    def __init__(self, plot, table):
        self.plot_ = plot
        self.table_ = table


def average_citations_per_year(
    directory="./",
):
    """Average citations per year."""

    indicators = annual_indicators(directory)
    plot = time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )

    return _Result(
        plot=plot,
        table=indicators,
    )
