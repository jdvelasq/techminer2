"""
Extract Custom Topics
===============================================================================

Extract and plot the user custom topics of the selected column.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/extract_custom_topics.png"
>>> custom_topics = find_string(
...     "author_keywords", 
...     contains='fintech',
...     directory=directory,
... ).head(10)
>>> extract_custom_topics(
...     column="author_keywords",
...     topics=custom_topics,
...     directory=directory,
... ).savefig(file_name)

.. image:: images/extract_custom_topics.png
    :width: 700px
    :align: center


>>> extract_custom_topics(
...     column="author_keywords",
...     topics=custom_topics,
...     directory=directory,
...     plot=False,
... )
                                        before 2020  between 2020-2021
fintech                                          42                 97
fintech application                               1                  2
fintech accelerators                              1                  0
determinants of using fintech services            0                  1
definition of fintech                             0                  1
cross-sector fintech                              0                  1
characteristics of fintech                        0                  1
fintech collaboration                             0                  1
fintech business model                            0                  1
fintech adoption                                  0                  1

"""

from .growth_indicators import growth_indicators
from .stacked_bar_chart import stacked_bar_chart


def extract_custom_topics(
    column,
    topics,
    top_n=20,
    time_window=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    indicators = growth_indicators(column, time_window=time_window, directory=directory)
    indicators = indicators[indicators.columns[:2]]
    indicators = indicators[indicators.index.isin(topics)]
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
