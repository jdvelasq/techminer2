# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Relevant (Recipe)
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| countries      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:---------------|-----------:|----------:|------:|-------------------:|
| United Kingdom |          1 |         1 |     7 |                199 |
| Australia      |          2 |         2 |     7 |                199 |
| United States  |          3 |         4 |     6 |                 59 |
| Ireland        |          4 |         5 |     5 |                 55 |
| China          |          5 |         9 |     5 |                 27 |
| Italy          |          6 |        16 |     5 |                  5 |
| Germany        |          7 |         6 |     4 |                 51 |
| Switzerland    |          8 |         7 |     4 |                 45 |
| Bahrain        |          9 |        11 |     4 |                 19 |
| Hong Kong      |         10 |         3 |     3 |                185 |
| Luxembourg     |         11 |         8 |     2 |                 34 |
| Greece         |         15 |        10 |     1 |                 21 |


>>> items.fig_.write_html("sphinx/_static/performance_analysis/fields/countries/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/countries/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:---------------|-----------:|----------:|------:|-------------------:|
| United Kingdom |          1 |         1 |     7 |                199 |
| Australia      |          2 |         2 |     7 |                199 |
| United States  |          3 |         4 |     6 |                 59 |
| Ireland        |          4 |         5 |     5 |                 55 |
| China          |          5 |         9 |     5 |                 27 |
| Italy          |          6 |        16 |     5 |                  5 |
| Germany        |          7 |         6 |     4 |                 51 |
| Switzerland    |          8 |         7 |     4 |                 45 |
| Bahrain        |          9 |        11 |     4 |                 19 |
| Hong Kong      |         10 |         3 |     3 |                185 |
| Luxembourg     |         11 |         8 |     2 |                 34 |
| Greece         |         15 |        10 |     1 |                 21 |
```
<BLANKLINE>



"""