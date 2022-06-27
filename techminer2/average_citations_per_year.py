"""
Average Citations per Year
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/average_citations_per_year.html"

>>> average_citations_per_year(directory=directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators_plot import annual_indicators_plot


def average_citations_per_year(directory="./"):
    return annual_indicators_plot(
        column="mean_global_citations",
        title="Average citations per year",
        directory=directory,
    )
