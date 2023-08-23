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
...     field='nlp_phrases',
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/nlp_phrases/word_trends.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/nlp_phrases/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
                        rank_occ  OCC  ...  between_2022_2023  growth_percentage
nlp_phrases                            ...                                      
REGULATORY_TECHNOLOGY          1   18  ...                5.0              27.78
FINANCIAL_INSTITUTIONS         2   15  ...                4.0              26.67
FINANCIAL_REGULATION           3    7  ...                1.0              14.29
REGULATORY_COMPLIANCE          4    7  ...                1.0              14.29
FINANCIAL_SECTOR               5    7  ...                2.0              28.57
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'nlp_phrases' field in a scientific bibliography database. Summarize \\
the table below, containing the number of documents before_2022 and \\
between_2022_2023, and sorted by the total number of documents, and \\
delimited by triple backticks. Identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research \\
field. Be sure to provide a concise summary of your findings in no more \\
than 150 words.
<BLANKLINE>
Table:
```
| nlp_phrases                 |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:----------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_TECHNOLOGY       |          1 |    18 |            13 |                   5 |               27.78 |
| FINANCIAL_INSTITUTIONS      |          2 |    15 |            11 |                   4 |               26.67 |
| FINANCIAL_REGULATION        |          3 |     7 |             6 |                   1 |               14.29 |
| REGULATORY_COMPLIANCE       |          4 |     7 |             6 |                   1 |               14.29 |
| FINANCIAL_SECTOR            |          5 |     7 |             5 |                   2 |               28.57 |
| ARTIFICIAL_INTELLIGENCE     |          6 |     7 |             4 |                   3 |               42.86 |
| FINANCIAL_SYSTEM            |          7 |     6 |             5 |                   1 |               16.67 |
| GLOBAL_FINANCIAL_CRISIS     |          8 |     6 |             3 |                   3 |               50    |
| FINANCIAL_CRISIS            |          9 |     6 |             6 |                   0 |                0    |
| COMPLIANCE_COSTS            |         10 |     6 |             5 |                   1 |               16.67 |
| FINANCIAL_SERVICES_INDUSTRY |         11 |     5 |             3 |                   2 |               40    |
| INFORMATION_TECHNOLOGY      |         12 |     5 |             4 |                   1 |               20    |
| FINANCIAL_TECHNOLOGY        |         13 |     5 |             4 |                   1 |               20    |
| REGTECH                     |         14 |     5 |             3 |                   2 |               40    |
| REGTECH_SOLUTIONS           |         15 |     5 |             4 |                   1 |               20    |
| TECHNOLOGICAL_SOLUTIONS     |         16 |     5 |             4 |                   1 |               20    |
| FINANCIAL_MARKETS           |         17 |     4 |             2 |                   2 |               50    |
| RISK_MANAGEMENT             |         18 |     4 |             3 |                   1 |               25    |
| AVAILABLE_]                 |         19 |     4 |             4 |                   0 |                0    |
| REGTECH_APPLICATION         |         20 |     4 |             3 |                   1 |               25    |
```
<BLANKLINE>



"""
