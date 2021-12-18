"""
Occurrence Matrix / HTML
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> occurrence_matrix_html(
...     directory=directory, 
...     column='authors', 
...     min_occ=2, 
...     cmap='Greys',
... ) # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler ...

"""

from .occurrence_matrix import occurrence_matrix


def occurrence_matrix_html(
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

    return matrix.style.background_gradient(cmap=cmap, axis=None)
