# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Frequent Words
===============================================================================


>>> from techminer2.performance import performance_metrics
>>> metrics = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='index_keywords',
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| index_keywords         |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:-----------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_COMPLIANCE  |          1 |     9 |             6 |                   3 |               33.33 |
| FINANCIAL_INSTITUTIONS |          2 |     6 |             4 |                   2 |               33.33 |
| FINANCE                |          3 |     5 |             3 |                   2 |               40    |
| REGTECH                |          4 |     5 |             3 |                   2 |               40    |
| ANTI_MONEY_LAUNDERING  |          5 |     3 |             3 |                   0 |                0    |
| FINTECH                |          6 |     3 |             3 |                   0 |                0    |
| INFORMATION_SYSTEMS    |          7 |     2 |             2 |                   0 |                0    |
| INFORMATION_USE        |          8 |     2 |             2 |                   0 |                0    |
| SOFTWARE_SOLUTION      |          9 |     2 |             2 |                   0 |                0    |
| SANDBOXES              |         10 |     2 |             2 |                   0 |                0    |


>>> metrics.fig_.write_html("sphinx/_static/performance/words/index_keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/index_keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
