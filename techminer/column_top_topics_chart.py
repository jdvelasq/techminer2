"""
Column Top Topics Chart
===============================================================================

Extract and plot the top topics of the selected column.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/column_top_topics_chart.png"
>>> column_top_topics_chart(column="author_keywords", directory=directory).savefig(file_name)

.. image:: images/column_top_topics_chart.png
    :width: 700px
    :align: center


>>> column_top_topics_chart(column='author_keywords', directory=directory, plot=False).head()
                        before 2020  between 2020-2021
fintech                          42                 97
financial technologies           11                 17
blockchain                        9                  8
financial inclusion               4                 13
bank                              6                  7


"""

from .growth_indicators import growth_indicators
from .stacked_bar_chart import stacked_bar_chart


def column_top_topics_chart(
    column,
    top_n=20,
    time_window=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    indicators = growth_indicators(column, time_window=time_window, directory=directory)
    indicators = indicators[indicators.columns[:2]]
    indicators = indicators.assign(
        num_documents=indicators[indicators.columns[0]]
        + indicators[indicators.columns[1]]
    )
    indicators = indicators.sort_values(by="num_documents", ascending=False)
    indicators.pop("num_documents")

    if plot is False:
        return indicators

    indicators = indicators.head(top_n)

    return stacked_bar_chart(
        indicators,
        title="Total Num Documents",
        xlabel="Num Documents",
        ylabel=column,
        figsize=figsize,
    )
