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
...     field='author_keywords',
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
| author_keywords                 |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:--------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINTECH                         |          1 |    31 |            13 |                  18 |               58.06 |
| INNOVATION                      |          2 |     7 |             6 |                   1 |               14.29 |
| FINANCIAL_SERVICES              |          3 |     4 |             1 |                   3 |               75    |
| FINANCIAL_TECHNOLOGY            |          4 |     4 |             1 |                   3 |               75    |
| MOBILE_FINTECH_PAYMENT_SERVICES |          5 |     4 |             1 |                   3 |               75    |
| BUSINESS                        |          6 |     3 |             0 |                   3 |              100    |
| SHADOW_BANKING                  |          7 |     3 |             0 |                   3 |              100    |
| FINANCIAL_INCLUSION             |          8 |     3 |             3 |                   0 |                0    |
| CASE_STUDIES                    |          9 |     3 |             1 |                   2 |               66.67 |
| DIGITALIZATION                  |         10 |     3 |             3 |                   0 |                0    |



>>> metrics.fig_.write_html("sphinx/_static/analyze/words/author_keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/author_keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
