"""
Modeling of Emergent Themes
===============================================================================

Topic extraction using non-negative matrix factorization.


>>> directory = "data/regtech/"

>>> from techminer2 import tlab__emergent_themes_with_nmf
>>> nmf = tlab__emergent_themes_with_nmf(
...     column="author_keywords",
...     min_occ=4,
...     max_occ=None,
...     directory=directory,
...     nmf__n_components=6,
...     nmf__init=None,
...     nmf__solver="mu",
...     nmf__beta_loss="frobenius",
...     nmf__max_iter=200,
...     nmf__random_state=0,
...  )


>>> nmf.themes_.head()
                         TH_00  ...                TH_05
0               regtech 70:462  ...    regulation 06:120
1               fintech 42:406  ...    innovation 04:029
2   financial inclusion 05:068  ...      big data 04:027
3     financial service 05:135  ...          bank 04:001
4  financial regulation 08:091  ...  crowdfunding 04:030
<BLANKLINE>
[5 rows x 6 columns]



>>> from techminer2 import tlab__emergent_themes_with_lda
>>> lda = tlab__emergent_themes_with_lda(
...     column="author_keywords",
...     min_occ=4,
...     max_occ=None,
...     directory=directory,
...     lda__n_components=10,
...     lda__max_iter=5,
...     lda__learning_offset=50.0,
...     lda__random_state=0,
...  )    

>>> lda.themes_.head()
               TH_00  ...                           TH_09
0     regtech 70:462  ...    anti-money laundering 04:030
1  blockchain 18:109  ...                     bank 04:001
2     fintech 42:406  ...  artificial intelligence 13:065
3  regulation 06:120  ...                insurtech 04:005
4        bank 04:001  ...        financial service 05:135
<BLANKLINE>
[5 rows x 10 columns]

"""


####
import pandas as pd
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.manifold import MDS

# from .bubble_map import bubble_map
from .vantagepoint__tf_matrix import vantagepoint__tf_matrix

##################


class _Result:
    def __init__(self):
        self.themes_ = None
        self.mds_data_ = None


def tlab__emergent_themes_with_nmf(
    column,
    min_occ=None,
    max_occ=None,
    directory="./",
    nmf__n_components=10,
    nmf__init=None,
    nmf__solver="cu",
    nmf__beta_loss="frobenius",
    nmf__max_iter=200,
    nmf__random_state=0,
):
    """Emergent Themes with NMF"""

    _tf_matrix = vantagepoint__tf_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
    )

    nmf = NMF(
        n_components=nmf__n_components,
        init=nmf__init,
        solver=nmf__solver,
        beta_loss=nmf__beta_loss,
        max_iter=nmf__max_iter,
        random_state=nmf__random_state,
    )
    nmf.fit(_tf_matrix)

    components = pd.DataFrame(
        nmf.components_,
        index=["TH_{:>02d}".format(i) for i in range(nmf__n_components)],
        columns=_tf_matrix.columns,
    )
    components = components.transpose()
    themes = _extract_themes(components, nmf__n_components)
    mds_data = _get_mds_data(components, nmf__random_state)

    result = _Result()
    result.themes_ = themes
    result.mds_data_ = mds_data

    return result


def tlab__emergent_themes_with_lda(
    column,
    min_occ=None,
    max_occ=None,
    directory="./",
    lda__n_components=10,
    lda__max_iter=5,
    lda__learning_offset=50.0,
    lda__random_state=0,
):
    """Emergent Themes with NMF"""

    _tf_matrix = vantagepoint__tf_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
    )

    lda = LatentDirichletAllocation(
        n_components=lda__n_components,
        max_iter=lda__max_iter,
        learning_method="online",
        learning_offset=lda__learning_offset,
        random_state=lda__random_state,
    )

    lda.fit(_tf_matrix)

    components = pd.DataFrame(
        lda.components_,
        index=["TH_{:>02d}".format(i) for i in range(lda__n_components)],
        columns=_tf_matrix.columns,
    )
    components = components.transpose()
    themes = _extract_themes(components, lda__n_components)
    mds_data = _get_mds_data(components, lda__random_state)

    result = _Result()
    result.themes_ = themes
    result.mds_data_ = mds_data

    return result


def _extract_themes(components, n_components):

    themes = components.copy()
    max_len = 0
    for i_cluster in range(n_components):
        themes_members = themes.iloc[:, i_cluster].copy()
        themes_members = themes_members.sort_values(ascending=False)
        themes_members = [
            index if value > 0 else ""
            for index, value in zip(themes_members.index, themes_members.values)
        ]
        max_len = max(
            max_len, len([member for member in themes_members if member != ""])
        )
        themes.iloc[:, i_cluster] = themes_members
    themes = themes.reset_index(drop=True)
    themes = themes.head(max_len)
    return themes


def _get_mds_data(components, random_state):
    clusters = components.copy()
    clusters = clusters.transpose()
    mds = MDS(n_components=2, random_state=random_state)
    mds_data = mds.fit_transform(clusters)
    mds_data = pd.DataFrame(
        mds_data,
        columns=[f"DIM-{i}" for i in range(2)],
        index=clusters.index,
    )
    return mds_data
