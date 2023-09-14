# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| organizations                                                      |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:-------------------------------------------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| Univ of Hong Kong (HKG)                                            |          1 |     3 |             3 |                   0 |                0    |
| Univ Coll Cork (IRL)                                               |          2 |     3 |             2 |                   1 |               33.33 |
| Ahlia Univ (BHR)                                                   |          3 |     3 |             2 |                   1 |               33.33 |
| Coventry Univ (GBR)                                                |          4 |     2 |             1 |                   1 |               50    |
| Univ of Westminster (GBR)                                          |          5 |     2 |             1 |                   1 |               50    |
| Dublin City Univ (IRL)                                             |          6 |     2 |             2 |                   0 |                0    |
| Politec di Milano (ITA)                                            |          7 |     2 |             1 |                   1 |               50    |
| Kingston Bus Sch (GBR)                                             |          8 |     1 |             1 |                   0 |                0    |
| FinTech HK, Hong Kong (HKG)                                        |          9 |     1 |             1 |                   0 |                0    |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |     1 |             1 |                   0 |                0    |




>>> items.fig_.write_html("sphinx/_static/performance/contributors/organizations/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/contributors/organizations/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
