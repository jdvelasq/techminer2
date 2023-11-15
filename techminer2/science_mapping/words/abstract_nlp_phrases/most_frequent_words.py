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
| abstract_nlp_phrases   |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:-----------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINTECH                |          1 |    32 |            11 |                  21 |               65.62 |
| TECHNOLOGIES           |          2 |    23 |             9 |                  14 |               60.87 |
| AUTHOR                 |          3 |    18 |             5 |                  13 |               72.22 |
| FINANCIAL_TECHNOLOGY   |          4 |    17 |             3 |                  14 |               82.35 |
| FINANCIAL_INDUSTRY     |          5 |    16 |             9 |                   7 |               43.75 |
| BANKING                |          6 |    14 |             5 |                   9 |               64.29 |
| FINANCE                |          7 |    13 |             7 |                   6 |               46.15 |
| RESEARCHERS            |          8 |    13 |             6 |                   7 |               53.85 |
| INNOVATION             |          9 |    12 |             5 |                   7 |               58.33 |
| PAPER                  |         10 |    12 |             5 |                   7 |               58.33 |


>>> metrics.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
