# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Relevant
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='organizations',
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
>>> print(items.df_.to_markdown())
| organizations                                                      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:-------------------------------------------------------------------|-----------:|----------:|------:|-------------------:|
| Univ of Hong Kong (HKG)                                            |          1 |         1 |     3 |                185 |
| Univ Coll Cork (IRL)                                               |          2 |         5 |     3 |                 41 |
| Ahlia Univ (BHR)                                                   |          3 |        16 |     3 |                 19 |
| Coventry Univ (GBR)                                                |          4 |        17 |     2 |                 17 |
| Univ of Westminster (GBR)                                          |          5 |        18 |     2 |                 17 |
| Dublin City Univ (IRL)                                             |          6 |        19 |     2 |                 14 |
| Politec di Milano (ITA)                                            |          7 |        50 |     2 |                  2 |
| Kingston Bus Sch (GBR)                                             |          8 |         2 |     1 |                153 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |         3 |     1 |                150 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |         4 |     1 |                150 |
| Duke Univ Sch of Law (USA)                                         |         11 |         6 |     1 |                 30 |
| Heinrich-Heine-Univ (DEU)                                          |         12 |         7 |     1 |                 24 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         13 |         8 |     1 |                 24 |
| Univ of Luxembourg (LUX)                                           |         14 |         9 |     1 |                 24 |
| Univ of Zurich (CHE)                                               |         15 |        10 |     1 |                 24 |



>>> items.fig_.write_html("sphinx/_static/performance/organizations/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/organizations/most_relevant_chart.html" 
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
| organizations                                                      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:-------------------------------------------------------------------|-----------:|----------:|------:|-------------------:|
| Univ of Hong Kong (HKG)                                            |          1 |         1 |     3 |                185 |
| Univ Coll Cork (IRL)                                               |          2 |         5 |     3 |                 41 |
| Ahlia Univ (BHR)                                                   |          3 |        16 |     3 |                 19 |
| Coventry Univ (GBR)                                                |          4 |        17 |     2 |                 17 |
| Univ of Westminster (GBR)                                          |          5 |        18 |     2 |                 17 |
| Dublin City Univ (IRL)                                             |          6 |        19 |     2 |                 14 |
| Politec di Milano (ITA)                                            |          7 |        50 |     2 |                  2 |
| Kingston Bus Sch (GBR)                                             |          8 |         2 |     1 |                153 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |         3 |     1 |                150 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |         4 |     1 |                150 |
| Duke Univ Sch of Law (USA)                                         |         11 |         6 |     1 |                 30 |
| Heinrich-Heine-Univ (DEU)                                          |         12 |         7 |     1 |                 24 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         13 |         8 |     1 |                 24 |
| Univ of Luxembourg (LUX)                                           |         14 |         9 |     1 |                 24 |
| Univ of Zurich (CHE)                                               |         15 |        10 |     1 |                 24 |
```
<BLANKLINE>


"""
