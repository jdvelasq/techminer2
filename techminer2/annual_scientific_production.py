"""
Annual Scientific Production (ok!)
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2.bibliometrix import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/annual_scientific_production.html"

>>> annual_scientific_production(directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators_plot import annual_indicators_plot


def annual_scientific_production(directory="./"):
    return annual_indicators_plot(
        column="num_documents",
        title="Annual Scientific Production",
        directory=directory,
    )
