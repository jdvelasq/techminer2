"""
SVD Map of TF Matrix
===============================================================================

Plots the SVD of the TF matrix (0/1 values).

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Transpose the TF matrix

2. Apply SVD to the transposed matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/svd_map_of_tf_matrix.png"
>>> svd_map_of_tf_matrix(
...     column='author_keywords',
...     min_occ=6,
...     directory=directory,
... ).savefig(file_name)


.. image:: images/svd_map_of_tf_matrix.png
    :width: 700px
    :align: center

>>> svd_map_of_tf_matrix(
...     column='author_keywords',
...     min_occ=6,
...     directory=directory,
...     plot=False,
... ).head()
                             dim0      dim1  ...     dim18     dim19
author_keywords                              ...                    
fintech                 11.732095 -0.807781  ...  0.047480 -0.087678
financial technologies   1.509205  4.965623  ... -0.017660 -0.121123
financial inclusion      1.410587 -0.040791  ... -0.045592  0.124723
block-chain              1.245573  0.114474  ... -0.280802  0.015832
innovating               0.939356  0.427864  ...  0.078966  0.193813
<BLANKLINE>
[5 rows x 20 columns]

"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import MDS

from .map_chart import map_chart
from .tf_matrix import tf_matrix


def svd_map_of_tf_matrix(
    column,
    min_occ=1,
    max_occ=None,
    directory="./",
    max_terms=150,
    dim_x=0,
    dim_y=1,
    figsize=(7, 7),
    svd__n_iter=5,
    random_state=0,
    plot=True,
):

    matrix = tf_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme="binary",
        sep="; ",
        directory=directory,
    ).transpose()

    max_dimensions = min(20, len(matrix.columns) - 1)

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions,
        n_iter=svd__n_iter,
        random_state=random_state,
    ).fit_transform(matrix)

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
