"""
Average Citations per Year
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/average_citations_per_year.html"

>>> average_citations_per_year(
...     directory=directory,
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators_plot import annual_indicators_plot


def average_citations_per_year(
    directory="./",
    database="documents",
):
    """Plots the number of average citations per year of publication."""

    if database == "documents":
        title = "Average citations per Year of Publication"
    elif database == "references":
        title = "Average Citations per Year in References"
    elif database == "cited_by":
        title = "Average citations per year of citing documents"
    else:
        raise ValueError("Invalid database")

    return annual_indicators_plot(
        column="mean_global_citations",
        title=title,
        directory=directory,
        database=database,
    )
