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
...     field='index_keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Index Keywords",
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/index_keywords/bar_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/index_keywords/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                        rank_occ  OCC  ...  between_2022_2023  growth_percentage
index_keywords                         ...                                      
REGULATORY_COMPLIANCE          1    9  ...                3.0              33.33
FINANCIAL_INSTITUTIONS         2    6  ...                2.0              33.33
FINANCE                        3    5  ...                2.0              40.00
REGTECH                        4    5  ...                2.0              40.00
ANTI_MONEY_LAUNDERING          5    3  ...                0.0               0.00
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'index_keywords' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| index_keywords                  |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:--------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_COMPLIANCE           |          1 |     9 |             6 |                   3 |               33.33 |
| FINANCIAL_INSTITUTIONS          |          2 |     6 |             4 |                   2 |               33.33 |
| FINANCE                         |          3 |     5 |             3 |                   2 |               40    |
| REGTECH                         |          4 |     5 |             3 |                   2 |               40    |
| ANTI_MONEY_LAUNDERING           |          5 |     3 |             3 |                   0 |                0    |
| FINTECH                         |          6 |     3 |             3 |                   0 |                0    |
| INFORMATION_SYSTEMS             |          7 |     2 |             2 |                   0 |                0    |
| INFORMATION_USE                 |          8 |     2 |             2 |                   0 |                0    |
| SOFTWARE_SOLUTION               |          9 |     2 |             2 |                   0 |                0    |
| SANDBOXES                       |         10 |     2 |             2 |                   0 |                0    |
| FINANCIAL_REGULATION            |         11 |     2 |             1 |                   1 |               50    |
| FINANCIAL_SERVICES_INDUSTRY     |         12 |     2 |             1 |                   1 |               50    |
| LAUNDERING                      |         13 |     2 |             2 |                   0 |                0    |
| BANKING                         |         14 |     2 |             2 |                   0 |                0    |
| FINANCIAL_CRISIS                |         15 |     2 |             1 |                   1 |               50    |
| RISK_MANAGEMENT                 |         16 |     2 |             2 |                   0 |                0    |
| COMMERCE                        |         17 |     2 |             2 |                   0 |                0    |
| CLASSIFICATION (OF_INFORMATION) |         18 |     2 |             1 |                   1 |               50    |
| ARTIFICIAL_INTELLIGENCE         |         19 |     2 |             1 |                   1 |               50    |
| BLOCKCHAIN                      |         20 |     2 |             2 |                   0 |                0    |
```
<BLANKLINE>


"""
