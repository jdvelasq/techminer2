"""
Index keywords wordcolud
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/index_keywords_wordcloud.png"
>>> index_keywords_wordcloud(10, directory=directory).savefig(file_name)

.. image:: images/index_keywords_wordcloud.png
    :width: 650px
    :align: center


>>> index_keywords_wordcloud(5, directory=directory, plot=False).head()
                         num_documents  global_citations  local_citations
index_keywords                                                           
fintech                             48               269               52
financial service                   19               347               52
finance                             18               489               77
sustainable development             12                93               21
investment                          10               187               20

"""

import os

from .column_indicators import column_indicators
from .word_cloud import word_cloud


def index_keywords_wordcloud(
    top_n=10, figsize=(8, 6), directory="./", cmap="Blues", plot=True
):

    indicators = column_indicators(column="index_keywords", directory=directory)
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
