"""
Co-occurrence Matrix / Bubble Chart
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_bubble_chart.png"
>>> co_occurrence_bubble_chart(
...     directory=directory,
...     column='authors',
...     min_occ=2, 
...     cmap='Greys',
... ).savefig(file_name)

.. image:: images/co_occurrence_bubble_chart.png
    :width: 700px
    :align: center

"""

from .bubble_chart import bubble_chart
from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_bubble_chart(
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

    return bubble_chart(
        matrix=matrix,
        darkness=matrix,
        figsize=figsize,
        cmap=cmap,
        grid_lw=1.0,
        grid_c="gray",
        grid_ls=":",
    )
