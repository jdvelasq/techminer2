"""
Documents by country
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/documents_by_country.html"


>>> documents_by_country(
...     directory
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/documents_by_country.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart


def documents_by_country(directory):

    return bar_chart(
        column="countries",
        min_occ=None,
        max_occ=None,
        top_n=10,
        directory=directory,
        metric="num_documents",
    )
