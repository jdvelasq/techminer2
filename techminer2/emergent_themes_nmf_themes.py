"""
Emergent Themes NMF / Themes
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> emergent_themes_nmf_themes(
...     column="author_keywords",
...     min_occ=4,
...     directory=directory,
...     n_components=6,
...     init=None,
...     solver="cd",
...     beta_loss="frobenius",
...     max_iter=200,
...     random_state=0,
... ).head()
             TH_0  ...                           TH_5
0         fintech  ...            financial inclusion
1        covid-19  ...                        regtech
2  business model  ...  sustainable development goals
3  perceived risk  ...            financial stability
4         startup  ...                 sustainability
<BLANKLINE>
[5 rows x 6 columns]


"""

from .emergent_themes_nmf import Emergent_Themes_NMF


def emergent_themes_nmf_themes(
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

    return model.themes
