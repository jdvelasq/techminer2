# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Performance Metrics
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
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
>>> print(items.df_.head().to_markdown())
| countries      |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:---------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| United Kingdom |          1 |          1 |          1 |     7 |                199 |                35 |         4 |         3 |      0.67 |
| Australia      |          2 |          2 |          2 |     7 |                199 |                31 |         4 |         3 |      0.57 |
| United States  |          3 |          4 |          5 |     6 |                 59 |                19 |         3 |         2 |      0.38 |
| Ireland        |          4 |          5 |          4 |     5 |                 55 |                22 |         3 |         2 |      0.5  |
| China          |          5 |          9 |         10 |     5 |                 27 |                 5 |         3 |         2 |      0.43 |


>>> items.fig_.write_html("sphinx/_static/performance/contributors/countries/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/countries/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries      |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:---------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| United Kingdom |          1 |          1 |          1 |     7 |                199 |                35 |         4 |         3 |      0.67 |
| Australia      |          2 |          2 |          2 |     7 |                199 |                31 |         4 |         3 |      0.57 |
| United States  |          3 |          4 |          5 |     6 |                 59 |                19 |         3 |         2 |      0.38 |
| Ireland        |          4 |          5 |          4 |     5 |                 55 |                22 |         3 |         2 |      0.5  |
| China          |          5 |          9 |         10 |     5 |                 27 |                 5 |         3 |         2 |      0.43 |
| Italy          |          6 |         16 |         15 |     5 |                  5 |                 2 |         1 |         1 |      0.2  |
| Germany        |          7 |          6 |          6 |     4 |                 51 |                15 |         3 |         2 |      0.5  |
| Switzerland    |          8 |          7 |          7 |     4 |                 45 |                13 |         2 |         2 |      0.29 |
| Bahrain        |          9 |         11 |         13 |     4 |                 19 |                 3 |         2 |         2 |      0.5  |
| Hong Kong      |         10 |          3 |          3 |     3 |                185 |                24 |         3 |         3 |      0.43 |
| Luxembourg     |         11 |          8 |          8 |     2 |                 34 |                 8 |         2 |         2 |      0.5  |
| Greece         |         15 |         10 |          9 |     1 |                 21 |                 8 |         1 |         1 |      0.17 |
```
<BLANKLINE>




"""
