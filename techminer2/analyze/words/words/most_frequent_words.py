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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.to_markdown())
| words                  |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:-----------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                |          1 |    48 |            36 |                  12 |               25    |
| REGULATORS             |          2 |    30 |            21 |                   9 |               30    |
| NEW_TECHNOLOGIES       |          3 |    22 |            15 |                   7 |               31.82 |
| REGULATORY_TECHNOLOGY  |          4 |    20 |            14 |                   6 |               30    |
| COMPLIANCE             |          5 |    18 |            15 |                   3 |               16.67 |
| BANK                   |          6 |    18 |            14 |                   4 |               22.22 |
| FINANCIAL_INSTITUTIONS |          7 |    16 |            12 |                   4 |               25    |
| CHALLENGE              |          8 |    16 |            13 |                   3 |               18.75 |
| PAPER                  |          9 |    15 |            11 |                   4 |               26.67 |
| APPLICATION            |         10 |    15 |            10 |                   5 |               33.33 |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/words/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/words/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
