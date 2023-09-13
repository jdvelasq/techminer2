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

>>> from techminer2.performance import performance_metrics
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.head().to_markdown()) 
| authors     |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| Arner DW    |          1 |          1 |          1 |     3 |                185 |                24 |         3 |         3 |      0.43 |
| Buckley RP  |          2 |          2 |          2 |     3 |                185 |                24 |         3 |         3 |      0.43 |
| Barberis JN |          3 |          3 |          3 |     2 |                161 |                19 |         2 |         2 |      0.29 |
| Butler T    |          4 |          5 |          4 |     2 |                 41 |                19 |         2 |         2 |      0.33 |
| Hamdan A    |          5 |         15 |         19 |     2 |                 18 |                 3 |         2 |         2 |      0.5  |


>>> metrics.fig_.write_html("sphinx/_static/performance/contributors/authors/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/authors/most_relevant_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
