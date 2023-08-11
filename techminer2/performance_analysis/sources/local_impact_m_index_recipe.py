# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- M-Index
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> root_dir = "data/regtech/"
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='source_abbr',
...     metric="m_index",
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
| source_abbr              |   h_index |   g_index |   m_index |
|:-------------------------|----------:|----------:|----------:|
| J BANK REGUL             |         2 |         2 |      0.5  |
| J FINANC CRIME           |         2 |         1 |      0.5  |
| FINANCIAL INNOV          |         1 |         1 |      0.5  |
| EUR J RISK REGUL         |         1 |         1 |      0.5  |
| DECIS SUPPORT SYST       |         1 |         1 |      0.5  |
| J IND BUS ECON           |         1 |         1 |      0.5  |
| LECT NOTES NETWORKS SYST |         1 |         1 |      0.5  |
| ADV INTELL SYS COMPUT    |         1 |         1 |      0.33 |
| J ANTITRUST ENFORC       |         1 |         1 |      0.33 |
| ACM INT CONF PROC SER    |         1 |         1 |      0.33 |



>>> items.fig_.write_html("sphinx/_static/performance/sources/m_index_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/sources/m_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'm_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr              |   h_index |   g_index |   m_index |
|:-------------------------|----------:|----------:|----------:|
| J BANK REGUL             |         2 |         2 |      0.5  |
| J FINANC CRIME           |         2 |         1 |      0.5  |
| FINANCIAL INNOV          |         1 |         1 |      0.5  |
| EUR J RISK REGUL         |         1 |         1 |      0.5  |
| DECIS SUPPORT SYST       |         1 |         1 |      0.5  |
| J IND BUS ECON           |         1 |         1 |      0.5  |
| LECT NOTES NETWORKS SYST |         1 |         1 |      0.5  |
| ADV INTELL SYS COMPUT    |         1 |         1 |      0.33 |
| J ANTITRUST ENFORC       |         1 |         1 |      0.33 |
| ACM INT CONF PROC SER    |         1 |         1 |      0.33 |
```
<BLANKLINE>


"""
