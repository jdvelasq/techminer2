# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Matrix 
===============================================================================


## >>> co_occurrence_matrix(
## >>> from techminer2.co_occurrence_matrix import co_occurrence_matrix
## ...     #
## ...     # FUNCTION PARAMS:
## ...     columns='author_keywords',
## ...     rows='authors',
## ...     #
## ...     # COLUMN PARAMS:
## ...     col_top_n=None,
## ...     col_occ_range=(2, None),
## ...     col_gc_range=(None, None),
## ...     col_custom_terms=None,
## ...     #
## ...     # ROW PARAMS:
## ...     row_top_n=None,
## ...     row_occ_range=(2, None),
## ...     row_gc_range=(None, None),
## ...     row_custom_terms=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
columns               FINTECH 31:5168  ...  P2P_LENDING 02:0161
rows                                   ...                     
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
[10 rows x 12 columns]


## >>> co_occurrence_matrix(
## ...     #
## ...     # FUNCTION PARAMS:
## ...     columns='author_keywords',
## ...     rows='author_keywords',
## ...     #
## ...     # COLUMN PARAMS:
## ...     col_top_n=None,
## ...     col_occ_range=(2, None),
## ...     col_gc_range=(None, None),
## ...     col_custom_terms=None,
## ...     #
## ...     # ROW PARAMS:
## ...     row_top_n=None,
## ...     row_occ_range=(None, None),
## ...     row_gc_range=(None, None),
## ...     row_custom_terms=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
columns                       FINTECH 31:5168  ...  P2P_LENDING 02:0161
rows                                           ...                     
FINTECH 31:5168                            31  ...                    2
INNOVATION 07:0911                          5  ...                    0
FINANCIAL_SERVICES 04:0667                  3  ...                    0
FINANCIAL_INCLUSION 03:0590                 3  ...                    0
FINANCIAL_TECHNOLOGY 03:0461                2  ...                    0
...                                       ...  ...                  ...
G20 01:0064                                 1  ...                    1
G28 01:0064                                 1  ...                    1
G29 01:0064                                 1  ...                    1
PAYMENTS 01:0064                            1  ...                    0
TRADING 01:0064                             1  ...                    0
<BLANKLINE>
[141 rows x 25 columns]

"""
from .co_occurrence_table import co_occurrence_table


def co_occurrence_matrix(
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

    def pivot(matrix_list):
        matrix = matrix_list.pivot(
            index=matrix_list.columns[0],
            columns=matrix_list.columns[1],
            values=matrix_list.columns[2],
        )
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)
        return matrix

    matrix_list = co_occurrence_table(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        retain_counters=True,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_terms=row_custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = pivot(matrix_list)
    matrix = matrix.astype(int)

    # sort the rows and columns of the matrix
    matrix_cols = matrix.columns.tolist()
    matrix_rows = matrix.index.tolist()
    matrix_cols = sorted(matrix_cols, key=lambda x: x.split()[-1], reverse=True)
    matrix_rows = sorted(matrix_rows, key=lambda x: x.split()[-1], reverse=True)
    matrix = matrix[matrix_cols]
    matrix = matrix.loc[matrix_rows]

    if retain_counters is False:
        matrix_cols = [" ".join(col.split()[:-1]) for col in matrix_cols]
        matrix_rows = [" ".join(row.split()[:-1]) for row in matrix_rows]
        matrix.columns = matrix_cols
        matrix.index = matrix_rows

    return matrix
