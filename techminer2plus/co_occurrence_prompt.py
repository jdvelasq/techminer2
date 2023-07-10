# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _co_occurrence_prompt:

Co-occurrence Prompt
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.co_occurrence_prompt(
...     columns='author_keywords',
...     rows='authors',
...     col_occ_range=(2, None),
...     row_occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'author_keywords' and 'authors' fields in a bibliographic dataset. Identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors            |   REGTECH 28:329 |   FINTECH 12:249 |   REGULATORY_TECHNOLOGY 07:037 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   ANTI_MONEY_LAUNDERING 05:034 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   RISK_MANAGEMENT 03:014 |   INNOVATION 03:012 |   SUPTECH 03:004 |   SEMANTIC_TECHNOLOGIES 02:041 |   DATA_PROTECTION 02:027 |   CHARITYTECH 02:017 |   ENGLISH_LAW 02:017 |   ACCOUNTABILITY 02:014 |   DATA_PROTECTION_OFFICER 02:014 |   GDPR 02:014 |   SANDBOXES 02:012 |   TECHNOLOGY 02:010 |   FINANCE 02:001 |   REPORTING 02:001 |
|:-------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|-------------------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------:|--------------------:|-----------------:|-------------------------------:|-------------------------:|---------------------:|---------------------:|------------------------:|---------------------------------:|--------------:|-------------------:|--------------------:|-----------------:|-------------------:|
| Arner DW 3:185     |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           1 |                             2 |                                0 |                        0 |                   0 |                0 |                              0 |                        1 |                    0 |                    0 |                       0 |                                0 |             0 |                  1 |                   0 |                0 |                  0 |
| Buckley RP 3:185   |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           1 |                             2 |                                0 |                        0 |                   0 |                0 |                              0 |                        1 |                    0 |                    0 |                       0 |                                0 |             0 |                  1 |                   0 |                0 |                  0 |
| Barberis JN 2:161  |                1 |                0 |                              0 |                   0 |                   0 |                              0 |                           1 |                             1 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  1 |                   0 |                0 |                  0 |
| Butler T 2:041     |                2 |                2 |                              0 |                   0 |                   1 |                              0 |                           0 |                             0 |                                0 |                        1 |                   0 |                0 |                              2 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Hamdan A 2:018     |                0 |                0 |                              2 |                   0 |                   0 |                              2 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Turki M 2:018      |                0 |                0 |                              2 |                   0 |                   0 |                              2 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Lin W 2:017        |                2 |                0 |                              0 |                   0 |                   0 |                              1 |                           0 |                             0 |                                1 |                        0 |                   0 |                0 |                              0 |                        0 |                    2 |                    2 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Singh C 2:017      |                2 |                0 |                              0 |                   0 |                   0 |                              1 |                           0 |                             0 |                                1 |                        0 |                   0 |                0 |                              0 |                        0 |                    2 |                    2 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Brennan R 2:014    |                2 |                0 |                              0 |                   2 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       2 |                                2 |             2 |                  0 |                   0 |                0 |                  0 |
| Crane M 2:014      |                2 |                0 |                              0 |                   2 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       2 |                                2 |             2 |                  0 |                   0 |                0 |                  0 |
| Ryan P 2:014       |                2 |                0 |                              0 |                   2 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       2 |                                2 |             2 |                  0 |                   0 |                0 |                  0 |
| Sarea A 2:012      |                0 |                0 |                              1 |                   0 |                   0 |                              1 |                           0 |                             0 |                                1 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Grassi L 2:002     |                2 |                2 |                              1 |                   1 |                   2 |                              0 |                           0 |                             0 |                                0 |                        1 |                   1 |                1 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                1 |                  1 |
| Lanfranchi D 2:002 |                2 |                2 |                              1 |                   1 |                   2 |                              0 |                           0 |                             0 |                                0 |                        1 |                   1 |                1 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                1 |                  1 |
| Arman AA 2:000     |                2 |                0 |                              0 |                   0 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                1 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   1 |                0 |                  0 |
```
<BLANKLINE>



>>> prompt = tm2p.co_occurrence_prompt(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'author_keywords' and 'None' fields in a bibliographic dataset. Identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   REGTECH 28:329 |   FINTECH 12:249 |   REGULATORY_TECHNOLOGY 07:037 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   ANTI_MONEY_LAUNDERING 05:034 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   RISK_MANAGEMENT 03:014 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|-------------------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------:|
| REGTECH 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                              1 |                           3 |                             2 |                                2 |                        2 |
| FINTECH 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                              0 |                           2 |                             1 |                                1 |                        2 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                              2 |                           0 |                             0 |                                1 |                        2 |
| COMPLIANCE 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                              0 |                           0 |                             0 |                                1 |                        1 |
| REGULATION 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                              0 |                           1 |                             0 |                                0 |                        2 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |                0 |                              2 |                   0 |                   0 |                              5 |                           0 |                             0 |                                1 |                        0 |
| FINANCIAL_SERVICES 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                              0 |                           4 |                             2 |                                0 |                        0 |
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           2 |                             4 |                                0 |                        0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                              1 |                           0 |                             0 |                                4 |                        1 |
| RISK_MANAGEMENT 03:014         |                2 |                2 |                              2 |                   1 |                   2 |                              0 |                           0 |                             0 |                                1 |                        3 |
```
<BLANKLINE>


"""
from .co_occurrence_matrix import co_occurrence_matrix
from .format_prompt_for_dataframes import format_prompt_for_dataframes


def co_occurrence_prompt(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a co-occurrence matrix prompt."""

    matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if columns == rows:
        main_text = (
            "Your task is to generate a short paragraph for a research paper analyzing the "
            "co-occurrence between the items of the same column in a bibliographic dataset. "
            "Analyze the table below which contains values of co-occurrence (OCC) for the "
            f"'{columns}' field in a bibliographic dataset. Identify any notable patterns, "
            "trends, or outliers in the data, and discuss their implications for the research "
            "field. Be sure to provide a concise summary of your findings in no more than 150 "
            "words."
        )

    else:
        main_text = (
            "Your task is to generate a short paragraph for a research paper analyzing "
            "the co-occurrence between the values of different columns in a bibliographic "
            "dataset. Analyze the table below, and delimited by triple backticks, which "
            f"contains values of co-occurrence (OCC) for the '{columns}' and '{rows}' "
            "fields in a bibliographic dataset. Identify any notable patterns, trends, "
            "or outliers in the data, and discuss their implications for the research "
            "field. Be sure to provide a concise summary of your findings in no more "
            "than 150 words."
        )

    return format_prompt_for_dataframes(main_text, matrix.to_markdown())
