"""
Column Pie Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_pie_chart.png"
>>> column_pie_chart('author_keywords', 15, directory=directory).savefig(file_name)

.. image:: images/column_pie_chart.png
    :width: 700px
    :align: center


>>> column_pie_chart('author_keywords', 15, directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
blockchain                         17               149               22
innovation                         13               249               46

"""

import os

from .indicators_api.column_indicators import column_indicators
from .visualization_api.pie_chart import pie_chart


def column_pie_chart(
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
    return pie_chart(
        series,
        darkness=darkness,
        cmap=cmap,
        figsize=figsize,
        fontsize=9,
        wedgeprops={
            "width": 0.6,
            "edgecolor": "k",
            "linewidth": 0.5,
            "linestyle": "-",
            "antialiased": True,
        },
    )
