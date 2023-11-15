# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Performance Metrics
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> metrics = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="OCCGC",
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
>>> print(metrics.df_.head().to_markdown()) 
| authors     |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| Jagtiani J. |          1 |         17 |         16 |     3 |                317 |                 2 |         3 |         3 |      1.5  |
| Gomber P.   |          2 |          1 |          1 |     2 |               1065 |                 7 |         2 |         2 |      0.67 |
| Hornuf L.   |          3 |         13 |         15 |     2 |                358 |                 2 |         2 |         2 |      0.67 |
| Gai K.      |          4 |         14 |         26 |     2 |                323 |                 1 |         2 |         2 |      0.67 |
| Qiu M.      |          5 |         15 |         27 |     2 |                323 |                 1 |         2 |         2 |      0.67 |

>>> metrics.fig_.write_html("sphinx/_static/analyze/contributors/authors/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/authors/most_relevant_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
