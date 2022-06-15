"""
Topic View
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> topic_view(
...     'author_keywords',
...     top_n=20,
...     directory=directory,
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

>>> topic_view(
...     'author_keywords',
...     min_occ=8,
...     max_occ=17,
...     directory=directory,
... )
                      num_documents  global_citations  local_citations
author_keywords                                                       
financial inclusion              17               339               61
block-chain                      17               149               22
innovating                       13               249               46
bank                             13               193               23
regulating                       12                89               10
financial service                11               300               43
crowdfunding                      8               116               18
peer-to-peer lending              8                73               11
financial innovation              8                44               15
covid-19                          8                36                6
cryptocurrencies                  8                36                5

>>> topic_view(
...     'author_keywords', 
...     min_occ=8, 
...     max_occ=17,
...     sort_index={"ascending": True},
...     directory=directory,
... )
                      num_documents  global_citations  local_citations
author_keywords                                                       
bank                             13               193               23
block-chain                      17               149               22
covid-19                          8                36                6
crowdfunding                      8               116               18
cryptocurrencies                  8                36                5
financial inclusion              17               339               61
financial innovation              8                44               15
financial service                11               300               43
innovating                       13               249               46
peer-to-peer lending              8                73               11
regulating                       12                89               10


"""
from .column_indicators import column_indicators


def topic_view(
    column,
    metric="num_documents",
    top_n=None,
    min_occ=1,
    max_occ=None,
    sort_values=None,
    sort_index=None,
    directory="./",
):
    # -----------------------------------------------------------------------------------
    order_by_sequence = {
        "num_documents": [
            "num_documents",
            "global_citations",
            "local_citations",
            column,
        ],
        "global_citations": [
            "global_citations",
            "num_documents",
            "local_citations",
            column,
        ],
        "local_citations": [
            "local_citations",
            "num_documents",
            "global_citations",
            column,
        ],
    }

    # -----------------------------------------------------------------------------------

    indicators = column_indicators(column=column, directory=directory)
    if min_occ is not None:
        indicators = indicators[indicators["num_documents"] >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators["num_documents"] <= max_occ]
    indicators.sort_values(
        by=order_by_sequence[metric],
        ascending=[False, False, False, True],
        inplace=True,
    )
    indicators = indicators.head(top_n)

    if sort_values is not None and sort_index is not None:
        raise ValueError("Only one of sort_values and sort_index can be specified")

    if sort_values is not None:
        by = sort_values["by"]
        by = order_by_sequence[by]
        ascending = sort_values["ascending"]
        ascending = [ascending] * 3 + [True]
        indicators = indicators.sort_values(by=by, ascending=ascending)

    # indicators = indicators.set_index(column)

    if sort_index is not None:
        indicators = indicators.sort_index(**sort_index)

    return indicators
