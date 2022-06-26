"""
Cleveland Chart
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/cleveland_chart.html"

>>> cleveland_chart(
...    column="author_keywords", 
...    top_n=20,
...    directory=directory,
...     metric="num_documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/cleveland_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .column_indicators_by_metric import column_indicators_by_metric
from .cleveland_plot import cleveland_plot


def cleveland_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    file_name="documents.csv",
):

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        file_name=file_name,
    )

    return cleveland_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
