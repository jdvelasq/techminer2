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
from .column_indicators import column_indicators
from .word_cloud_plot import word_cloud_plot


def word_cloud(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
    database="documents",
    #
    figsize=(12, 12),
):
    """Plots a word cloud from a dataframe."""

    indicators = column_indicators(
        column=column,
        directory=directory,
        database=database,
        use_filter=(database == "documents"),
        sep=";",
    )

    indicators = indicators.sort_values(metric, ascending=False)

    if min_occ is not None:
        indicators = indicators[indicators.num_documents >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.num_documents <= max_occ]
    if top_n is not None:
        indicators = indicators.head(top_n)

    return word_cloud_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
        figsize=figsize,
    )
