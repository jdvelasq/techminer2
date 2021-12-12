"""
Co-occurrence Matrix / SVD Map
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **cosine** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Apply SVD to the co-occurrence matrix with `n_components=20`.

2. Plot the decomposed matrix.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_svd_map.png"
>>> co_occurrence_svd_map(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
... ).savefig(file_name)


.. image:: images/co_occurrence_svd_map.png
    :width: 700px
    :align: center

>>> co_occurrence_svd_map(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
...     plot=False,
... ).head()
                            dim0      dim1  ...     dim18     dim19
author_keywords                             ...                    
fintech                 1.266169 -0.123487  ... -0.011774  0.072038
financial technologies  0.666967 -0.342768  ... -0.274869 -0.127540
financial inclusion     0.664505 -0.311517  ...  0.056878  0.324649
blockchain              0.622238 -0.488122  ... -0.037378 -0.059448
innovation              0.691683  0.476721  ... -0.222151  0.091783
<BLANKLINE>
[5 rows x 20 columns]

"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .map_chart import map_chart


def co_occurrence_svd_map(
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
