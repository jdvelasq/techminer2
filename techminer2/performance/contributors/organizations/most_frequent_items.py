# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent
===============================================================================

>>> from techminer2.performance_analysis import performance_metrics
>>> items = item_metrics(
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
| organizations                                                      |   rank_occ |   OCC |
|:-------------------------------------------------------------------|-----------:|------:|
| Univ of Hong Kong (HKG)                                            |          1 |     3 |
| Univ Coll Cork (IRL)                                               |          2 |     3 |
| Ahlia Univ (BHR)                                                   |          3 |     3 |
| Coventry Univ (GBR)                                                |          4 |     2 |
| Univ of Westminster (GBR)                                          |          5 |     2 |
| Dublin City Univ (IRL)                                             |          6 |     2 |
| Politec di Milano (ITA)                                            |          7 |     2 |
| Kingston Bus Sch (GBR)                                             |          8 |     1 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |     1 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |     1 |


>>> items.fig_.write_html("sphinx/_static/performance/organizations/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/organizations/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                                      |   rank_occ |   OCC |
|:-------------------------------------------------------------------|-----------:|------:|
| Univ of Hong Kong (HKG)                                            |          1 |     3 |
| Univ Coll Cork (IRL)                                               |          2 |     3 |
| Ahlia Univ (BHR)                                                   |          3 |     3 |
| Coventry Univ (GBR)                                                |          4 |     2 |
| Univ of Westminster (GBR)                                          |          5 |     2 |
| Dublin City Univ (IRL)                                             |          6 |     2 |
| Politec di Milano (ITA)                                            |          7 |     2 |
| Kingston Bus Sch (GBR)                                             |          8 |     1 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |     1 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |     1 |
```
<BLANKLINE>


"""
