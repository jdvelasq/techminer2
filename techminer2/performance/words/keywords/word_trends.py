# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Word Trends
===============================================================================


>>> from techminer2.performance.plots import word_trends
>>> chart = word_trends(
...     #
...     # ITEMS PARAMS:
...     field='keywords',
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     #
...     # CHART PARAMS:
...     title="Total Number of Documents, with Percentage of Documents Published in the Last Years",
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/keywords/word_trends.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/keywords/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
                       rank_occ  OCC  ...  between_2022_2023  growth_percentage
keywords                              ...                                      
REGTECH                       1   28  ...                8.0              28.57
FINTECH                       2   12  ...                2.0              16.67
REGULATORY_COMPLIANCE         3    9  ...                3.0              33.33
REGULATORY_TECHNOLOGY         4    8  ...                3.0              37.50
COMPLIANCE                    5    7  ...                2.0              28.57
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'keywords' field in a scientific bibliography database. Summarize the \\
table below, containing the number of documents before_2022 and \\
between_2022_2023, and sorted by the total number of documents, and \\
delimited by triple backticks. Identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research \\
field. Be sure to provide a concise summary of your findings in no more \\
than 150 words.
<BLANKLINE>
Table:
```
| keywords                |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                 |          1 |    28 |            20 |                   8 |               28.57 |
| FINTECH                 |          2 |    12 |            10 |                   2 |               16.67 |
| REGULATORY_COMPLIANCE   |          3 |     9 |             6 |                   3 |               33.33 |
| REGULATORY_TECHNOLOGY   |          4 |     8 |             5 |                   3 |               37.5  |
| COMPLIANCE              |          5 |     7 |             5 |                   2 |               28.57 |
| FINANCE                 |          6 |     7 |             4 |                   3 |               42.86 |
| ANTI_MONEY_LAUNDERING   |          7 |     6 |             6 |                   0 |                0    |
| ARTIFICIAL_INTELLIGENCE |          8 |     6 |             4 |                   2 |               33.33 |
| FINANCIAL_INSTITUTIONS  |          9 |     6 |             4 |                   2 |               33.33 |
| REGULATION              |         10 |     5 |             4 |                   1 |               20    |
| FINANCIAL_REGULATION    |         11 |     5 |             2 |                   3 |               60    |
| RISK_MANAGEMENT         |         12 |     5 |             4 |                   1 |               20    |
| FINANCIAL_SERVICES      |         13 |     4 |             3 |                   1 |               25    |
| SMART_CONTRACTS         |         14 |     3 |             3 |                   0 |                0    |
| INNOVATION              |         15 |     3 |             2 |                   1 |               33.33 |
| BLOCKCHAIN              |         16 |     3 |             3 |                   0 |                0    |
| SUPTECH                 |         17 |     3 |             1 |                   2 |               66.67 |
| SEMANTIC_TECHNOLOGIES   |         18 |     2 |             2 |                   0 |                0    |
| DATA_PROTECTION         |         19 |     2 |             1 |                   1 |               50    |
| CHARITYTECH             |         20 |     2 |             1 |                   1 |               50    |
```
<BLANKLINE>



"""
