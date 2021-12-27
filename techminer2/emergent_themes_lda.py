"""
Modeling of Emergent Themes with LDA
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> analysis = Emergent_Themes_LDA(
...     column="author_keywords",
...     min_occ=4,
...     max_occ=None,
...     scheme=None,
...     directory=directory,
...     n_components=6,
...     max_iter=5,
...     learning_offset=50.0,
...     random_state=0,
... )
>>> analysis.themes.head()
                     TH_0  ...                     TH_5
0                 fintech  ...             crowdfunding
1  financial technologies  ...                  fintech
2     financial inclusion  ...  artificial intelligence
3              regulating  ...         machine learning
4             block-chain  ...       internet of things
<BLANKLINE>
[5 rows x 6 columns]

>>> file_name = "/workspaces/techminer2/sphinx/images/emergent_themes_lda_mds_map.png"
>>> analysis.map().savefig(file_name)

.. image:: images/emergent_themes_lda_mds_map.png
    :width: 700px
    :align: center

"""
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.manifold import MDS

from .tf_matrix import tf_matrix
from .visualization_api.bubble_map import bubble_map


class Emergent_Themes_LDA:
    """
    Modeling of Emergent Themes with LDA
    """

    def __init__(
        self,
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
        # -------------------------------------------------------------------------------
        tf = tf_matrix(
            column=column,
            min_occ=min_occ,
            max_occ=max_occ,
            scheme=scheme,
            directory=directory,
        )

        # -------------------------------------------------------------------------------
        lda = LatentDirichletAllocation(
            n_components=n_components,
            max_iter=max_iter,
            learning_method="online",
            learning_offset=learning_offset,
            random_state=random_state,
        )

        lda.fit(tf)

        format_str = "TH_{:02d}" if n_components > 9 else "TH_{:d}"
        components = pd.DataFrame(
            lda.components_,
            index=[format_str.format(i) for i in range(n_components)],
            columns=tf.columns,
        )
        components = components.transpose()

        # -------------------------------------------------------------------------------
        themes = components.copy()
        themes.index = themes.index.get_level_values(0)
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
        self._themes = themes
        # -------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------
        clusters = components.copy()
        clusters = clusters.transpose()
        mds = MDS(n_components=2, random_state=random_state)
        mds_data = mds.fit_transform(clusters)
        mds_data = pd.DataFrame(
            mds_data,
            columns=[f"DIM-{i}" for i in range(2)],
            index=clusters.index,
        )
        self.mds_data = mds_data

    @property
    def themes(self):
        return self._themes

    def map(
        self,
        color_scheme="clusters",
        figsize=(9, 9),
    ):

        return bubble_map(
            node_x=self.mds_data.loc[:, "DIM-0"],
            node_y=self.mds_data.loc[:, "DIM-1"],
            node_clusters=range(len(self.mds_data)),
            node_texts=self.mds_data.index.tolist(),
            node_sizes=[1 for i in range(len(self.mds_data))],
            x_axis_at=0,
            y_axis_at=0,
            color_scheme=color_scheme,
            xlabel="X-Axis (Dim-0)",
            ylabel="Y-Axis (Dim-1)",
            figsize=figsize,
            fontsize=7,
        )
