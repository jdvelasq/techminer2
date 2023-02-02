"""
Average Citations per Year
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__average_citations_per_year.html"

>>> from techminer2 import bibliometrix__average_citations_per_year
>>> bibliometrix__average_citations_per_year(directory).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ..._time_plot import time_plot
from ...techminer.indicators.indicators_by_year import indicators_by_year


def bibliometrix__average_citations_per_year(
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

    return time_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )
