"""
Modeling of Emergent Themes
===============================================================================

Topic extraction using non-negative matrix factorization.


>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> nmf = tlab.modeling_of_emerging_themes.emergent_themes_with_nmf(
...     criterion="author_keywords",
...     topics_length=4,
...     directory=directory,
...     nmf__n_components=6,
...     nmf__init=None,
...     nmf__solver="mu",
...     nmf__beta_loss="frobenius",
...     nmf__max_iter=200,
...     nmf__random_state=0,
...  )
>>> nmf.themes_.head()
                          TH_00  ...                         TH_05
0                regtech 28:329  ...                fintech 12:249
1             compliance 07:030  ...                regtech 28:329
2  regulatory technology 07:037  ...             compliance 07:030
3                fintech 12:249  ...  regulatory technology 07:037
<BLANKLINE>
[4 rows x 6 columns]



>>> lda = tlab.modeling_of_emerging_themes.emergent_themes_with_lda(
...     criterion="author_keywords",
...     topics_length=4,
...     directory=directory,
...     lda__n_components=10,
...     lda__max_iter=5,
...     lda__learning_offset=50.0,
...     lda__random_state=0,
...  )    
>>> lda.themes_.head()
                          TH_00  ...                         TH_09
0                regtech 28:329  ...  regulatory technology 07:037
1  regulatory technology 07:037  ...                fintech 12:249
2             compliance 07:030  ...             compliance 07:030
3                fintech 12:249  ...                regtech 28:329
<BLANKLINE>
[4 rows x 10 columns]

"""


####
import pandas as pd
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.manifold import MDS

# from .bubble_map import bubble_map
from ...vantagepoint.analyze.tfidf.tf_matrix import tf_matrix

##################


class _Result:
    def __init__(self):
        self.themes_ = None
        self.mds_data_ = None


def emergent_themes_with_nmf(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    nmf__n_components=10,
    nmf__init=None,
    nmf__solver="cu",
    nmf__beta_loss="frobenius",
    nmf__max_iter=200,
    nmf__random_state=0,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Emergent Themes with NMF"""

    _tf_matrix = tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        scheme="binary",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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


def emergent_themes_with_lda(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    lda__n_components=10,
    lda__max_iter=5,
    lda__learning_offset=50.0,
    lda__random_state=0,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Emergent Themes with LDA"""

    _tf_matrix = tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        scheme="binary",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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
