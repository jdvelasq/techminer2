"""
TF-IDF Matrix / SVD Map
===============================================================================

Plots the SVD of the TFIDF matrix (0/1 values).

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Transpose the TF matrix

2. Apply SVD to the transposed matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/tf_idf_matrix_svd_map.png"
>>> tf_idf_matrix_svd_map(
...     column='author_keywords',
...     min_occ=6,
...     directory=directory,
... ).savefig(file_name)


.. image:: images/tf_idf_matrix_svd_map.png
    :width: 700px
    :align: center

>>> tf_idf_matrix_svd_map(
...     column='author_keywords',
...     min_occ=6,
...     directory=directory,
...     plot=False,
... ).head()
                            dim0      dim1  ...     dim18     dim19
author_keywords                             ...                    
fintech                 7.351135 -0.401663  ... -0.000113  0.004895
financial technologies  0.590853  3.559285  ... -0.072427  0.041903
financial inclusion     0.599857  0.179345  ... -0.045422  0.009677
blockchain              0.358602  0.375982  ... -0.266282 -0.662902
bank                    0.247483  0.507004  ... -0.049019 -0.039345
<BLANKLINE>
[5 rows x 20 columns]

"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .map_chart import map_chart
from .tf_idf_matrix import tf_idf_matrix


def tf_idf_matrix_svd_map(
    column,
    min_occ=1,
    max_occ=None,
    sep="; ",
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    directory="./",
    max_terms=150,
    dim_x=0,
    dim_y=1,
    figsize=(7, 7),
    svd__n_iter=5,
    random_state=0,
    plot=True,
):

    matrix = tf_idf_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme="binary",
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
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
