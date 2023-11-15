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
| countries     |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:--------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| United States |          1 |          1 |          2 |    16 |               3189 |                 8 |        16 |        10 |      5.33 |
| China         |          2 |          4 |          4 |     8 |               1085 |                 4 |         8 |         8 |      2    |
| Germany       |          3 |          2 |          1 |     7 |               1814 |                11 |         7 |         7 |      2.33 |
| South Korea   |          4 |          3 |          3 |     6 |               1192 |                 8 |         6 |         6 |      1.5  |
| Australia     |          5 |          5 |          7 |     5 |                783 |                 3 |         5 |         5 |      1.67 |

    
>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
