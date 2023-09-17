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
...     field='descriptors',
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
| descriptors             |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                 |          1 |    29 |            20 |                   9 |               31.03 |
| REGULATORY_TECHNOLOGY   |          2 |    21 |            15 |                   6 |               28.57 |
| FINANCIAL_INSTITUTIONS  |          3 |    16 |            12 |                   4 |               25    |
| REGULATORY_COMPLIANCE   |          4 |    15 |            12 |                   3 |               20    |
| FINANCIAL_REGULATION    |          5 |    12 |             8 |                   4 |               33.33 |
| FINTECH                 |          6 |    12 |            10 |                   2 |               16.67 |
| REGULATION              |          7 |     8 |             5 |                   3 |               37.5  |
| ARTIFICIAL_INTELLIGENCE |          8 |     8 |             5 |                   3 |               37.5  |
| NEW_TECHNOLOGIES        |          9 |     8 |             4 |                   4 |               50    |
| FINANCIAL_SECTOR        |         10 |     7 |             5 |                   2 |               28.57 |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/descriptors/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/descriptors/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
