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
...     field='descriptors',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Descriptors",
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/descriptors/bar_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/descriptors/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                        rank_occ  OCC  ...  between_2022_2023  growth_percentage
descriptors                            ...                                      
REGTECH                        1   29  ...                9.0              31.03
REGULATORY_TECHNOLOGY          2   20  ...                6.0              30.00
FINANCIAL_INSTITUTIONS         3   16  ...                4.0              25.00
REGULATORY_COMPLIANCE          4   15  ...                3.0              20.00
FINANCIAL_REGULATION           5   12  ...                4.0              33.33
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'descriptors' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| descriptors                 |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:----------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                     |          1 |    29 |            20 |                   9 |               31.03 |
| REGULATORY_TECHNOLOGY       |          2 |    20 |            14 |                   6 |               30    |
| FINANCIAL_INSTITUTIONS      |          3 |    16 |            12 |                   4 |               25    |
| REGULATORY_COMPLIANCE       |          4 |    15 |            12 |                   3 |               20    |
| FINANCIAL_REGULATION        |          5 |    12 |             8 |                   4 |               33.33 |
| FINTECH                     |          6 |    12 |            10 |                   2 |               16.67 |
| ARTIFICIAL_INTELLIGENCE     |          7 |     8 |             5 |                   3 |               37.5  |
| FINANCIAL_SECTOR            |          8 |     7 |             5 |                   2 |               28.57 |
| FINANCIAL_CRISIS            |          9 |     7 |             6 |                   1 |               14.29 |
| COMPLIANCE                  |         10 |     7 |             5 |                   2 |               28.57 |
| FINANCE                     |         11 |     7 |             4 |                   3 |               42.86 |
| FINANCIAL_SYSTEM            |         12 |     6 |             5 |                   1 |               16.67 |
| FINANCIAL_SERVICES          |         13 |     6 |             5 |                   1 |               16.67 |
| INFORMATION_TECHNOLOGY      |         14 |     6 |             4 |                   2 |               33.33 |
| GLOBAL_FINANCIAL_CRISIS     |         15 |     6 |             3 |                   3 |               50    |
| FINANCIAL_TECHNOLOGY        |         16 |     6 |             5 |                   1 |               16.67 |
| ANTI_MONEY_LAUNDERING       |         17 |     6 |             6 |                   0 |                0    |
| COMPLIANCE_COSTS            |         18 |     6 |             5 |                   1 |               16.67 |
| TECHNOLOGICAL_SOLUTIONS     |         19 |     6 |             4 |                   2 |               33.33 |
| FINANCIAL_SERVICES_INDUSTRY |         20 |     5 |             3 |                   2 |               40    |
```
<BLANKLINE>



"""
