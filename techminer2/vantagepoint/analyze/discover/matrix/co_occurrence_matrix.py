# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _co_occurrence_matrix:

Co-occurrence Matrix 
===============================================================================


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> tm2.co_occurrence_matrix(
...     columns='author_keywords',
...     rows='authors',
...     col_occ_range=(2, None),
...     row_occ_range=(2, None),
...     root_dir=root_dir,
... )
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

"""
from ....._counters_lib import add_counters_to_frame_axis
from ....._filtering_lib import generate_custom_items
from ....._sorting_lib import sort_indicators_by_metric, sort_matrix_axis
from .....techminer.metrics.global_co_occurrence_matrix_list import (
    global_co_occurrence_matrix_list,
)
from .....techminer.metrics.global_indicators_by_field import (
    global_indicators_by_field,
)


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
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        raw_matrix_list = raw_matrix_list[
            raw_matrix_list[name].isin(custom_items)
        ]

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
