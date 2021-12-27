"""
Auto-correlation Matrix / Heatmap
===============================================================================



>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/auto_corr_matrix_heatmap.png"
>>> auto_corr_matrix_heatmap(
...     column='authors', 
...     min_occ=2, 
...     directory=directory,
...     figsize=(10, 10),
... ).savefig(file_name)


.. image:: images/auto_corr_matrix_heatmap.png
    :width: 700px
    :align: center

"""


from .auto_corr_matrix import auto_corr_matrix
from .visualization_api.heat_map import heat_map


def auto_corr_matrix_heatmap(
    column,
    method="pearson",
    min_occ=1,
    max_occ=None,
    scheme=None,
    sep="; ",
    directory="./",
    cmap="Greys",
    figsize=(6, 6),
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

    return heat_map(
        matrix=matrix,
        cmap=cmap,
        figsize=figsize,
    )
