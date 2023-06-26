# flake8: noqa
"""
Most Relevant Countries
===============================================================================



>>> FILE_NAME = "sphinx/_static/use_cases/countries/most_relevant_items.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.countries.most_relevant_items(
...     top_n=10,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/countries/most_relevant_items.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
                rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
countries                               ...                           
United Kingdom         1        1    7  ...      4.0      3.0     0.67
Australia              2        2    7  ...      4.0      3.0     0.57
United States          3        4    6  ...      3.0      2.0     0.38
Ireland                4        5    5  ...      3.0      2.0     0.50
China                  5        9    5  ...      3.0      2.0     0.43
<BLANKLINE>
[5 rows x 18 columns]


>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries      |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| United Kingdom |          1 |         1 |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33.17 |         4 |         3 |      0.67 |
| Australia      |          2 |         2 |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                   0         |                     2017 |     7 |                       28.43 |         4 |         3 |      0.57 |
| United States  |          3 |         4 |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                   0.166667  |                     2016 |     8 |                        7.38 |         3 |         2 |      0.38 |
| Ireland        |          4 |         5 |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                        9.17 |         3 |         2 |      0.5  |
| China          |          5 |         9 |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                   0.4       |                     2017 |     7 |                        3.86 |         3 |         2 |      0.43 |
| Italy          |          6 |        16 |     5 |             3 |                   2 |                  5 |                 2 |                            1    |                           0.4  |                   0   |                     1   |                   0.2       |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| Germany        |          7 |         6 |     4 |             3 |                   1 |                 51 |                17 |                           12.75 |                           4.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        8.5  |         3 |         2 |      0.5  |
| Switzerland    |          8 |         7 |     4 |             3 |                   1 |                 45 |                13 |                           11.25 |                           3.25 |                   0.5 |                     0.5 |                   0.125     |                     2017 |     7 |                        6.43 |         2 |         2 |      0.29 |
| Bahrain        |          9 |        11 |     4 |             3 |                   1 |                 19 |                 5 |                            4.75 |                           1.25 |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Hong Kong      |         10 |         3 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                   0         |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Luxembourg     |         11 |         8 |     2 |             2 |                   0 |                 34 |                 8 |                           17    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        8.5  |         2 |         2 |      0.5  |
| Greece         |         15 |        10 |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                   0         |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
# from ... import list_items
# from ...graphing_lib import ranking_chart

FIELD = "countries"
METRIC = "OCCGC"
TITLE = "Most Relevant Countries"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_relevant_items(
    #
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most Relevant Items."""

    if title is None:
        title = TITLE

    itemslist = list_items(
        field=FIELD,
        metric=METRIC,
        #
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return ranking_chart(
        itemslist=itemslist,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
