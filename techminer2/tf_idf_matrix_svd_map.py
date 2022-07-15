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
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tf_idf_matrix_svd_map.html"

>>> tf_idf_matrix_svd_map(
...     column='author_keywords',
...     min_occ=6,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/tf_idf_matrix_svd_map.html" height="800px" width="100%" frameBorder="0"></iframe>



>>> tf_idf_matrix_svd_map(
...     column='author_keywords',
...     min_occ=6,
...     directory=directory,
...     plot=False,
... ).head()
                                              dim0  ...      dim9
regtech 70:462                            3.955303  ... -0.013210
fintech 42:406                            3.288423  ... -0.044653
blockchain 18:109                         1.479294  ... -0.113154
artificial intelligence 13:065            0.616298  ... -0.478101
regulatory technologies (regtech) 12:047  0.237330  ... -0.017035
<BLANKLINE>
[5 rows x 10 columns]



"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .map_chart import map_chart
from .tf_idf_matrix import tf_idf_matrix


def tf_idf_matrix_svd_map(
    column,
    min_occ=1,
    max_occ=None,
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    directory="./",
    dim_x=0,
    dim_y=1,
    svd__n_iter=5,
    random_state=0,
    plot=True,
    delta=1,
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

    max_dimensions = min(20, len(matrix.columns) - 1, len(matrix.index))

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions,
        n_iter=svd__n_iter,
        random_state=random_state,
    ).fit_transform(matrix)

    labels = matrix.index

    decomposed_matrix = pd.DataFrame(
        decomposed_matrix,
        columns=[f"dim{dim}" for dim in range(max_dimensions)],
        index=labels,
    )

    if plot is False:
        return decomposed_matrix

    return map_chart(
        dataframe=decomposed_matrix,
        dim_x=dim_x,
        dim_y=dim_y,
        delta=delta,
    )
