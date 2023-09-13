# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent Words
===============================================================================


>>> from techminer2.performance import performance_metrics
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| keywords                |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                 |          1 |    28 |            20 |                   8 |               28.57 |
| FINTECH                 |          2 |    12 |            10 |                   2 |               16.67 |
| REGULATORY_COMPLIANCE   |          3 |     9 |             6 |                   3 |               33.33 |
| REGULATORY_TECHNOLOGY   |          4 |     8 |             5 |                   3 |               37.5  |
| COMPLIANCE              |          5 |     7 |             5 |                   2 |               28.57 |
| FINANCE                 |          6 |     7 |             4 |                   3 |               42.86 |
| ANTI_MONEY_LAUNDERING   |          7 |     6 |             6 |                   0 |                0    |
| ARTIFICIAL_INTELLIGENCE |          8 |     6 |             4 |                   2 |               33.33 |
| FINANCIAL_INSTITUTIONS  |          9 |     6 |             4 |                   2 |               33.33 |
| REGULATION              |         10 |     5 |             4 |                   1 |               20    |


>>> metrics.fig_.write_html("sphinx/_static/performance/words/keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
