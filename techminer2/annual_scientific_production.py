"""
Annual Scientific Production
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/annual_scientific_production.html"

>>> annual_scientific_production(
...     directory,
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators_plot import annual_indicators_plot


def annual_scientific_production(
    directory="./",
    database="documents",
):
    """Computes annual scientific production (number of documents per year)."""

    if database == "documents":
        title = "Annual Scientific Production"
    elif database == "references":
        title = "Num Documents per Year in References"
    elif database == "cited_by":
        title = "Citing Documents per Year"
    else:
        raise ValueError("Invalid database")

    return annual_indicators_plot(
        column="OCC",
        title=title,
        directory=directory,
        database=database,
    )
