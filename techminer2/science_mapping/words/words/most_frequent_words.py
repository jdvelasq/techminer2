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
...     field='words',
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
| words      |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:-----------|-----------:|------:|--------------:|--------------------:|--------------------:|
| fintech    |          1 |    50 |            18 |                  32 |               64    |
| financial  |          2 |    44 |            15 |                  29 |               65.91 |
| ©          |          3 |    42 |            14 |                  28 |               66.67 |
| technology |          4 |    39 |            13 |                  26 |               66.67 |
| new        |          5 |    26 |             9 |                  17 |               65.38 |
| service    |          6 |    26 |            10 |                  16 |               61.54 |
| industry   |          7 |    23 |            11 |                  12 |               52.17 |
| study      |          8 |    23 |             9 |                  14 |               60.87 |
| model      |          9 |    19 |             5 |                  14 |               73.68 |
| innovation |         10 |    19 |             8 |                  11 |               57.89 |

>>> metrics.fig_.write_html("sphinx/_static/analyze/words/words/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/words/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
