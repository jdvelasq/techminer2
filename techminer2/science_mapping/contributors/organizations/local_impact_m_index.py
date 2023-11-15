# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- M-Index
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| organizations                                          |   h_index |   g_index |   m_index |
|:-------------------------------------------------------|----------:|----------:|----------:|
| Baylor Univ. (USA)                                     |         2 |         2 |       2   |
| Federal Reserve Bank of Philadelphia (USA)             |         3 |         3 |       1.5 |
| CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU) |         1 |         1 |       1   |
| SKEMA Bus. Sch. (FRA)                                  |         1 |         1 |       1   |
| Univ. of Bremen (DEU)                                  |         1 |         1 |       1   |
| Univ. of Lille Nord de France (FRA)                    |         1 |         1 |       1   |
| Federal Reserve Bank of Chicago (USA)                  |         2 |         2 |       1   |
| Georgia State Univ. (USA)                              |         1 |         1 |       1   |
| Univ. of Zaragoza (ESP)                                |         1 |         1 |       1   |
| Columbia Univ. (USA)                                   |         1 |         1 |       1   |



>>> items.fig_.write_html("sphinx/_static/analyze/contributors/organizations/m_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/m_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
