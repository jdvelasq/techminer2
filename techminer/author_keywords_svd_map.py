"""
Author keywords SVD map
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_keywords_svd_map.png"
>>> author_keywords_svd_map(min_occ=3, directory=directory).savefig(file_name)

.. image:: images/author_keywords_svd_map.png
    :width: 650px
    :align: center

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_svd_map import co_occurrence_svd_map


def author_keywords_svd_map(
    min_occ=2,
    max_occ=None,
    normalization=None,
    max_terms=150,
    dim_x=0,
    dim_y=1,
    figsize=(8, 8),
    n_iter=5,
    random_state=0,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="author_keywords",
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        directory=directory,
    )

    return co_occurrence_svd_map(
        coc_matrix,
        max_terms=max_terms,
        dim_x=dim_x,
        dim_y=dim_y,
        figsize=figsize,
        n_iter=n_iter,
        random_state=random_state,
    )
