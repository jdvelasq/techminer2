"""
Authors' production over time
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/authors_production_over_time.html"

>>> authors_production_over_time(
...    top_n=10, 
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .production_over_time import production_over_time


def authors_production_over_time(
    top_n=10,
    directory="./",
):

    return production_over_time(
        column="authors",
        top_n=top_n,
        directory=directory,
        title="Authors' production over time",
    )
