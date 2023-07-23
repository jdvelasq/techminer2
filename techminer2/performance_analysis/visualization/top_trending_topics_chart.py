# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Top Trending Topics Chart
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.



>>> from techminer2.performance_analysis.visualization import top_trending_topics
>>> file_name = "sphinx/_static/performance_analysis/visualization/top_trending_topics.html"
>>> chart = top_trending_topics_graph(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/performance_analysis/visualization/top_trending_topics.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> r.table_.head()
                                 OCC  ...  percentage_of_docs_in_last_years
author_keywords                       ...                                  
ANTI_MONEY_LAUNDERING              4  ...                              0.50
REGULATORY_TECHNOLOGY (REGTECH)    3  ...                              0.50
REGULATION                         4  ...                              0.25
ACCOUNTABILITY                     2  ...                              0.50
DATA_PROTECTION_OFFICER            2  ...                              0.50
<BLANKLINE>
[5 rows x 10 columns]


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
def top_trending_topics_chart():
    pass


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
#     """Top Trending Topics Graph.  :meta private:"""

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
#         obj,
#         title=title,
#         metric_label="average_growth_rate",
#         field_label=field_label,
#     ).plot_

#     return obj
