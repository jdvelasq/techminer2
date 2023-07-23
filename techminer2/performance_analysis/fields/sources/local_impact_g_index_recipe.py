# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- G-Index (Recipe)
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> root_dir = "data/regtech/"
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='source_abbr',
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
| source_abbr                   |   h_index |   g_index |   m_index |
|:------------------------------|----------:|----------:|----------:|
| J BANK REGUL                  |         2 |         2 |      0.5  |
| J ECON BUS                    |         1 |         1 |      0.17 |
| NORTHWEST J INTL LAW BUS      |         1 |         1 |      0.14 |
| PALGRAVE STUD DIGIT BUS ENABL |         1 |         1 |      0.2  |
| DUKE LAW J                    |         1 |         1 |      0.12 |
| J RISK FINANC                 |         1 |         1 |      0.17 |
| J MONEY LAUND CONTROL         |         1 |         1 |      0.25 |
| J FINANC CRIME                |         2 |         1 |      0.5  |
| FINANCIAL INNOV               |         1 |         1 |      0.5  |
| ICEIS - PROC INT CONF ENTERP  |         1 |         1 |      0.25 |


>>> items.fig_.write_html("sphinx/_static/performance_analysis/fields/sources/g_index_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/sources/g_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'g_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   h_index |   g_index |   m_index |
|:------------------------------|----------:|----------:|----------:|
| J BANK REGUL                  |         2 |         2 |      0.5  |
| J ECON BUS                    |         1 |         1 |      0.17 |
| NORTHWEST J INTL LAW BUS      |         1 |         1 |      0.14 |
| PALGRAVE STUD DIGIT BUS ENABL |         1 |         1 |      0.2  |
| DUKE LAW J                    |         1 |         1 |      0.12 |
| J RISK FINANC                 |         1 |         1 |      0.17 |
| J MONEY LAUND CONTROL         |         1 |         1 |      0.25 |
| J FINANC CRIME                |         2 |         1 |      0.5  |
| FINANCIAL INNOV               |         1 |         1 |      0.5  |
| ICEIS - PROC INT CONF ENTERP  |         1 |         1 |      0.25 |
```
<BLANKLINE>

"""
