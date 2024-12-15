# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2.correlation_matrix import auto_correlation_matrix
>>> auto_correlation_matrix(
...     #
...     # FUNCTION PARAMS:
...     rows_and_columns='authors',
...     method="pearson",
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).round(3)
                      Jagtiani J. 3:0317  ...  Zavolokina L. 2:0181
Jagtiani J. 3:0317                  1.00  ...                   0.0
Gomber P. 2:1065                    0.00  ...                   0.0
Hornuf L. 2:0358                    0.00  ...                   0.0
Gai K. 2:0323                       0.00  ...                   0.0
Qiu M. 2:0323                       0.00  ...                   0.0
Sun X./3 2:0323                     0.00  ...                   0.0
Lemieux C. 2:0253                   0.77  ...                   0.0
Dolata M. 2:0181                    0.00  ...                   1.0
Schwabe G. 2:0181                   0.00  ...                   1.0
Zavolokina L. 2:0181                0.00  ...                   1.0
<BLANKLINE>
[10 rows x 10 columns]


"""
from ...internals.helpers.utils_format_prompt_for_dataframes import (
    _utils_format_prompt_for_dataframes,
)
from ..metrics.tfidf_frame import tfidf_frame
from ._compute_corr_matrix import compute_corr_matrix


def auto_correlation_matrix(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    method="pearson",
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    data_matrix = tfidf_frame(
        #
        # TF PARAMS:
        field=rows_and_columns,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    custom_terms = [
        " ".join(col.split(" ")[:-1]) for col in data_matrix.columns.tolist()
    ]

    corr_matrix = compute_corr_matrix(method=method, data_matrix=data_matrix)

    return corr_matrix
