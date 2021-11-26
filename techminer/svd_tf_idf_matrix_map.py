"""
SVD of the TF-IDF matrix
===============================================================================

Plots the SVD of the TF-IDF matrix.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Transpose the TF-IDF matrix

2. Apply SVD to the transposed matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/svd_tf_idf_matrix_map.png"
>>> tf_idf_matrix = tf_idf_matrix(directory, 'author_keywords', min_occ=10)
>>> svd_tf_idf_matrix_map(tf_idf_matrix).savefig(file_name)

.. image:: images/svd_tf_idf_matrix_map.png
    :width: 700px
    :align: center




"""

from .svd_co_occurrence_matrix_map import svd_co_occurrence_matrix_map


def svd_tf_idf_matrix_map(
    tf_idf_matrix,
    max_terms=150,
    dim_x=0,
    dim_y=1,
    figsize=(7, 7),
    n_iter=5,
    random_state=0,
):

    tf_idf_matrix = tf_idf_matrix.transpose()

    return svd_co_occurrence_matrix_map(
        tf_idf_matrix,
        max_terms=max_terms,
        dim_x=dim_x,
        dim_y=dim_y,
        figsize=figsize,
        n_iter=n_iter,
        random_state=random_state,
    )
