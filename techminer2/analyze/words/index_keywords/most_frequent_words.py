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


>>> from techminer2.analyze import performance_metrics
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| index_keywords          |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINANCE                 |          1 |    10 |             3 |                   7 |               70    |
| FINTECH                 |          2 |    10 |             3 |                   7 |               70    |
| FINANCIAL_SERVICES      |          3 |     5 |             0 |                   5 |              100    |
| FINANCIAL_INDUSTRY      |          4 |     4 |             1 |                   3 |               75    |
| COMMERCE                |          5 |     3 |             1 |                   2 |               66.67 |
| SURVEY                  |          6 |     3 |             1 |                   2 |               66.67 |
| ELECTRONIC_MONEY        |          7 |     3 |             0 |                   3 |              100    |
| SUSTAINABLE_DEVELOPMENT |          8 |     3 |             0 |                   3 |              100    |
| BLOCKCHAIN              |          9 |     2 |             0 |                   2 |              100    |
| INVESTMENT              |         10 |     2 |             1 |                   1 |               50    |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/index_keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/index_keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
