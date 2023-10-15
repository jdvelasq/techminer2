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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown()) 
| authors       |   rank_occ |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |
|:--------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| Jagtiani J.   |          1 |     3 |             0 |                   3 |                 100 |
| Gomber P.     |          2 |     2 |             1 |                   1 |                  50 |
| Hornuf L.     |          3 |     2 |             1 |                   1 |                  50 |
| Gai K.        |          4 |     2 |             1 |                   1 |                  50 |
| Qiu M.        |          5 |     2 |             1 |                   1 |                  50 |
| Sun X./3      |          6 |     2 |             1 |                   1 |                  50 |
| Lemieux C.    |          7 |     2 |             0 |                   2 |                 100 |
| Dolata M.     |          8 |     2 |             2 |                   0 |                   0 |
| Schwabe G.    |          9 |     2 |             2 |                   0 |                   0 |
| Zavolokina L. |         10 |     2 |             2 |                   0 |                   0 |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/authors/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/authors/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
