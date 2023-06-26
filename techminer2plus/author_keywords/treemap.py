# flake8: noqa
"""
TreeMap
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/author_keywords/treemap.html"

>>> import techminer2plus
>>> chart = techminer2plus.publish.author_keywords.treemap(
...    top_n=20,
...    root_dir=root_dir,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/author_keywords/treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

    
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
| author_keywords         |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY   |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE              |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION              |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING   |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES      |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION    |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
| RISK_MANAGEMENT         |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
| INNOVATION              |     3 |             2 |                   1 |                 12 |                 4 |                            4    |                           1.33 |                  -0.5 |                     0.5 |                   0.166667  |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| BLOCKCHAIN              |     3 |             3 |                   0 |                  5 |                 0 |                            1.67 |                           0    |                  -0.5 |                     0   |                   0         |                     2017 |     7 |                        0.71 |         1 |         1 |      0.14 |
| SUPTECH                 |     3 |             1 |                   2 |                  4 |                 2 |                            1.33 |                           0.67 |                   0   |                     1   |                   0.333333  |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
| SEMANTIC_TECHNOLOGIES   |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                   0         |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| DATA_PROTECTION         |     2 |             1 |                   1 |                 27 |                 5 |                           13.5  |                           2.5  |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        6.75 |         2 |         1 |      0.5  |
| SMART_CONTRACTS         |     2 |             2 |                   0 |                 22 |                 8 |                           11    |                           4    |                   0   |                     0   |                   0         |                     2017 |     7 |                        3.14 |         1 |         1 |      0.14 |
| CHARITYTECH             |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| ENGLISH_LAW             |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| ACCOUNTABILITY          |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                   0         |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| DATA_PROTECTION_OFFICER |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                   0         |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""
# from ... import list_items
# from ...report import treemap as visualize_treemap

FIELD = "author_keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def treemap(
    title=None,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Makes a treemap."""

    obj = list_items(
        field=FIELD,
        root_dir=root_dir,
        database=database,
        metric="OCC",
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return visualize_treemap(
        obj,
        title=title,
    )
