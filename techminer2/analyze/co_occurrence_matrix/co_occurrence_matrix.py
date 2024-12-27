# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Matrix 
===============================================================================


>>> from techminer2.analyze.co_occurrence_matrix import CoOccurrenceMatrix
>>> (
...     CoOccurrenceMatrix()
...     .set_column_params(
...         field="author_keywords",
...         top_n=10,
...         occ_range=(2, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_rows_params(
...         field="authors",
...         top_n=None,
...         occ_range=(2, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_format_params(
...         retain_counters=True,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
columns               FINTECH 31:5168  ...  CYBER_SECURITY 02:0342
rows                                   ...                        
Jagtiani J. 3:0317                  3  ...                       0
Gomber P. 2:1065                    1  ...                       0
Hornuf L. 2:0358                    2  ...                       0
Gai K. 2:0323                       2  ...                       1
Qiu M. 2:0323                       2  ...                       1
Sun X./3 2:0323                     2  ...                       1
Lemieux C. 2:0253                   2  ...                       0
Dolata M. 2:0181                    2  ...                       0
Schwabe G. 2:0181                   2  ...                       0
Zavolokina L. 2:0181                2  ...                       0
<BLANKLINE>
[10 rows x 5 columns]

>>> from techminer2.analyze.co_occurrence_matrix import CoOccurrenceMatrix
>>> (
...     CoOccurrenceMatrix()
...     .set_column_params(
...         field="author_keywords",
...         top_n=10,
...         occ_range=(2, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_rows_params(
...         field=None,
...         top_n=None,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_format_params(
...         retain_counters=True,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
columns                       FINTECH 31:5168  ...  CASE_STUDY 02:0340
rows                                           ...                    
FINTECH 31:5168                            31  ...                   2
INNOVATION 07:0911                          5  ...                   0
FINANCIAL_SERVICES 04:0667                  3  ...                   0
FINANCIAL_INCLUSION 03:0590                 3  ...                   1
FINANCIAL_TECHNOLOGY 03:0461                2  ...                   0
CROWDFUNDING 03:0335                        2  ...                   0
MARKETPLACE_LENDING 03:0317                 3  ...                   0
BUSINESS_MODELS 02:0759                     2  ...                   0
CYBER_SECURITY 02:0342                      2  ...                   0
CASE_STUDY 02:0340                          2  ...                   2
<BLANKLINE>
[10 rows x 10 columns]




"""
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams
from .co_occurrence_dataframe import CoOccurrenceDataFrame
from .internals.output_params import OutputParams, OutputParamsMixin


class CoOccurrenceMatrix(
    ColumnsAndRowsParamsMixin,
    DatabaseParamsMixin,
    OutputParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.columns_params = ItemParams()
        self.database_params = DatabaseParams()
        self.output_params = OutputParams()
        self.rows_params = ItemParams()

    def build(self):

        def pivot(matrix_list):
            matrix = matrix_list.pivot(
                index=matrix_list.columns[0],
                columns=matrix_list.columns[1],
                values=matrix_list.columns[2],
            )
            matrix = matrix.fillna(0)
            matrix = matrix.astype(int)
            return matrix

        matrix_list = (
            CoOccurrenceDataFrame()
            .set_columns_params(**self.columns_params.__dict__)
            .set_rows_params(**self.rows_params.__dict__)
            .set_format_params(**self.output_params.__dict__)
            .set_database_params(**self.database_params.__dict__)
            .build()
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

        if self.output_params.retain_counters is False:
            matrix_cols = [" ".join(col.split()[:-1]) for col in matrix_cols]
            matrix_rows = [" ".join(row.split()[:-1]) for row in matrix_rows]
            matrix.columns = matrix_cols
            matrix.index = matrix_rows

        return matrix


# TODO: Remove
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
    return (
        CoOccurrenceMatrix()
        .set_columns_params(
            field=columns,
            top_n=col_top_n,
            occ_range=col_occ_range,
            gc_range=col_gc_range,
            custom_terms=col_custom_terms,
        )
        .set_rows_params(
            field=rows,
            top_n=row_top_n,
            occ_range=row_occ_range,
            gc_range=row_gc_range,
            custom_terms=row_custom_terms,
        )
        .set_format_params(
            retain_counters=retain_counters,
        )
        .set_database_params(
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        .build()
    )
