# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent Words
===============================================================================


>>> from techminer2.analyze import performance_metrics
>>> metrics = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| keywords              |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:----------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINTECH               |          1 |    32 |            13 |                  19 |               59.38 |
| FINANCE               |          2 |    11 |             4 |                   7 |               63.64 |
| FINANCIAL_SERVICES    |          3 |     8 |             1 |                   7 |               87.5  |
| INNOVATION            |          4 |     8 |             6 |                   2 |               25    |
| FINANCIAL_INDUSTRY    |          5 |     5 |             2 |                   3 |               60    |
| BUSINESS              |          6 |     4 |             0 |                   4 |              100    |
| BLOCKCHAIN            |          7 |     4 |             0 |                   4 |              100    |
| FINANCIAL_INSTITUTION |          8 |     4 |             2 |                   2 |               50    |
| FINANCIAL_TECHNOLOGY  |          9 |     4 |             1 |                   3 |               75    |
| PEER_TO_PEER_LENDING  |         10 |     4 |             1 |                   3 |               75    |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
