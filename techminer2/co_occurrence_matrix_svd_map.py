"""
Co-occurrence Matrix / SVD Map
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **salton** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the  co-occurrence matrix normalized with the **salton* measure.

2. Apply SVD to the co-occurrence matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_matrix_svd_map.png"
>>> co_occurrence_matrix_svd_map(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
... ).savefig(file_name)


.. image:: images/co_occurrence_matrix_svd_map.png
    :width: 700px
    :align: center

>>> co_occurrence_matrix_svd_map(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
...     plot=False,
... ).head()
                            dim0      dim1  ...     dim18     dim19
author_keywords                             ...                    
fintech                 1.267223 -0.217794  ... -0.013252  0.012584
financial technologies  0.650255 -0.375421  ... -0.275021 -0.130661
financial inclusion     0.624967 -0.393748  ...  0.056618  0.266723
block-chain             0.580905 -0.556643  ... -0.037316 -0.046776
innovating              0.723366  0.453754  ... -0.220027  0.176728
<BLANKLINE>
[5 rows x 20 columns]

"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .co_occurrence_matrix import co_occurrence_matrix
from .visualization_api.map_chart import map_chart


def co_occurrence_matrix_svd_map(
    column,
    min_occ=1,
    max_terms=150,
    dim_x=0,
    dim_y=1,
    directory="./",
    figsize=(7, 7),
    svd__n_iter=5,
    random_state=0,
    plot=True,
):

    matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        normalization="salton",
        directory=directory,
    )

    max_dimensions = min(20, len(matrix.columns) - 1)

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions,
        n_iter=svd__n_iter,
        random_state=random_state,
    ).fit_transform(matrix)

    if decomposed_matrix.shape[0] > max_terms:
        decomposed_matrix = decomposed_matrix.head(max_terms)
    if isinstance(matrix.index, pd.MultiIndex):
        labels = matrix.index.get_level_values(0)
    else:
        labels = matrix.index

    decomposed_matrix = pd.DataFrame(
        decomposed_matrix,
        columns=[f"dim{dim}" for dim in range(max_dimensions)],
        index=labels,
    )

    if plot is False:
        return decomposed_matrix

    return map_chart(
        data=decomposed_matrix,
        dim_x=dim_x,
        dim_y=dim_y,
        max_items=max_terms,
        figsize=figsize,
        color="k",
    )
