"""
Occurrence Matrix / Heatmap
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/occurrence_matrix_heatmap.png"
>>> occurrence_matrix_heatmap(
...     directory=directory,
...     column='authors',
...     by='author_keywords',
...     min_occ=2, 
...     min_occ_by=6,
...     cmap='Greys',
...     figsize=(10, 10),
... ).savefig(file_name)

.. image:: images/occurrence_matrix_heatmap.png
    :width: 700px
    :align: center

"""

from .heat_map import heat_map
from .occurrence_matrix import occurrence_matrix


def occurrence_matrix_heatmap(
    column,
    min_occ=1,
    max_occ=None,
    by=None,
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
        min_occ=min_occ,
        max_occ=max_occ,
        by=by,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )

    return heat_map(
        matrix=matrix,
        cmap=cmap,
        figsize=figsize,
    )
