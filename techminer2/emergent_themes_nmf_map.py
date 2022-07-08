"""
Emergent Themes NMF / Map
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/emergent_themes_nmf_mds_map.png"
>>> emergent_themes_nmf_map(
...     column="author_keywords",
...     min_occ=4,
...     directory=directory,
...     n_components=6,
...     init=None,
...     solver="cd",
...     beta_loss="frobenius",
...     max_iter=200,
...     random_state=0,
...     color_scheme="clusters",
...     figsize=(9, 9),
... ).savefig(file_name)

.. image:: images/emergent_themes_nmf_mds_map.png
    :width: 700px
    :align: center



"""

from .emergent_themes_nmf import Emergent_Themes_NMF


def emergent_themes_nmf_map(
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    directory="./",
    #
    n_components=10,
    init=None,
    solver="cu",
    beta_loss="frobenius",
    max_iter=200,
    random_state=0,
    color_scheme="clusters",
    figsize=(9, 9),
):
    model = Emergent_Themes_NMF(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        directory=directory,
        #
        n_components=n_components,
        init=init,
        solver=solver,
        beta_loss=beta_loss,
        max_iter=max_iter,
        random_state=random_state,
    )

    return model.map(
        color_scheme=color_scheme,
        figsize=figsize,
    )
