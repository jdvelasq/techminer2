"""
Institutions' production over time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/institutions_production_over_time.html"

>>> institutions_production_over_time(
...    top_n=10, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/institutions_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .column_production_by_year import column_production_by_year


def institutions_production_over_time(
    top_n=10,
    directory="./",
):

    return column_production_by_year(
        column="institutions",
        top_n=top_n,
        directory=directory,
        title="Institutions' production over time",
    )
