"""
Documents by year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/documents_by_year_plot.html"

>>> documents_by_year(
...     directory
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/documents_by_year_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

---

"""
from .annual_indicators_plot import annual_indicators_plot


def documents_by_year(directory="./"):
    return annual_indicators_plot(
        column="num_documents",
        title="Documents by year",
        directory=directory,
    )
