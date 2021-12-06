"""
Author keywords wordcolud
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_keywords_wordcloud.png"
>>> author_keywords_wordcloud(10, directory=directory).savefig(file_name)

.. image:: images/author_keywords_wordcloud.png
    :width: 650px
    :align: center


>>> author_keywords_wordcloud(5, directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
blockchain                         17               149               22
innovation                         13               249               46

"""

import os

from .column_indicators import column_indicators
from .word_cloud import word_cloud


def author_keywords_wordcloud(
    top_n=10, figsize=(8, 6), directory="./", cmap="Blues", plot=True
):

    indicators = column_indicators(column="author_keywords", directory=directory)
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
