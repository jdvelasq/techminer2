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
...     field='title_nlp_phrases',
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/title_nlp_phrases/word_trends.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/title_nlp_phrases/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
                               rank_occ  ...  growth_percentage
title_nlp_phrases                        ...                   
REGULATORY_TECHNOLOGY                 1  ...               0.00
ARTIFICIAL_INTELLIGENCE               2  ...              33.33
FINANCIAL_REGULATION                  3  ...               0.00
FINANCIAL_CRIME                       4  ...               0.00
DIGITAL_REGULATORY_COMPLIANCE         5  ...               0.00
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'title_nlp_phrases' field in a scientific bibliography database. \\
Summarize the table below, containing the number of documents before_2022 \\
and between_2022_2023, and sorted by the total number of documents, and \\
delimited by triple backticks. Identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research \\
field. Be sure to provide a concise summary of your findings in no more \\
than 150 words.
<BLANKLINE>
Table:
```
| title_nlp_phrases             |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_TECHNOLOGY         |          1 |     3 |             3 |                   0 |                0    |
| ARTIFICIAL_INTELLIGENCE       |          2 |     3 |             2 |                   1 |               33.33 |
| FINANCIAL_REGULATION          |          3 |     2 |             2 |                   0 |                0    |
| FINANCIAL_CRIME               |          4 |     2 |             2 |                   0 |                0    |
| DIGITAL_REGULATORY_COMPLIANCE |          5 |     1 |             1 |                   0 |                0    |
| UNDERSTANDING_REGTECH         |          6 |     1 |             1 |                   0 |                0    |
| BANK_FAILURES                 |          7 |     1 |             1 |                   0 |                0    |
| CONCEPT_ARTICLE               |          8 |     1 |             1 |                   0 |                0    |
| REALISTIC_PROTECTION          |          9 |     1 |             1 |                   0 |                0    |
| EUROPEAN_UNION                |         10 |     1 |             1 |                   0 |                0    |
| FINANCIAL_RISK                |         11 |     1 |             1 |                   0 |                0    |
| INNOVATIVE_REGTECH_APPROACH   |         12 |     1 |             1 |                   0 |                0    |
| EFFECTIVE_SOLUTIONS           |         13 |     1 |             1 |                   0 |                0    |
| FINANCIAL_DEVELOPMENT         |         14 |     1 |             0 |                   1 |              100    |
| GDPR_REGTECH                  |         15 |     1 |             1 |                   0 |                0    |
| BANK_TREASURY                 |         16 |     1 |             1 |                   0 |                0    |
| DIGITAL_TRANSFORMATION        |         17 |     1 |             1 |                   0 |                0    |
| FINANCIAL_SYSTEM              |         18 |     1 |             1 |                   0 |                0    |
| REGULATORY_TECHNOLOGY_REGTECH |         19 |     1 |             1 |                   0 |                0    |
| AML_COMPLIANCE                |         20 |     1 |             1 |                   0 |                0    |
```
<BLANKLINE>



"""
