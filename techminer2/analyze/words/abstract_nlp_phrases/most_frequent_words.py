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
...     field='abstract_nlp_phrases',
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
| abstract_nlp_phrases    |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_TECHNOLOGY   |          1 |    19 |            13 |                   6 |               31.58 |
| FINANCIAL_INSTITUTIONS  |          2 |    16 |            12 |                   4 |               25    |
| FINANCIAL_CRISIS        |          3 |    12 |             9 |                   3 |               25    |
| REGULATORY_COMPLIANCE   |          4 |    10 |             8 |                   2 |               20    |
| FINANCIAL_SECTOR        |          5 |     9 |             7 |                   2 |               22.22 |
| FINANCIAL_REGULATION    |          6 |     7 |             6 |                   1 |               14.29 |
| ARTIFICIAL_INTELLIGENCE |          7 |     7 |             4 |                   3 |               42.86 |
| FINANCIAL_SYSTEM        |          8 |     6 |             5 |                   1 |               16.67 |
| INFORMATION_TECHNOLOGY  |          9 |     6 |             4 |                   2 |               33.33 |
| COMPLIANCE_COST         |         10 |     6 |             5 |                   1 |               16.67 |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
