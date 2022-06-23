"""
Most relevant institutions
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_relevant_institutions.html"

>>> most_relevant_institutions(
...     directory=directory,
...     top_n=20,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_relevant_institutions.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .cleveland_chart import cleveland_chart


def most_relevant_institutions(directory="./", top_n=20):

    return cleveland_chart(
        column="institutions",
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        directory=directory,
        metric="num_documents",
        title="Most relevant institutions",
    )
