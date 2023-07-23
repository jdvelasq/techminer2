# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Frequent Words (Recipe)
===============================================================================


>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='index_keywords',
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
| index_keywords         |   rank_occ |   OCC |
|:-----------------------|-----------:|------:|
| REGULATORY_COMPLIANCE  |          1 |     9 |
| FINANCIAL_INSTITUTIONS |          2 |     6 |
| FINANCE                |          3 |     5 |
| REGTECH                |          4 |     5 |
| ANTI_MONEY_LAUNDERING  |          5 |     3 |
| FINTECH                |          6 |     3 |
| INFORMATION_SYSTEMS    |          7 |     2 |
| INFORMATION_USE        |          8 |     2 |
| SOFTWARE_SOLUTION      |          9 |     2 |
| SANDBOXES              |         10 |     2 |


>>> items.fig_.write_html("sphinx/_static/performance_analysis/fields/index_keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/index_keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'index_keywords' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| index_keywords         |   rank_occ |   OCC |
|:-----------------------|-----------:|------:|
| REGULATORY_COMPLIANCE  |          1 |     9 |
| FINANCIAL_INSTITUTIONS |          2 |     6 |
| FINANCE                |          3 |     5 |
| REGTECH                |          4 |     5 |
| ANTI_MONEY_LAUNDERING  |          5 |     3 |
| FINTECH                |          6 |     3 |
| INFORMATION_SYSTEMS    |          7 |     2 |
| INFORMATION_USE        |          8 |     2 |
| SOFTWARE_SOLUTION      |          9 |     2 |
| SANDBOXES              |         10 |     2 |
```
<BLANKLINE>

"""
