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
...     field='noun_phrases',
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
| noun_phrases            |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_TECHNOLOGY   |          1 |    20 |            14 |                   6 |               30    |
| FINANCIAL_INSTITUTIONS  |          2 |    15 |            11 |                   4 |               26.67 |
| FINANCIAL_REGULATION    |          3 |     7 |             6 |                   1 |               14.29 |
| REGULATORY_COMPLIANCE   |          4 |     7 |             6 |                   1 |               14.29 |
| FINANCIAL_SECTOR        |          5 |     7 |             5 |                   2 |               28.57 |
| ARTIFICIAL_INTELLIGENCE |          6 |     7 |             4 |                   3 |               42.86 |
| FINANCIAL_SYSTEM        |          7 |     6 |             5 |                   1 |               16.67 |
| GLOBAL_FINANCIAL_CRISIS |          8 |     6 |             3 |                   3 |               50    |
| FINANCIAL_CRISIS        |          9 |     6 |             6 |                   0 |                0    |
| COMPLIANCE_COST         |         10 |     6 |             5 |                   1 |               16.67 |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/noun_phrases/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/noun_phrases/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""