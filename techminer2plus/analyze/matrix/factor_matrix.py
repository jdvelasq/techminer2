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

>>> import techminer2plus
>>> factor_matrix = techminer2plus.analyze.matrix.factor_matrix(
...     field="authors",
...     occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> factor_matrix.table_.round(3)
component                Factor_00 Factor_01  ... Factor_04 Factor_05
explained_variance          3.5514    2.2015  ...    0.4746    0.2857
explained_variance_ratio    0.3864    0.2395  ...    0.0516    0.0311
row                                           ...                    
Arner DW 3:185               3.921     0.601  ...    -0.148    -0.000
Buckley RP 3:185             3.921     0.601  ...    -0.148    -0.000
Barberis JN 2:161            2.753     0.325  ...     0.075    -0.000
Butler T 2:041              -0.473    -0.489  ...     1.643    -1.414
Hamdan A 2:018              -0.818    -1.642  ...    -0.364    -0.000
Turki M 2:018               -0.818    -1.642  ...    -0.364    -0.000
Lin W 2:017                 -0.641    -0.885  ...    -0.464    -0.000
Singh C 2:017               -0.641    -0.885  ...    -0.464    -0.000
Brennan R 2:014             -1.576     2.533  ...    -0.148     0.000
Crane M 2:014               -1.576     2.533  ...    -0.148     0.000
Ryan P 2:014                -1.576     2.533  ...    -0.148     0.000
Sarea A 2:012               -0.719    -1.322  ...    -0.035     0.000
Grassi L 2:002              -0.641    -0.885  ...    -0.464    -0.000
Lanfranchi D 2:002          -0.641    -0.885  ...    -0.464    -0.000
Arman AA 2:000              -0.473    -0.489  ...     1.643     1.414
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
    database="main",
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
