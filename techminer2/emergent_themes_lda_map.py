"""
Emergent Themes LDA / MAP
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/emergent_themes_lda_mds_map.png"
>>> emergent_themes_lda_map(
...     column="author_keywords",
...     min_occ=4,
...     max_occ=None,
...     scheme=None,
...     directory=directory,
...     n_components=6,
...     max_iter=5,
...     learning_offset=50.0,
...     random_state=0,
...     color_scheme="clusters",
...     figsize=(9, 9),
... ).savefig(file_name)

.. image:: images/emergent_themes_lda_mds_map.png
    :width: 700px
    :align: center

"""

from .emergent_themes_lda import Emergent_Themes_LDA


def emergent_themes_lda_map(
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    directory="./",
    #
    n_components=10,
    max_iter=5,
    learning_offset=50.0,
    random_state=0,
    color_scheme="clusters",
    figsize=(9, 9),
):
    model = Emergent_Themes_LDA(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        directory=directory,
        n_components=n_components,
        max_iter=max_iter,
        learning_offset=learning_offset,
        random_state=random_state,
    )

    return model.map(
        color_scheme=color_scheme,
        figsize=figsize,
    )
