# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- G-Index
===============================================================================


>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| organizations                                                      |   h_index |   g_index |   m_index |
|:-------------------------------------------------------------------|----------:|----------:|----------:|
| Univ of Hong Kong (HKG)                                            |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)                                               |         2 |         2 |      0.33 |
| Ahlia Univ (BHR)                                                   |         2 |         2 |      0.5  |
| Kingston Bus Sch (GBR)                                             |         1 |         1 |      0.17 |
| FinTech HK, Hong Kong (HKG)                                        |         1 |         1 |      0.14 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         1 |         1 |      0.14 |
| Duke Univ Sch of Law (USA)                                         |         1 |         1 |      0.12 |
| Heinrich-Heine-Univ (DEU)                                          |         1 |         1 |      0.25 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         1 |         1 |      0.25 |
| Univ of Luxembourg (LUX)                                           |         1 |         1 |      0.25 |


>>> items.fig_.write_html("sphinx/_static/performance/contributors/organizations/g_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/contributors/organizations/g_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
