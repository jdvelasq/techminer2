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
...     field='title_nlp_phrases',
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
| title_nlp_phrases               |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:--------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINTECH                         |          1 |    27 |            10 |                  17 |               62.96 |
| BANKING                         |          2 |     7 |             3 |                   4 |               57.14 |
| MOBILE_FINTECH_PAYMENT_SERVICES |          3 |     5 |             1 |                   4 |               80    |
| CHINA                           |          4 |     5 |             3 |                   2 |               40    |
| IMPACT                          |          5 |     4 |             1 |                   3 |               75    |
| CHALLENGES                      |          6 |     3 |             1 |                   2 |               66.67 |
| FINTECH_REVOLUTION              |          7 |     3 |             1 |                   2 |               66.67 |
| INDUSTRY                        |          8 |     3 |             2 |                   1 |               33.33 |
| SECURE                          |          9 |     3 |             1 |                   2 |               66.67 |
| ROLE                            |         10 |     3 |             0 |                   3 |              100    |



>>> metrics.fig_.write_html("sphinx/_static/analyze/words/title_nlp_phrases/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/title_nlp_phrases/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
