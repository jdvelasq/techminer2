"""
Co-occurrence Matrix / HTML visualization
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_matrix_html.png"
>>> co_occurrence_matrix_html(
...     directory=directory, 
...     column='authors', 
...     min_occ=2, 
...     cmap='Greys',
... ) # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler ...

"""

from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_matrix_html(
    column,
    min_occ=1,
    max_occ=None,
    normalization=None,
    scheme=None,
    directory="./",
    cmap="Greys",
):
    matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )

    return matrix.style.background_gradient(cmap=cmap, axis=None)
