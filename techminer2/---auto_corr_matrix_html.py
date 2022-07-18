"""
Auto-correlation Matrix / HTML
===============================================================================



>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> auto_corr_matrix_html(
...     column='authors', 
...     min_occ=6, 
...     directory=directory,
... ) # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler ...



"""


from .vp.analyze.matrix.auto_corr_matrix import auto_corr_matrix


def auto_corr_matrix_html(
    column,
    method="pearson",
    min_occ=1,
    max_occ=None,
    scheme=None,
    sep="; ",
    directory="./",
    cmap="Greys",
):

    matrix = auto_corr_matrix(
        column=column,
        method=method,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        sep=sep,
        directory=directory,
    )

    return matrix.style.background_gradient(cmap=cmap, axis=None)
