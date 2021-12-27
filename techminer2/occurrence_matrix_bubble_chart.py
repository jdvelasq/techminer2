"""
Occurrence Matrix / Bubble Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/occurrence_matrix_bubble_chart.png"
>>> occurrence_matrix_bubble_chart(
...     directory=directory,
...     column='authors',
...     by='author_keywords',
...     min_occ=2, 
...     min_occ_by=6,
...     cmap='Greys',
...     figsize=(10, 10),
... ).savefig(file_name)

.. image:: images/occurrence_matrix_bubble_chart.png
    :width: 700px
    :align: center

"""

from .occurrence_matrix import occurrence_matrix
from .visualization_api.bubble_chart import bubble_chart


def occurrence_matrix_bubble_chart(
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    normalization=None,
    scheme=None,
    directory="./",
    cmap="Greys",
    figsize=(6, 6),
):
    matrix = occurrence_matrix(
        column=column,
        by=by,
        min_occ=min_occ,
        max_occ=max_occ,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )

    return bubble_chart(
        matrix=matrix,
        darkness=matrix,
        figsize=figsize,
        cmap=cmap,
        grid_lw=1.0,
        grid_c="gray",
        grid_ls=":",
    )
