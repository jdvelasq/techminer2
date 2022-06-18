"""
Occurrence Matrix / Sankey Diagram
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/occurrence_matrix_sankey_diagram.png"
>>> occurrence_matrix_sankey_diagram(
...     directory=directory,
...     column='authors',
...     by='author_keywords',
...     min_occ=3, 
...     min_occ_by=6,
...     figsize=(10, 10),
... ).savefig(file_name)

.. image:: images/occurrence_matrix_sankey_diagram.png
    :width: 700px
    :align: center

"""

from .occurrence_matrix import occurrence_matrix
from .sankey_diagram import sankey_diagram


def occurrence_matrix_sankey_diagram(
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    normalization=None,
    scheme=None,
    directory="./",
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

    return sankey_diagram(
        data=matrix,
        figsize=figsize,
    )
