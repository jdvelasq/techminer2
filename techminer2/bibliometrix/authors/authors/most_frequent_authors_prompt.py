# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_frequent_authors_prompt:

Most Frequent Authors Prompt
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> prompt = tm2p.most_frequent_authors_prompt(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors     |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Arner DW    |          1 |         1 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Buckley RP  |          2 |         2 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Barberis JN |          3 |         3 |     2 |             2 |                   0 |                161 |                 3 |                           80.5  |                           1.5  |                   0   |                     0   |                        0    |                     2017 |     7 |                       23    |         2 |         2 |      0.29 |
| Butler T    |          4 |         5 |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                        0    |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Hamdan A    |          5 |        15 |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Turki M     |          6 |        16 |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Lin W       |          7 |        17 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Singh C     |          8 |        18 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Brennan R   |          9 |        19 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Crane M     |         10 |        20 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
```
<BLANKLINE>



"""
from ....format_prompt_for_dataframes import format_prompt_for_dataframes
from ....vantagepoint.discover.list_items_table import list_items_table


def most_frequent_authors_prompt(
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Returns a ItemList object with the extracted items of database field."""

    FIELD = "authors"
    METRIC = "OCC"

    data_frame = list_items_table(
        #
        # ITEMS PARAMS:
        field=FIELD,
        metric=METRIC,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    main_text = (
        "Your task is to generate an analysis about the bibliometric indicators of the "
        f"'{FIELD}' field in a scientific bibliography database. Summarize the table below, "
        f"sorted by the '{METRIC}' metric, and delimited by triple backticks, identify "
        "any notable patterns, trends, or outliers in the data, and discuss their "
        "implications for the research field. Be sure to provide a concise summary "
        "of your findings in no more than 150 words."
    )
    return format_prompt_for_dataframes(main_text, data_frame.to_markdown())
