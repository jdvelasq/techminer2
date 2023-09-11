# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_relevant_sources_recipe:

Most Relevant
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> root_dir = "data/regtech/"
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='source_abbr',
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
| source_abbr                   |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |          1 |          3 |          4 |     2 |                 35 |                 9 |         2 |         2 |      0.5  |
| J FINANC CRIME                |          2 |          8 |          8 |     2 |                 13 |                 4 |         2 |         1 |      0.5  |
| STUD COMPUT INTELL            |          3 |         28 |         23 |     2 |                  1 |                 1 |         1 |         1 |      0.33 |
| FOSTER INNOVCOMPET WITH FINTE |          4 |         30 |         31 |     2 |                  1 |                 0 |         1 |         1 |      0.25 |
| INT CONF INF TECHNOL SYST INN |          5 |         37 |         37 |     2 |                  0 |                 0 |         0 |         0 |      0    |



>>> items.fig_.write_html("sphinx/_static/performance/contributors/sources/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/sources/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |          1 |          3 |          4 |     2 |                 35 |                 9 |         2 |         2 |      0.5  |
| J FINANC CRIME                |          2 |          8 |          8 |     2 |                 13 |                 4 |         2 |         1 |      0.5  |
| STUD COMPUT INTELL            |          3 |         28 |         23 |     2 |                  1 |                 1 |         1 |         1 |      0.33 |
| FOSTER INNOVCOMPET WITH FINTE |          4 |         30 |         31 |     2 |                  1 |                 0 |         1 |         1 |      0.25 |
| INT CONF INF TECHNOL SYST INN |          5 |         37 |         37 |     2 |                  0 |                 0 |         0 |         0 |      0    |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |         38 |         38 |     2 |                  0 |                 0 |         0 |         0 |      0    |
| J ECON BUS                    |          7 |          1 |          1 |     1 |                153 |                17 |         1 |         1 |      0.17 |
| NORTHWEST J INTL LAW BUS      |          8 |          2 |          2 |     1 |                150 |                16 |         1 |         1 |      0.14 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |          4 |          3 |     1 |                 33 |                14 |         1 |         1 |      0.2  |
| DUKE LAW J                    |         10 |          5 |          5 |     1 |                 30 |                 8 |         1 |         1 |      0.12 |
| J RISK FINANC                 |         11 |          6 |          6 |     1 |                 21 |                 8 |         1 |         1 |      0.17 |
| J MONEY LAUND CONTROL         |         12 |          7 |          9 |     1 |                 14 |                 3 |         1 |         1 |      0.25 |
| FINANCIAL INNOV               |         13 |          9 |         18 |     1 |                 13 |                 1 |         1 |         1 |      0.5  |
| ICEIS - PROC INT CONF ENTERP  |         14 |         10 |         10 |     1 |                 12 |                 3 |         1 |         1 |      0.25 |
```
<BLANKLINE>



"""
