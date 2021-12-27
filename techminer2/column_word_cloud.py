"""
Column Word Cloud
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_word_cloud.png"
>>> column_word_cloud('author_keywords', 50, directory=directory).savefig(file_name)

.. image:: images/column_wordcloud.png
    :width: 700px
    :align: center


>>> column_word_cloud('author_keywords', 50, directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
block-chain                        17               149               22
bank                               13               193               23

"""

import os

from .indicators_api.column_indicators import column_indicators
from .visualization_api.word_cloud import word_cloud


def column_word_cloud(
    column,
    top_n=10,
    figsize=(8, 6),
    directory="./",
    cmap="Blues",
    plot=True,
):

    indicators = column_indicators(column=column, directory=directory)
    indicators = indicators.sort_values(by="num_documents", ascending=False)

    if plot is False:
        return indicators

    series = indicators.num_documents.head(top_n)
    darkness = indicators.global_citations.head(top_n)
    return word_cloud(
        series=series,
        darkness=darkness,
        cmap=cmap,
        figsize=figsize,
    )
