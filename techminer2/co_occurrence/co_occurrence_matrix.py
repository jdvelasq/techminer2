# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _co_occurrence_analysis.co_occurrence_matrix:

Co-occurrence Matrix 
===============================================================================


>>> from techminer2.co_occurrence_analysis import co_occurrence_matrix
>>> matrix = co_occurrence_matrix(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows='authors',
...     #
...     # COLUMN PARAMS:
...     col_top_n=None,
...     col_occ_range=(2, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(2, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_
author_keywords     REGTECH 28:329  ...  REPORTING 02:001
authors                             ...                  
Arner DW 3:185                   2  ...                 0
Buckley RP 3:185                 2  ...                 0
Barberis JN 2:161                1  ...                 0
Butler T 2:041                   2  ...                 0
Hamdan A 2:018                   0  ...                 0
Turki M 2:018                    0  ...                 0
Lin W 2:017                      2  ...                 0
Singh C 2:017                    2  ...                 0
Brennan R 2:014                  2  ...                 0
Crane M 2:014                    2  ...                 0
Ryan P 2:014                     2  ...                 0
Sarea A 2:012                    0  ...                 0
Grassi L 2:002                   2  ...                 1
Lanfranchi D 2:002               2  ...                 1
Arman AA 2:000                   2  ...                 0
<BLANKLINE>
[15 rows x 23 columns]

>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...

>>> matrix.list_cells_.head()
              row             column  matrix_value
0  REGTECH 28:329     Arner DW 3:185             2
1  REGTECH 28:329   Buckley RP 3:185             2
2  REGTECH 28:329  Barberis JN 2:161             1
3  REGTECH 28:329     Butler T 2:041             2
4  REGTECH 28:329     Hamdan A 2:018             0

>>> print(matrix.prompt_)
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



>>> matrix = co_occurrence_matrix(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows=None,
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(2, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_
author_keywords                 REGTECH 28:329  ...  RISK_MANAGEMENT 03:014
author_keywords                                 ...                        
REGTECH 28:329                              28  ...                       2
FINTECH 12:249                              12  ...                       2
REGULATORY_TECHNOLOGY 07:037                 2  ...                       2
COMPLIANCE 07:030                            7  ...                       1
REGULATION 05:164                            4  ...                       2
ANTI_MONEY_LAUNDERING 05:034                 1  ...                       0
FINANCIAL_SERVICES 04:168                    3  ...                       0
FINANCIAL_REGULATION 04:035                  2  ...                       0
ARTIFICIAL_INTELLIGENCE 04:023               2  ...                       1
RISK_MANAGEMENT 03:014                       2  ...                       3
<BLANKLINE>
[10 rows x 10 columns]

>>> matrix.list_cells_.head()
              row                        column  matrix_value
0  REGTECH 28:329                REGTECH 28:329            28
1  REGTECH 28:329                FINTECH 12:249            12
2  REGTECH 28:329  REGULATORY_TECHNOLOGY 07:037             2
3  REGTECH 28:329             COMPLIANCE 07:030             7
4  REGTECH 28:329             REGULATION 05:164             4

>>> print(matrix.prompt_)
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
from dataclasses import dataclass

from .._counters_lib import add_counters_to_frame_axis
from .._filtering_lib import generate_custom_items
from .._sorting_lib import sort_indicators_by_metric, sort_matrix_axis
from ..format_prompt_for_dataframes import format_prompt_for_dataframes
from ..indicators.global_co_occurrence_matrix_list import global_co_occurrence_matrix_list
from ..indicators.global_indicators_by_field import global_indicators_by_field


def co_occurrence_matrix(
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
    """Creates a co-occurrence matrix.

    :meta private:
    """

    matrix = ___matrix(
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

    prompt = __prompt(
        matrix=matrix,
        columns=columns,
        rows=rows,
    )

    @dataclass
    class Result:
        df_ = matrix
        prompt_ = prompt

        @property
        def list_cells_(self):
            matrix = self.df_.copy()
            matrix = matrix.melt(
                value_name="matrix_value",
                var_name="row",
                ignore_index=False,
            )
            matrix["column"] = matrix.index.to_list()
            matrix = matrix.reset_index(drop=True)
            matrix = matrix[["row", "column", "matrix_value"]]

            return matrix

        @property
        def heat_map_(self):
            #
            def make_heat_map(styler):
                styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="Oranges")
                return styler

            return self.df_.style.pipe(make_heat_map)

    return Result()


def ___matrix(
    #
    # FUNCTION PARAMS:
    columns,
    rows,
    #
    # COLUMN PARAMS:
    col_top_n,
    col_occ_range,
    col_gc_range,
    col_custom_items,
    #
    # ROW PARAMS:
    row_top_n,
    row_occ_range,
    row_gc_range,
    row_custom_items,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Creates a co-occurrence matrix."""

    def filter_terms(
        raw_matrix_list,
        name,
        field,
        # Item filters:
        top_n,
        occ_range,
        gc_range,
        custom_items,
    ):
        if custom_items is None:
            indicators = global_indicators_by_field(
                field=field,
                root_dir=root_dir,
                database=database,
                year_filter=year_filter,
                cited_by_filter=cited_by_filter,
                **filters,
            )

            indicators = sort_indicators_by_metric(indicators, "OCC", is_trend_analysis=False)

            custom_items = generate_custom_items(
                indicators=indicators,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        raw_matrix_list = raw_matrix_list[raw_matrix_list[name].isin(custom_items)]

        return raw_matrix_list

    def pivot(matrix_list):
        matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)
        return matrix

    #
    # MAIN CODE:
    #
    if rows is None:
        rows = columns
        row_top_n = col_top_n
        row_occ_range = col_occ_range
        row_gc_range = col_gc_range
        row_custom_items = col_custom_items

    # Generates a matrix list with all descriptors in the database
    raw_matrix_list = global_co_occurrence_matrix_list(
        columns=columns,
        rows=rows,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # Filters the terms in the 'row' column of the matrix list
    raw_filterd_matrix_list = filter_terms(
        raw_matrix_list=raw_matrix_list,
        field=rows,
        name="row",
        #
        # ROW PARAMS:
        top_n=row_top_n,
        occ_range=row_occ_range,
        gc_range=row_gc_range,
        custom_items=row_custom_items,
    )

    # Filters the terms in the 'column' column of the matrix list
    filtered_matrix_list = filter_terms(
        raw_matrix_list=raw_filterd_matrix_list,
        field=columns,
        name="column",
        #
        # ROW PARAMS:
        top_n=col_top_n,
        occ_range=col_occ_range,
        gc_range=col_gc_range,
        custom_items=col_custom_items,
    )

    # Creates a matrix
    matrix = pivot(filtered_matrix_list)

    # sort the rows and columns of the matrix
    matrix = sort_matrix_axis(
        matrix,
        axis=0,
        field=rows,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = sort_matrix_axis(
        matrix,
        axis=1,
        field=columns,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    row_custom_items = matrix.index.tolist()
    col_custom_items = matrix.columns.tolist()

    matrix = add_counters_to_frame_axis(
        dataframe=matrix,
        axis=0,
        field=rows,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = add_counters_to_frame_axis(
        dataframe=matrix,
        axis=1,
        field=columns,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix.columns.name = columns
    matrix.index.name = rows

    return matrix


def __prompt(matrix, columns, rows):
    """Creates a co-occurrence matrix prompt."""

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
