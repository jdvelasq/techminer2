# flake8: noqa
"""
Factor Matrix
===============================================================================

Factor matrix obtained by appliying PCA to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Applies PCA to the co-occurrence matrix.

3. Returns the factor matrix.


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> factor_matrix = vantagepoint.analyze.factor_matrix(
...     field="authors",
...     occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> factor_matrix.table_
component                Factor_00 Factor_01  ... Factor_04     Factor_05
explained_variance          3.5514    2.2015  ...    0.4746        0.2857
explained_variance_ratio    0.3864    0.2395  ...    0.0516        0.0311
row                                           ...                        
Arner DW 3:185            3.920561  0.600934  ... -0.148250 -7.455683e-17
Buckley RP 3:185          3.920561  0.600934  ... -0.148250 -7.455683e-17
Barberis JN 2:161         2.752839  0.324807  ...  0.074600 -1.904568e-17
Butler T/1 2:041         -0.472960 -0.489055  ...  1.643183 -1.414214e+00
Hamdan A 2:018           -0.817727 -1.641907  ... -0.363928 -3.521126e-16
Turki M 2:018            -0.817727 -1.641907  ... -0.363928 -3.521126e-16
Lin W 2:017              -0.641277 -0.885031  ... -0.464342 -1.023124e-16
Singh C 2:017            -0.641277 -0.885031  ... -0.464342 -1.023124e-16
Brennan R 2:014          -1.576144  2.532547  ... -0.147991  2.446323e-16
Crane M 2:014            -1.576144  2.532547  ... -0.147991  2.446323e-16
Ryan P 2:014             -1.576144  2.532547  ... -0.147991  2.446323e-16
Sarea A 2:012            -0.719045 -1.322270  ... -0.035271  8.709897e-18
Grassi L 2:002           -0.641277 -0.885031  ... -0.464342 -4.492571e-16
Lanfranchi D 2:002       -0.641277 -0.885031  ... -0.464342 -4.492571e-16
Arman AA 2:000           -0.472960 -0.489055  ...  1.643183  1.414214e+00
<BLANKLINE>
[15 rows x 6 columns]

# pylint: disable=line-too-long
"""

import pandas as pd
from sklearn.decomposition import PCA

from ...classes import FactorMatrix
from .co_occurrence_matrix import co_occurrence_matrix


def factor_matrix(
    # Specific params:
    field,
    pca=None,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Creates a Factor Matrix.




    # pylint: disable=line-too-long
    """

    coc_matrix = co_occurrence_matrix(
        columns=field,
        # Columns item filters:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = coc_matrix.matrix_

    if pca is None:
        pca = PCA(n_components=6)

    pca.fit(matrix)

    transformed_matrix = pca.transform(matrix)
    columns = [
        (f"Factor_{i_component:>02d}", round(ev, 4), round(evratio, 4))
        for i_component, (ev, evratio) in enumerate(
            zip(pca.explained_variance_, pca.explained_variance_ratio_)
        )
    ]
    columns = pd.MultiIndex.from_tuples(
        columns,
        names=["component", "explained_variance", "explained_variance_ratio"],
    )
    matrix = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )

    fmatrix = FactorMatrix()
    fmatrix.table_ = matrix
    fmatrix.field_ = field
    fmatrix.prompt_ = "TODO"

    return fmatrix
