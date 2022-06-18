"""
Cross-correlation Matrix / Heatmap
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/cross_corr_matrix_heatmap.png"
>>> cross_corr_matrix_heatmap(
...     'authors',
...     min_occ=2, 
...     by='countries', 
...     min_occ_by=6, 
...     directory=directory,
... ).savefig(file_name) 

.. image:: images/cross_corr_matrix_heatmap.png
    :width: 700px
    :align: center

"""

from .cross_corr_matrix import cross_corr_matrix
from .heat_map import heat_map


def cross_corr_matrix_heatmap(
    column,
    by=None,
    method="pearson",
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    scheme=None,
    sep="; ",
    directory="./",
    cmap="Greys",
    figsize=(6, 6),
):

    matrix = cross_corr_matrix(
        column=column,
        by=by,
        method=method,
        min_occ=min_occ,
        max_occ=max_occ,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        scheme=scheme,
        sep=sep,
        directory=directory,
    )

    return heat_map(
        matrix=matrix,
        cmap=cmap,
        figsize=figsize,
    )
