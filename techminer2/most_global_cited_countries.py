"""
Most global cited countries
===============================================================================

See https://jdvelasq.github.io/techminer2/column_indicators.html

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_global_cited_countries.html"

>>> most_global_cited_countries(
...     directory=directory,
...     top_n=20,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_global_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cleveland_chart import cleveland_chart


def most_global_cited_countries(directory="./", top_n=20):

    return cleveland_chart(
        column="countries",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        metric="global_citations",
        title="Most global cited countries",
    )
