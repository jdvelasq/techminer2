"""
Emergent Themes LDA / Themes
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> emergent_themes_lda_themes(
...     column="author_keywords",
...     min_occ=4,
...     max_occ=None,
...     scheme=None,
...     directory=directory,
...     n_components=6,
...     max_iter=5,
...     learning_offset=50.0,
...     random_state=0,
... ).head()
                     TH_0  ...                     TH_5
0                 fintech  ...             crowdfunding
1  financial technologies  ...                  fintech
2     financial inclusion  ...  artificial intelligence
3              regulating  ...         machine learning
4             block-chain  ...       internet of things
<BLANKLINE>
[5 rows x 6 columns]


"""

from .emergent_themes_lda import Emergent_Themes_LDA


def emergent_themes_lda_themes(
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

    return model.themes
