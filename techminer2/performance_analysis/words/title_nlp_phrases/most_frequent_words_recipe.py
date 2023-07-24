# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent Words (Recipe)
===============================================================================


>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='title_nlp_phrases',
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
| title_nlp_phrases       |   rank_occ |   OCC |
|:------------------------|-----------:|------:|
| REGULATORY_TECHNOLOGY   |          1 |     3 |
| ARTIFICIAL_INTELLIGENCE |          2 |     3 |
| FINANCIAL_REGULATION    |          3 |     2 |
| FINANCIAL_CRIME         |          4 |     2 |
| EUROPEAN_UNION          |          5 |     1 |
| FINANCIAL_RISK          |          6 |     1 |
| EFFECTIVE_SOLUTIONS     |          7 |     1 |
| FINANCIAL_DEVELOPMENT   |          8 |     1 |
| BANK_TREASURY           |          9 |     1 |
| DIGITAL_TRANSFORMATION  |         10 |     1 |



>>> items.fig_.write_html("sphinx/_static/performance_analysis/fields/title_nlp_phrases/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/title_nlp_phrases/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'title_nlp_phrases' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| title_nlp_phrases       |   rank_occ |   OCC |
|:------------------------|-----------:|------:|
| REGULATORY_TECHNOLOGY   |          1 |     3 |
| ARTIFICIAL_INTELLIGENCE |          2 |     3 |
| FINANCIAL_REGULATION    |          3 |     2 |
| FINANCIAL_CRIME         |          4 |     2 |
| EUROPEAN_UNION          |          5 |     1 |
| FINANCIAL_RISK          |          6 |     1 |
| EFFECTIVE_SOLUTIONS     |          7 |     1 |
| FINANCIAL_DEVELOPMENT   |          8 |     1 |
| BANK_TREASURY           |          9 |     1 |
| DIGITAL_TRANSFORMATION  |         10 |     1 |
```
<BLANKLINE>


"""
