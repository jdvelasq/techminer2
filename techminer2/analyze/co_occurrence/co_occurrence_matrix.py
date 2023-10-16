# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Matrix 
===============================================================================


>>> from techminer2.analyze.co_occurrence import co_occurrence_matrix
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_
author_keywords       FINTECH 31:5168  ...  P2P_LENDING 02:0161
authors                                ...                     
Jagtiani J. 3:0317                  3  ...                    2
Gomber P. 2:1065                    1  ...                    0
Hornuf L. 2:0358                    2  ...                    0
Gai K. 2:0323                       2  ...                    0
Qiu M. 2:0323                       2  ...                    0
Sun X./3 2:0323                     2  ...                    0
Lemieux C. 2:0253                   2  ...                    1
Dolata M. 2:0181                    2  ...                    0
Schwabe G. 2:0181                   2  ...                    0
Zavolokina L. 2:0181                2  ...                    0
<BLANKLINE>
[10 rows x 14 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...

>>> matrix.list_cells_.head()
               row              column  matrix_value
0  FINTECH 31:5168  Jagtiani J. 3:0317             3
1  FINTECH 31:5168    Gomber P. 2:1065             1
2  FINTECH 31:5168    Hornuf L. 2:0358             2
3  FINTECH 31:5168       Gai K. 2:0323             2
4  FINTECH 31:5168       Qiu M. 2:0323             2


>>> print(matrix.prompt_) # doctest: +ELLIPSIS
Your task is ...



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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_
author_keywords                          FINTECH 31:5168  ...  DIGITALIZATION 03:0434
author_keywords                                           ...                        
FINTECH 31:5168                                       31  ...                       3
INNOVATION 07:0911                                     5  ...                       3
FINANCIAL_SERVICES 04:0667                             3  ...                       0
FINANCIAL_TECHNOLOGY 04:0551                           2  ...                       1
MOBILE_FINTECH_PAYMENT_SERVICES 04:0485                3  ...                       0
BUSINESS 03:0896                                       3  ...                       0
SHADOW_BANKING 03:0643                                 3  ...                       0
FINANCIAL_INCLUSION 03:0590                            3  ...                       0
CASE_STUDIES 03:0442                                   3  ...                       0
DIGITALIZATION 03:0434                                 3  ...                       3
<BLANKLINE>
[10 rows x 10 columns]



>>> matrix.list_cells_.head()
               row                                   column  matrix_value
0  FINTECH 31:5168                          FINTECH 31:5168            31
1  FINTECH 31:5168                       INNOVATION 07:0911             5
2  FINTECH 31:5168               FINANCIAL_SERVICES 04:0667             3
3  FINTECH 31:5168             FINANCIAL_TECHNOLOGY 04:0551             2
4  FINTECH 31:5168  MOBILE_FINTECH_PAYMENT_SERVICES 04:0485             3

>>> print(matrix.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
from dataclasses import dataclass

from ..._common._counters_lib import add_counters_to_frame_axis
from ..._common._filtering_lib import generate_custom_items
from ..._common._sorting_lib import sort_indicators_by_metric, sort_matrix_axis
from ..._common.format_prompt_for_dataframes import format_prompt_for_dataframes
from ..._read_records import read_records
from ..._stopwords import load_stopwords
from ...indicators.global_indicators_by_field import global_indicators_by_field


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

            indicators = sort_indicators_by_metric(indicators, "OCC")

            custom_items = generate_custom_items(
                indicators=indicators,
                metric="OCC",
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


def global_co_occurrence_matrix_list(
    columns,
    rows,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Creates a matrix list with all terms of the database."""

    records = read_records(
        # Database params:
        root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = records[[columns]].copy()
    matrix_list = matrix_list.rename(columns={columns: "column"})
    matrix_list = matrix_list.assign(row=records[[rows]])

    stopwords = load_stopwords(root_dir=root_dir)

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()
        matrix_list = matrix_list[~matrix_list[name].isin(stopwords)]

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    matrix_list = matrix_list.sort_values(
        ["OCC", "row", "column"], ascending=[False, True, True]
    )

    return matrix_list
