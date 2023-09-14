# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Local Impact --- M-Index
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
...     metric="m_index",
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
| countries            |   h_index |   g_index |   m_index |
|:---------------------|----------:|----------:|----------:|
| United Kingdom       |         4 |         3 |      0.67 |
| Australia            |         4 |         3 |      0.57 |
| Ireland              |         3 |         2 |      0.5  |
| Germany              |         3 |         2 |      0.5  |
| Luxembourg           |         2 |         2 |      0.5  |
| Bahrain              |         2 |         2 |      0.5  |
| United Arab Emirates |         2 |         1 |      0.5  |
| Japan                |         1 |         1 |      0.5  |
| Hong Kong            |         3 |         3 |      0.43 |
| China                |         3 |         2 |      0.43 |




>>> items.fig_.write_html("sphinx/_static/analyze/contributors/countries/m_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/m_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
