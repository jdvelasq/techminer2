# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bar Chart
===============================================================================


>>> from techminer2.performance.plots import bar_chart
>>> chart = bar_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     metric_label=None,
...     field_label=None,
...     #
...     # ITEM FILTERS:
...     top_n=20,
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/author_keywords/bar_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/author_keywords/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                       rank_occ  OCC  ...  between_2022_2023  growth_percentage
author_keywords                       ...                                      
REGTECH                       1   28  ...                8.0              28.57
FINTECH                       2   12  ...                2.0              16.67
REGULATORY_TECHNOLOGY         3    7  ...                2.0              28.57
COMPLIANCE                    4    7  ...                2.0              28.57
REGULATION                    5    5  ...                1.0              20.00
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords         |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                 |          1 |    28 |            20 |                   8 |               28.57 |
| FINTECH                 |          2 |    12 |            10 |                   2 |               16.67 |
| REGULATORY_TECHNOLOGY   |          3 |     7 |             5 |                   2 |               28.57 |
| COMPLIANCE              |          4 |     7 |             5 |                   2 |               28.57 |
| REGULATION              |          5 |     5 |             4 |                   1 |               20    |
| ANTI_MONEY_LAUNDERING   |          6 |     5 |             5 |                   0 |                0    |
| FINANCIAL_SERVICES      |          7 |     4 |             3 |                   1 |               25    |
| FINANCIAL_REGULATION    |          8 |     4 |             2 |                   2 |               50    |
| ARTIFICIAL_INTELLIGENCE |          9 |     4 |             3 |                   1 |               25    |
| RISK_MANAGEMENT         |         10 |     3 |             2 |                   1 |               33.33 |
| INNOVATION              |         11 |     3 |             2 |                   1 |               33.33 |
| BLOCKCHAIN              |         12 |     3 |             3 |                   0 |                0    |
| SUPTECH                 |         13 |     3 |             1 |                   2 |               66.67 |
| SEMANTIC_TECHNOLOGIES   |         14 |     2 |             2 |                   0 |                0    |
| DATA_PROTECTION         |         15 |     2 |             1 |                   1 |               50    |
| SMART_CONTRACTS         |         16 |     2 |             2 |                   0 |                0    |
| CHARITYTECH             |         17 |     2 |             1 |                   1 |               50    |
| ENGLISH_LAW             |         18 |     2 |             1 |                   1 |               50    |
| ACCOUNTABILITY          |         19 |     2 |             2 |                   0 |                0    |
| DATA_PROTECTION_OFFICER |         20 |     2 |             2 |                   0 |                0    |
```
<BLANKLINE>


"""
