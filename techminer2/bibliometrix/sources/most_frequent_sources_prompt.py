# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_frequent_sources_prompt:

Most Frequent Sources Prompt
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> prompt = tm2p.most_frequent_sources_prompt(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |          1 |         3 |     2 |             2 |                   0 |                 35 |                 9 |                            17.5 |                            4.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        8.75 |         2 |         2 |      0.5  |
| J FINANC CRIME                |          2 |         8 |     2 |             1 |                   1 |                 13 |                 4 |                             6.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| FOSTER INNOVCOMPET WITH FINTE |          3 |        28 |     2 |             2 |                   0 |                  1 |                 1 |                             0.5 |                            0.5 |                   0   |                     0   |                        0    |                     2020 |     4 |                        0.25 |         1 |         1 |      0.25 |
| STUD COMPUT INTELL            |          4 |        29 |     2 |             2 |                   0 |                  1 |                 1 |                             0.5 |                            0.5 |                  -1   |                     0   |                        0    |                     2021 |     3 |                        0.33 |         1 |         1 |      0.33 |
| INT CONF INF TECHNOL SYST INN |          5 |        36 |     2 |             0 |                   2 |                  0 |                 0 |                             0   |                            0   |                   0   |                     1   |                        0.5  |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |        37 |     2 |             2 |                   0 |                  0 |                 0 |                             0   |                            0   |                  -1   |                     0   |                        0    |                     2021 |     3 |                        0    |         0 |         0 |      0    |
| J ECON BUS                    |          7 |         1 |     1 |             1 |                   0 |                153 |                17 |                           153   |                           17   |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| NORTHWEST J INTL LAW BUS      |          8 |         2 |     1 |             1 |                   0 |                150 |                 0 |                           150   |                            0   |                   0   |                     0   |                        0    |                     2017 |     7 |                       21.43 |         1 |         1 |      0.14 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |         4 |     1 |             1 |                   0 |                 33 |                14 |                            33   |                           14   |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| DUKE LAW J                    |         10 |         5 |     1 |             1 |                   0 |                 30 |                 0 |                            30   |                            0   |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
```
<BLANKLINE>


"""
from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ...vantagepoint.discover.list_items_table import list_items_table


def most_frequent_sources_prompt(
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

    FIELD = "source_abbr"
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
