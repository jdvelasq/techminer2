"""
Average Citations per Year
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/average_citations_per_year.html"

>>> from techminer2 import average_citations_per_year
>>> average_citations_per_year(directory).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators import annual_indicators
from .time_plot import time_plot


def average_citations_per_year(
    directory="./",
):
    """Average citations per year."""

    indicators = annual_indicators(directory)
    return time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )
