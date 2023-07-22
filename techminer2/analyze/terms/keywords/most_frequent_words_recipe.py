# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent Words (Recipe)
===============================================================================


>>> from techminer2.analyze.terms import list_items
>>> items = list_items(
...     #
...     # ITEMS PARAMS:
...     field='keywords',
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
| keywords                |   rank_occ |   OCC |
|:------------------------|-----------:|------:|
| REGTECH                 |          1 |    28 |
| FINTECH                 |          2 |    12 |
| REGULATORY_COMPLIANCE   |          3 |     9 |
| REGULATORY_TECHNOLOGY   |          4 |     8 |
| COMPLIANCE              |          5 |     7 |
| FINANCE                 |          6 |     7 |
| ANTI_MONEY_LAUNDERING   |          7 |     6 |
| ARTIFICIAL_INTELLIGENCE |          8 |     6 |
| FINANCIAL_INSTITUTIONS  |          9 |     6 |
| REGULATION              |         10 |     5 |


>>> items.fig_.write_html("sphinx/_static/analyze/terms/keywords/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/terms/keywords/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'keywords' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| keywords                |   rank_occ |   OCC |
|:------------------------|-----------:|------:|
| REGTECH                 |          1 |    28 |
| FINTECH                 |          2 |    12 |
| REGULATORY_COMPLIANCE   |          3 |     9 |
| REGULATORY_TECHNOLOGY   |          4 |     8 |
| COMPLIANCE              |          5 |     7 |
| FINANCE                 |          6 |     7 |
| ANTI_MONEY_LAUNDERING   |          7 |     6 |
| ARTIFICIAL_INTELLIGENCE |          8 |     6 |
| FINANCIAL_INSTITUTIONS  |          9 |     6 |
| REGULATION              |         10 |     5 |
```
<BLANKLINE>


"""
