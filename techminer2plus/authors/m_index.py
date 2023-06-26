# flake8: noqa
"""
M-Index
===============================================================================



>>> FILE_NAME = "sphinx/_static/use_cases/authors/m_index.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.authors.m_index(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/authors/m_index.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
           rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
authors                            ...                           
Hamdan A          5       15    2  ...      2.0      2.0      0.5
Turki M           6       16    2  ...      2.0      2.0      0.5
Lin W             7       17    2  ...      2.0      1.0      0.5
Singh C           8       18    2  ...      2.0      1.0      0.5
Brennan R         9       19    2  ...      2.0      1.0      0.5
<BLANKLINE>
[5 rows x 18 columns]

>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'm_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors             |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Hamdan A            |          5 |        15 |     2 |             2 |                   0 |                 18 |                 5 |                             9   |                            2.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |       0.5 |
| Turki M             |          6 |        16 |     2 |             2 |                   0 |                 18 |                 5 |                             9   |                            2.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |       0.5 |
| Lin W               |          7 |        17 |     2 |             1 |                   1 |                 17 |                 4 |                             8.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |       0.5 |
| Singh C             |          8 |        18 |     2 |             1 |                   1 |                 17 |                 4 |                             8.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |       0.5 |
| Brennan R           |          9 |        19 |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |       0.5 |
| Crane M             |         10 |        20 |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |       0.5 |
| Ryan P              |         11 |        21 |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |       0.5 |
| Gong X              |         26 |        22 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Muganyi T           |         27 |        23 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Sun H-P             |         28 |        24 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Taghizadeh-Hesary F |         29 |        25 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Yan L               |         30 |        26 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Yin Y               |         31 |        27 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Cruz Rambaud S      |         57 |        54 |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Exposito Gazquez A  |         58 |        55 |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Ye Z                |         55 |        52 |     1 |             0 |                   1 |                  3 |                 1 |                             3   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Zhao L              |         56 |        53 |     1 |             0 |                   1 |                  3 |                 1 |                             3   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Abdullah Y          |         70 |        69 |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |       0.5 |
| Rabbani MR          |         76 |        75 |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |       0.5 |
| Shahnawaz S         |         77 |        76 |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |       0.5 |
```
<BLANKLINE>






# pylint: disable=line-too-long
"""
# from ... import list_items
# from ...graphing_lib import ranking_chart

FIELD = "authors"
METRIC = "m_index"
TITLE = "Author's M-Index"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def m_index(
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
    """Most Relevant Source Items."""

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
