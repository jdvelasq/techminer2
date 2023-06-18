# flake8: noqa
"""
Bar Graph
==============================================================================

* When ``is_trend_analysis == False``, plots the total number of documents 
  in the period of analysis for the most frequent items in a field using a 
  horizontal bar plot. 


* When ``is_trend_analysis == True``, plots the total number of documents
  in the period of analysis for the items with the highest average growth rate 
  in a field using a horizontal bar plot.


Example: Default Usage vs Trend Analysis
------------------------------------------------------------------------------

* Default:

>>> from techminer2 import scientopy
>>> root_dir = "data/regtech/"
>>> r = scientopy.bar_graph(
...     field='author_keywords',
...     top_n=10,
...     is_trend_analysis=False,
...     root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/scientopy__bar_graph_1.html"
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar_graph_1.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.to_markdown())
| author_keywords                 |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:--------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| REGTECH                         |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                          0.142857  |
| FINTECH                         |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                          0.0833333 |
| COMPLIANCE                      |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                          0.142857  |
| REGULATION                      |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                          0.1       |
| FINANCIAL_SERVICES              |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                          0.125     |
| FINANCIAL_REGULATION            |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                          0.25      |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |             3 |                   1 |                 30 |                10 |                            7.5  |                           2.5  |                  -1   |                     0.5 |                          0.125     |
| ARTIFICIAL_INTELLIGENCE         |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                          0.125     |
| ANTI_MONEY_LAUNDERING           |     4 |             4 |                   0 |                 23 |                 4 |                            5.75 |                           1    |                  -1.5 |                     0   |                          0         |
| RISK_MANAGEMENT                 |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                          0.166667  |






* Trend Analysis:

>>> from techminer2 import scientopy
>>> root_dir = "data/regtech/"
>>> r = scientopy.bar_graph(
...     field='author_keywords',
...     top_n=10,
...     is_trend_analysis=True,
...     root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/scientopy__bar_graph_2.html"
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar_graph_1.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.to_markdown())
| author_keywords           |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:--------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| ANNUAL_GENERAL_MEETINGS   |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| BENEFIT                   |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| CHALLENGES                |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| COMPANIES                 |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| COSTS_OF_VOTING           |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| MIFID_II                  |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| ONLINE_SHAREHOLDER_VOTING |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| SHAREHOLDER_MONITORING    |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| COMPLIANCE                |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                           0.142857 |
| FINANCIAL_SERVICES        |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                           0.125    |





>>> print(r.prompt_)
Your task is to generate a short analysis for a scientific research paper. Analyze the table below, delimited by triple backticks, in at most 100 words, for the different items of the field 'author_keywords', providing conclusions about the different columns of the table, and take into account that the columns Before 2022 and Between 2022-2023 represents the number of documents for each item in the indicated time period.
<BLANKLINE>
Table:
```
| author_keywords           |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:--------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| ANNUAL_GENERAL_MEETINGS   |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| BENEFIT                   |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| CHALLENGES                |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| COMPANIES                 |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| COSTS_OF_VOTING           |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| MIFID_II                  |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| ONLINE_SHAREHOLDER_VOTING |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| SHAREHOLDER_MONITORING    |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0.5 |                     0.5 |                           0.5      |
| COMPLIANCE                |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                           0.142857 |
| FINANCIAL_SERVICES        |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                           0.125    |
```
<BLANKLINE>





Example: Time Filter
------------------------------------------------------------------------------

>>> from techminer2 import scientopy
>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/scientopy__bar-3.html"
>>> r = scientopy.bar_graph(
...     field='author_keywords',
...     top_n=10,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-3.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())    
| author_keywords       |   OCC |   Before 2020 |   Between 2020-2021 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:----------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| REGTECH               |    18 |             7 |                  11 |                297 |                69 |                           16.5  |                           3.83 |                  -0.5 |                     5.5 |                           0.305556 |
| FINTECH               |    10 |             6 |                   4 |                235 |                48 |                           23.5  |                           4.8  |                  -1.5 |                     2   |                           0.2      |
| COMPLIANCE            |     5 |             1 |                   4 |                 29 |                 9 |                            5.8  |                           1.8  |                   0   |                     2   |                           0.4      |
| REGULATION            |     4 |             2 |                   2 |                163 |                22 |                           40.75 |                           5.5  |                   0.5 |                     1   |                           0.25     |
| ANTI_MONEY_LAUNDERING |     4 |             0 |                   4 |                 23 |                 4 |                            5.75 |                           1    |                   1.5 |                     2   |                           0.5      |




Example: Custom Items Analysis
------------------------------------------------------------------------------

>>> file_name = "sphinx/_static/scientopy__bar-4.html"
>>> r = scientopy.bar_graph(
...     field='author_keywords',
...     custom_items=[
...         "FINTECH", 
...         "BLOCKCHAIN", 
...         "FINANCIAL_REGULATION", 
...         "MACHINE_LEARNING",
...         "BIG_DATA",
...         "CRYPTOCURRENCY",
...     ],
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-4.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.to_markdown()) 
| author_keywords      |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:---------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| FINTECH              |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                          0.0833333 |
| FINANCIAL_REGULATION |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                          0.25      |
| BLOCKCHAIN           |     3 |             3 |                   0 |                  5 |                 0 |                            1.67 |                           0    |                  -0.5 |                     0   |                          0         |
| BIG_DATA             |     1 |             0 |                   1 |                  3 |                 0 |                            3    |                           0    |                   0   |                     0.5 |                          0.5       |
| MACHINE_LEARNING     |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                          0.5       |



Example: Filters
------------------------------------------------------------------------------


>>> r = scientopy.bar_graph(
...     field='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/scientopy__bar-5.html"
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-5.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())    
| countries      |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:---------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| United Kingdom |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                          0.0714286 |
| Australia      |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                          0         |
| United States  |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                          0.166667  |
| Ireland        |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                          0.1       |
| China          |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                          0.4       |



>>> r = scientopy.bar_graph(
...     field='countries',
...     root_dir=root_dir,
...     countries=['Australia', 'United Kingdom', 'United States'],
... )
>>> file_name = "sphinx/_static/scientopy__bar-6.html"
>>> r.plot_.write_html(file_name)


.. raw:: html

    <iframe src="../_static/scientopy__bar-6.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown()) 
| countries      |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:---------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| United Kingdom |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                          0.0714286 |
| Australia      |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                          0         |
| United States  |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                          0.166667  |
| Hong Kong      |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                          0         |
| Switzerland    |     3 |             2 |                   1 |                 45 |                13 |                           15    |                           4.33 |                   0.5 |                     0.5 |                          0.166667  |



>>> r = scientopy.bar_graph(
...     field='author_keywords',
...     is_trend_analysis=True,
...     top_n=5,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> file_name = "sphinx/_static/scientopy__bar-7.html"
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-7.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.to_markdown()) 
| author_keywords                 |   OCC |   Before 2020 |   Between 2020-2021 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:--------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| ANTI_MONEY_LAUNDERING           |     4 |             0 |                   4 |                 23 |                 4 |                            5.75 |                            1   |                   1.5 |                     2   |                               0.5  |
| REGULATORY_TECHNOLOGY (REGTECH) |     3 |             0 |                   3 |                 29 |                 9 |                            9.67 |                            3   |                   1   |                     1.5 |                               0.5  |
| REGULATION                      |     4 |             2 |                   2 |                163 |                22 |                           40.75 |                            5.5 |                   0.5 |                     1   |                               0.25 |
| ACCOUNTABILITY                  |     2 |             0 |                   2 |                 14 |                 3 |                            7    |                            1.5 |                   0.5 |                     1   |                               0.5  |
| DATA_PROTECTION_OFFICER         |     2 |             0 |                   2 |                 14 |                 3 |                            7    |                            1.5 |                   0.5 |                     1   |                               0.5  |



>>> print(r.prompt_)
Your task is to generate a short analysis for a scientific research paper. Analyze the table below, delimited by triple backticks, in at most 100 words, for the different items of the field 'author_keywords', providing conclusions about the different columns of the table, and take into account that the columns Before 2020 and Between 2020-2021 represents the number of documents for each item in the indicated time period.
<BLANKLINE>
Table:
```
| author_keywords                 |   OCC |   Before 2020 |   Between 2020-2021 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:--------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| ANTI_MONEY_LAUNDERING           |     4 |             0 |                   4 |                 23 |                 4 |                            5.75 |                            1   |                   1.5 |                     2   |                               0.5  |
| REGULATORY_TECHNOLOGY (REGTECH) |     3 |             0 |                   3 |                 29 |                 9 |                            9.67 |                            3   |                   1   |                     1.5 |                               0.5  |
| REGULATION                      |     4 |             2 |                   2 |                163 |                22 |                           40.75 |                            5.5 |                   0.5 |                     1   |                               0.25 |
| ACCOUNTABILITY                  |     2 |             0 |                   2 |                 14 |                 3 |                            7    |                            1.5 |                   0.5 |                     1   |                               0.5  |
| DATA_PROTECTION_OFFICER         |     2 |             0 |                   2 |                 14 |                 3 |                            7    |                            1.5 |                   0.5 |                     1   |                               0.5  |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""

# from .._plots.bar_plot import bar_plot

# from ..classes import ScientoPyGraph
# from ..indicators.indicators_by_field import indicators_by_field
# from ..items import generate_custom_items
# from ..report import bar_chart
# from ..sorting import sort_indicators_by_metric
# from .common import PROMPT, get_default_indicators, get_trend_indicators


# # pylint: disable=too-many-arguments
# # pylint: disable=too-many-locals
# def bar_graph(
#     field,
#     # Specific params:
#     time_window=2,
#     is_trend_analysis=False,
#     title=None,
#     metric_label=None,
#     field_label=None,
#     n_words=100,
#     # Item filters:
#     top_n=None,
#     occ_range=None,
#     gc_range=None,
#     custom_items=None,
#     # Database params:
#     root_dir="./",
#     database="main",
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """ScientoPy Bar Plot."""

#     if is_trend_analysis:
#         return trend_analysis_bar_graph(
#             field=field,
#             # Specific params:
#             time_window=time_window,
#             title=title,
#             metric_label=metric_label,
#             field_label=field_label,
#             n_words=n_words,
#             # Item filters:
#             top_n=top_n,
#             occ_range=occ_range,
#             gc_range=gc_range,
#             custom_items=custom_items,
#             # Database params:
#             root_dir=root_dir,
#             database=database,
#             year_filter=year_filter,
#             cited_by_filter=cited_by_filter,
#             **filters,
#         )

#     return default_bar_graph(
#         field=field,
#         # Specific params:
#         time_window=time_window,
#         title=title,
#         metric_label=metric_label,
#         field_label=field_label,
#         n_words=n_words,
#         # Item filters:
#         top_n=top_n,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         custom_items=custom_items,
#         # Database params:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )


# def default_bar_graph(
#     field,
#     # Specific params:
#     time_window,
#     title,
#     metric_label,
#     field_label,
#     n_words,
#     # Item filters:
#     top_n,
#     occ_range,
#     gc_range,
#     custom_items,
#     # Database params:
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     """ScientoPy Bar Plot."""

#     indicators = get_default_indicators(
#         field=field,
#         # Specific params:
#         time_window=time_window,
#         # Item filters:
#         top_n=top_n,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         custom_items=custom_items,
#         # Database params:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     before = indicators.columns[1]
#     between = indicators.columns[2]

#     obj = ScientoPyGraph()
#     obj.table_ = indicators
#     obj.metric_ = "OCC"
#     obj.field_ = field
#     obj.prompt_ = (
#         PROMPT.format(
#             field=field, before=before, between=between, n_words=n_words
#         )
#         + f"\nTable:\n```\n{indicators.to_markdown()}\n```\n"
#     )
#     obj.plot_ = bar_chart(
#         obj, title=title, metric_label=metric_label, field_label=field_label
#     ).plot_

#     return obj


# def trend_analysis_bar_graph(
#     field,
#     # Specific params:
#     time_window,
#     title,
#     metric_label,
#     field_label,
#     n_words,
#     # Item filters:
#     top_n,
#     occ_range,
#     gc_range,
#     custom_items,
#     # Database params:
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     """ScientoPy Bar Plot."""

#     indicators = get_trend_indicators(
#         field=field,
#         # Specific params:
#         time_window=time_window,
#         # Item filters:
#         top_n=top_n,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         custom_items=custom_items,
#         # Database params:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     before = indicators.columns[1]
#     between = indicators.columns[2]

#     obj = ScientoPyGraph()
#     obj.table_ = indicators
#     obj.metric_ = "average_growth_rate"
#     obj.field_ = field
#     obj.prompt_ = (
#         PROMPT.format(
#             field=field, before=before, between=between, n_words=n_words
#         )
#         + f"\nTable:\n```\n{indicators.to_markdown()}\n```\n"
#     )
#     obj.plot_ = bar_chart(
#         obj, title=title, metric_label=metric_label, field_label=field_label
#     ).plot_

#     return obj
