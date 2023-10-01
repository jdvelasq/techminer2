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
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
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
>>> print(items.df_.head().to_markdown()) 
| countries      |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:---------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| United Kingdom |          1 |          1 |          1 |     7 |                199 |                35 |         4 |         3 |      0.67 |
| Australia      |          2 |          2 |          2 |     7 |                199 |                31 |         4 |         3 |      0.57 |
| United States  |          3 |          4 |          5 |     6 |                 59 |                19 |         3 |         2 |      0.38 |
| Ireland        |          4 |          5 |          4 |     5 |                 55 |                22 |         3 |         2 |      0.5  |
| China          |          5 |          9 |         10 |     5 |                 27 |                 5 |         3 |         2 |      0.43 |

    
>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
