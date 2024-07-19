# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Table 
===============================================================================


>>> from techminer2.co_occurrence_matrix import co_occurrence_table
>>> co_occurrence_table(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows='authors',
...     retain_counters=True,
...     #
...     # COLUMN PARAMS:
...     col_top_n=None,
...     col_occ_range=(2, None),
...     col_gc_range=(None, None),
...     col_custom_terms=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(2, None),
...     row_gc_range=(None, None),
...     row_custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(10)
                 rows                      columns  OCC
0  Jagtiani J. 3:0317              FINTECH 31:5168    3
1  Jagtiani J. 3:0317  MARKETPLACE_LENDING 03:0317    3
2    Dolata M. 2:0181     CONTENT_ANALYSIS 02:0181    2
3    Dolata M. 2:0181       DIGITALIZATION 02:0181    2
4    Dolata M. 2:0181              FINTECH 31:5168    2
5    Dolata M. 2:0181           INNOVATION 07:0911    2
6    Dolata M. 2:0181        POPULAR_PRESS 02:0181    2
7       Gai K. 2:0323              FINTECH 31:5168    2
8    Hornuf L. 2:0358              FINTECH 31:5168    2
9  Jagtiani J. 3:0317          LENDINGCLUB 02:0253    2


"""

from .._core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics
from .._core.metrics.extract_top_n_terms_by_metric import extract_top_n_terms_by_metric
from .._core.metrics.sort_records_by_metric import sort_records_by_metric
from .._core.read_filtered_database import read_filtered_database
from .._core.stopwords.load_user_stopwords import load_user_stopwords
from ..helpers.helper_compute_occurrences_and_citations import helper_compute_occurrences_and_citations


def co_occurrence_table(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    retain_counters=True,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_terms=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    def filter_terms(
        #
        # MATRIX PARAMS:
        raw_matrix_list,
        name,
        field,
        #
        # TERM PARAMS:
        top_n,
        occ_range,
        gc_range,
        custom_items,
    ):
        if custom_items is None:
            indicators = calculate_global_performance_metrics(
                field=field,
                root_dir=root_dir,
                database=database,
                year_filter=year_filter,
                cited_by_filter=cited_by_filter,
                **filters,
            )

            indicators = sort_records_by_metric(indicators, "OCC")

            custom_items = extract_top_n_terms_by_metric(
                indicators=indicators,
                metric="OCC",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        raw_matrix_list = raw_matrix_list[raw_matrix_list[name].isin(custom_items)]

        return raw_matrix_list

    #
    # MAIN CODE:
    #
    if rows is None:
        rows = columns
        row_top_n = col_top_n
        row_occ_range = col_occ_range
        row_gc_range = col_gc_range
        row_custom_terms = col_custom_terms

    records = read_filtered_database(
        #
        # DATABASE PARAMS:
        root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **filters,
    )

    raw_matrix_list = records[[columns]].copy()
    raw_matrix_list = raw_matrix_list.rename(columns={columns: "column"})
    raw_matrix_list = raw_matrix_list.assign(row=records[[rows]])

    stopwords = load_user_stopwords(root_dir=root_dir)

    for name in ["column", "row"]:
        raw_matrix_list[name] = raw_matrix_list[name].str.split(";")
        raw_matrix_list = raw_matrix_list.explode(name)
        raw_matrix_list[name] = raw_matrix_list[name].str.strip()
        raw_matrix_list = raw_matrix_list[~raw_matrix_list[name].isin(stopwords)]

    raw_matrix_list["OCC"] = 1
    raw_matrix_list = raw_matrix_list.groupby(["row", "column"], as_index=False).aggregate("sum")

    raw_matrix_list = raw_matrix_list.sort_values(["OCC", "row", "column"], ascending=[False, True, True])

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
        custom_items=row_custom_terms,
    )

    # Filters the terms in the 'column' column of the matrix list
    filtered_matrix_list = filter_terms(
        raw_matrix_list=raw_filterd_matrix_list,
        field=columns,
        name="column",
        #
        # COL PARAMS:
        top_n=col_top_n,
        occ_range=col_occ_range,
        gc_range=col_gc_range,
        custom_items=col_custom_terms,
    )

    # Assign counters to column 'row'
    if retain_counters:

        rows_map = helper_compute_occurrences_and_citations(
            criterion=rows,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        filtered_matrix_list["row"] = filtered_matrix_list["row"].map(rows_map)

        columns_map = helper_compute_occurrences_and_citations(
            criterion=columns,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        filtered_matrix_list["column"] = filtered_matrix_list["column"].map(columns_map)

    filtered_matrix_list = filtered_matrix_list.reset_index(drop=True)
    # filtered_matrix_list = filtered_matrix_list.rename(columns={"row": rows, "column": columns})
    filtered_matrix_list = filtered_matrix_list.rename(columns={"row": "rows", "column": "columns"})

    return filtered_matrix_list
