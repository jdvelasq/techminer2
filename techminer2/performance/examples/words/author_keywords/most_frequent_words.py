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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| author_keywords         |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                 |          1 |    28 |            20 |                   8 |               28.57 |
| FINTECH                 |          2 |    12 |            10 |                   2 |               16.67 |
| REGULATORY_TECHNOLOGY   |          3 |     7 |             5 |                   2 |               28.57 |
| COMPLIANCE              |          4 |     7 |             5 |                   2 |               28.57 |
| REGULATION              |          5 |     5 |             4 |                   1 |               20    |
| ANTI_MONEY_LAUNDERING   |          6 |     5 |             5 |                   0 |                0    |
| FINANCIAL_SERVICES      |          7 |     4 |             3 |                   1 |               25    |
| FINANCIAL_REGULATION    |          8 |     4 |             2 |                   2 |               50    |
| ARTIFICIAL_INTELLIGENCE |          9 |     4 |             3 |                   1 |               25    |
| RISK_MANAGEMENT         |         10 |     3 |             2 |                   1 |               33.33 |

>>> metrics.fig_.write_html("sphinx/_static/performance/words/author_keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/author_keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
