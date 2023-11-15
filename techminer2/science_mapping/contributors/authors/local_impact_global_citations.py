# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Local Impact --- Global Citations
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="global_citations",
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
| authors       |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:--------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| Gomber P.     |          1 |          1 |               1065 |                 7 |                           532.5 |                            3.5 |                       355   |
| Kauffman R.J. |          2 |          5 |                576 |                 3 |                           576   |                            3   |                       288   |
| Parker C.     |          3 |          6 |                576 |                 3 |                           576   |                            3   |                       288   |
| Weber B.W.    |          4 |          7 |                576 |                 3 |                           576   |                            3   |                       288   |
| Lee I.        |          5 |         13 |                557 |                 2 |                           557   |                            2   |                       278.5 |
| Shin Y.J.     |          6 |         14 |                557 |                 2 |                           557   |                            2   |                       278.5 |
| Koch J.-A.    |          7 |          2 |                489 |                 4 |                           489   |                            4   |                       163   |
| Siering M.    |          8 |          3 |                489 |                 4 |                           489   |                            4   |                       163   |
| Buchak G.     |          9 |         53 |                390 |                 0 |                           390   |                            0   |                       195   |
| Matvos G.     |         10 |         54 |                390 |                 0 |                           390   |                            0   |                       195   |

>>> items.fig_.write_html("sphinx/_static/analyze/contributors/authors/global_citations_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/authors/global_citations_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task ...


"""
