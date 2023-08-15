# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Frequent
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='countries',
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
| countries      |   rank_occ |   OCC |
|:---------------|-----------:|------:|
| United Kingdom |          1 |     7 |
| Australia      |          2 |     7 |
| United States  |          3 |     6 |
| Ireland        |          4 |     5 |
| China          |          5 |     5 |
| Italy          |          6 |     5 |
| Germany        |          7 |     4 |
| Switzerland    |          8 |     4 |
| Bahrain        |          9 |     4 |
| Hong Kong      |         10 |     3 |


>>> items.fig_.write_html("sphinx/_static/performance/contributors/countries/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/countries/most_frequent_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
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
| countries      |   rank_occ |   OCC |
|:---------------|-----------:|------:|
| United Kingdom |          1 |     7 |
| Australia      |          2 |     7 |
| United States  |          3 |     6 |
| Ireland        |          4 |     5 |
| China          |          5 |     5 |
| Italy          |          6 |     5 |
| Germany        |          7 |     4 |
| Switzerland    |          8 |     4 |
| Bahrain        |          9 |     4 |
| Hong Kong      |         10 |     3 |
```
<BLANKLINE>



"""
