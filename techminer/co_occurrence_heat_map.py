"""
Co-occurrence -- heat map
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> matrix = co_occurrence_matrix(directory, column='authors', min_occ=5)
>>> auto_corr_heat_map(matrix, num_terms=10)

.. image:: images/co_occurrence_heat_map.png
    :width: 500px
    :align: center

"""
from .heat_map import heat_map

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def co_occurrence_heat_map(
    co_occurrence_matrix,
    cmap="Greys",
    figsize=(6, 6),
    fontsize=9,
):
    matrix = co_occurrence_matrix.copy()

    return heat_map(
        matrix,
        cmap=cmap,
        figsize=figsize,
        fontsize=fontsize,
    )
