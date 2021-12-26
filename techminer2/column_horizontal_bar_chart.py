"""
Column Horizontal Bar Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_horizontal_bar_chart.png"
>>> column_horizontal_bar_chart(
...     'author_keywords', 
...     top_n=20, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/column_horizontal_bar_chart.png
    :width: 700px
    :align: center


>>> column_horizontal_bar_chart(
...     'author_keywords', 
...     top_n=20, 
...     directory=directory, 
...     plot=False
... )
                         num_documents  global_citations  local_citations
author_keywords                                                          
fintech                            139              1285              218
financial technologies              28               225               41
financial inclusion                 17               339               61
block-chain                         17               149               22
innovating                          13               249               46
bank                                13               193               23
regulating                          12                89               10
financial service                   11               300               43
crowdfunding                         8               116               18
peer-to-peer lending                 8                73               11
financial innovation                 8                44               15
covid-19                             8                36                6
cryptocurrencies                     8                36                5
technology                           7               192               31
start-up                             7               141               28
finance                              7                52                8
risk                                 7                15                1
business model                       6               174               25
artificial intelligence              6                30                4
regulatory sandbox                   6                26                7

"""


from .column_indicators import column_indicators
from .column_indicators_subset import column_indicators_subset
from .horizontal_bar_chart import horizontal_bar_chart


def column_horizontal_bar_chart(
    column,
    top_n=20,
    cmap="Greys",
    figsize=(8, 6),
    directory="./",
    metric="num_documents",
    sort_values=None,
    sort_index=None,
    plot=True,
):

    indicators = column_indicators(column=column, directory=directory)
    indicators = column_indicators_subset(
        column=column,
        indicators=indicators,
        metric=metric,
        top_n=top_n,
        sort_values=sort_values,
        sort_index=sort_index,
    )
    indicators = indicators.head(top_n)

    if plot is False:
        return indicators

    indicators = indicators[metric]

    return horizontal_bar_chart(
        indicators,
        darkness=indicators,
        cmap=cmap,
        figsize=figsize,
        edgecolor="k",
        linewidth=0.5,
        title=None,
        xlabel=metric.replace("_", " ").title(),
        ylabel=column.replace("_", " ").title(),
        zorder=10,
    )
