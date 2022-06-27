"""
Word cloud (chart)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/word_cloud.png"

>>> word_cloud(
...     column='author_keywords', 
...     metric='num_documents',
...     title="Author Keywords",
...     top_n=50, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/word_cloud.png
    :width: 900px
    :align: center

"""

from .column_indicators_by_metric import column_indicators_by_metric
from .word_cloud_plot import word_cloud_plot


def word_cloud(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    file_name="documents.csv",
    #
    figsize=(12, 12),
):
    """Makes a word cloud from a dataframe."""

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        file_name=file_name,
    )

    return word_cloud_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
        figsize=figsize,
    )
