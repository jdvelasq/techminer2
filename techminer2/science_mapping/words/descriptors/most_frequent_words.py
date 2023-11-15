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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| descriptors          |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:---------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINTECH              |          1 |    45 |            16 |                  29 |               64.44 |
| TECHNOLOGIES         |          2 |    26 |            11 |                  15 |               57.69 |
| FINANCE              |          3 |    22 |            10 |                  12 |               54.55 |
| INNOVATION           |          4 |    20 |            10 |                  10 |               50    |
| FINANCIAL_TECHNOLOGY |          5 |    19 |             4 |                  15 |               78.95 |
| FINANCIAL_INDUSTRY   |          6 |    18 |            10 |                   8 |               44.44 |
| AUTHOR               |          7 |    18 |             5 |                  13 |               72.22 |
| BANKING              |          8 |    15 |             6 |                   9 |               60    |
| FINANCIAL_SERVICES   |          9 |    14 |             4 |                  10 |               71.43 |
| RESEARCHERS          |         10 |    14 |             7 |                   7 |               50    |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/descriptors/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/descriptors/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
