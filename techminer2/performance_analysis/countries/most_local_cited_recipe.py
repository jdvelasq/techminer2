# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
...     metric="local_citations",
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
| countries      |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:---------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| United Kingdom |         1 |                199 |                35 |                           28.43 |                           5    |                       33.17 |
| Australia      |         2 |                199 |                30 |                           28.43 |                           4.29 |                       28.43 |
| Hong Kong      |         3 |                185 |                23 |                           61.67 |                           7.67 |                       26.43 |
| Ireland        |         5 |                 55 |                22 |                           11    |                           4.4  |                        9.17 |
| United States  |         4 |                 59 |                19 |                            9.83 |                           3.17 |                        7.38 |
| Germany        |         6 |                 51 |                14 |                           12.75 |                           3.5  |                        8.5  |
| Switzerland    |         7 |                 45 |                12 |                           11.25 |                           3    |                        6.43 |
| Greece         |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Luxembourg     |         8 |                 34 |                 7 |                           17    |                           3.5  |                        8.5  |
| China          |         9 |                 27 |                 5 |                            5.4  |                           1    |                        3.86 |


>>> items.fig_.write_html("sphinx/_static/performance/countries/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/countries/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'local_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries      |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:---------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| United Kingdom |         1 |                199 |                35 |                           28.43 |                           5    |                       33.17 |
| Australia      |         2 |                199 |                30 |                           28.43 |                           4.29 |                       28.43 |
| Hong Kong      |         3 |                185 |                23 |                           61.67 |                           7.67 |                       26.43 |
| Ireland        |         5 |                 55 |                22 |                           11    |                           4.4  |                        9.17 |
| United States  |         4 |                 59 |                19 |                            9.83 |                           3.17 |                        7.38 |
| Germany        |         6 |                 51 |                14 |                           12.75 |                           3.5  |                        8.5  |
| Switzerland    |         7 |                 45 |                12 |                           11.25 |                           3    |                        6.43 |
| Greece         |        10 |                 21 |                 8 |                           21    |                           8    |                        3.5  |
| Luxembourg     |         8 |                 34 |                 7 |                           17    |                           3.5  |                        8.5  |
| China          |         9 |                 27 |                 5 |                            5.4  |                           1    |                        3.86 |
```
<BLANKLINE>




"""
