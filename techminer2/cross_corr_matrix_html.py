"""
Cross-correlation Matrix / HTML
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> cross_corr_matrix_html(
...     'authors',
...     min_occ=3, 
...     by='countries', 
...     min_occ_by=6, 
...     directory=directory,
... ) # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler ...


"""

from .cross_corr_matrix import cross_corr_matrix


def cross_corr_matrix_html(
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

    return matrix.style.background_gradient(cmap=cmap, axis=None)
