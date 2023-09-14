# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Frequent
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
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
>>> print(items.df_.to_markdown()) 
| authors     |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| Arner DW    |          1 |     3 |             3 |                   0 |                   0 |
| Buckley RP  |          2 |     3 |             3 |                   0 |                   0 |
| Barberis JN |          3 |     2 |             2 |                   0 |                   0 |
| Butler T    |          4 |     2 |             2 |                   0 |                   0 |
| Hamdan A    |          5 |     2 |             2 |                   0 |                   0 |
| Turki M     |          6 |     2 |             2 |                   0 |                   0 |
| Lin W       |          7 |     2 |             1 |                   1 |                  50 |
| Singh C     |          8 |     2 |             1 |                   1 |                  50 |
| Brennan R   |          9 |     2 |             2 |                   0 |                   0 |
| Crane M     |         10 |     2 |             2 |                   0 |                   0 |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/authors/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/authors/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
