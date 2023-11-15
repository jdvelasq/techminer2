# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Local Impact --- G-Index
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
...     metric="g_index",
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
| countries      |   h_index |   g_index |   m_index |
|:---------------|----------:|----------:|----------:|
| United States  |        16 |        10 |      5.33 |
| China          |         8 |         8 |      2    |
| Germany        |         7 |         7 |      2.33 |
| South Korea    |         6 |         6 |      1.5  |
| Australia      |         5 |         5 |      1.67 |
| Switzerland    |         4 |         4 |      1    |
| United Kingdom |         3 |         3 |      1    |
| Netherlands    |         3 |         3 |      1    |
| Denmark        |         2 |         2 |      0.67 |
| Latvia         |         2 |         2 |      0.5  |


>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/g_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/g_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...






"""
