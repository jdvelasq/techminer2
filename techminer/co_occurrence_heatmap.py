"""
Co-occurrence heatmap
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_heatmap.png"
>>> co_occurrence_heatmap(directory=directory, column='authors', min_occ=2, cmap='Greys').savefig(file_name)

.. image:: images/co_occurrence_heatmap.png
    :width: 700px
    :align: center

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .heat_map import heat_map


def co_occurrence_heatmap(
    column,
    min_occ=1,
    max_occ=None,
    normalization=None,
    scheme=None,
    directory="./",
    cmap="Greys",
    figsize=(6, 6),
):
    matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )

    return heat_map(
        matrix=matrix,
        cmap=cmap,
        figsize=figsize,
    )
