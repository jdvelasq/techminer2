"""
Average Citations per Year
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/average_citations_per_year.html"

>>> from techminer2.bbx.overview import average_citations_per_year
>>> average_citations_per_year(directory).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...tm2.indicators.annual_indicators import annual_indicators
from ...tm2.plots.time_plot import time_plot


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
