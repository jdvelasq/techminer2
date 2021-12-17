"""
TF-IDF SVD Map
===============================================================================

Plots the SVD of the TF-IDF matrix.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Transpose the TF-IDF matrix

2. Apply SVD to the transposed matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/svd_tf_idf_matrix_map.png"
>>> tf_idf_matrix = tf_idf_matrix('author_keywords', min_occ=6, directory=directory)
>>> svd_tf_idf_matrix_map(tf_idf_matrix).savefig(file_name)

.. image:: images/svd_tf_idf_matrix_map.png
    :width: 700px
    :align: center




"""

from .co_occurrence_matrix_svd_map import co_occurrence_matrix_svd_map


def tf_idf_svd_map(
    tf_idf_matrix,
    max_terms=150,
    dim_x=0,
    dim_y=1,
    figsize=(7, 7),
    n_iter=5,
    random_state=0,
):

    tf_idf_matrix = tf_idf_matrix.transpose()

    return co_occurrence_svd_map(
        tf_idf_matrix,
        max_terms=max_terms,
        dim_x=dim_x,
        dim_y=dim_y,
        figsize=figsize,
        n_iter=n_iter,
        random_state=random_state,
    )
