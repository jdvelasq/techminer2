"""
Thematic analysis of documents
===============================================================================

The implemented methodology is based on the Thematic Analysis of Elementary
Contexts implemented in T-LAB.

>>> from techminer2 import *
>>> directory = "data/"
>>> analysis = ThematicAnalysis(
...     column="author_keywords",
...     min_occ=4,
...     norm="l2",
...     use_idf=True,
...     smooth_idf=True,
...     sublinear_tf=False,
...     n_clusters=6,
...     linkage="ward",
...     affinity="euclidean",
...     directory=directory,
...     random_state=0, 
... )
>>> analysis.themes.head()
                     CL_0                    CL_1  ...     CL_4      CL_5
0                 fintech  financial technologies  ...  fintech  covid-19
1  financial technologies    peer-to-peer lending  ...            fintech
2                    bank                 fintech  ...            bitcoin
3              innovation              regulation  ...                   
4       financial service                          ...                   
<BLANKLINE>
[5 rows x 6 columns]

>>> analysis.partitions
CLUSTER
0    112
1     13
2     12
3      7
4     32
5      6
Name: num_documents, dtype: int64


>>> file_name = "/workspaces/techminer2/sphinx/images/thematic_analysis__mds_map.png"
>>> analysis.map().savefig(file_name)

.. image:: images/thematic_analysis__mds_map.png
    :width: 700px
    :align: center

"""

import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS

from .bubble_map import bubble_map
from .tf_idf_matrix import tf_idf_matrix


class ThematicAnalysis:
    def __init__(
        self,
        column,
        min_occ=None,
        norm="l2",
        use_idf=True,
        smooth_idf=True,
        sublinear_tf=False,
        n_clusters=6,
        linkage="ward",
        affinity="euclidean",
        directory="./",
        random_state=0,
    ):
        # -------------------------------------------------------------------------------
        tfidf = tf_idf_matrix(
            column=column,
            min_occ=min_occ,
            scheme="binary",
            norm=norm,
            use_idf=use_idf,
            smooth_idf=smooth_idf,
            sublinear_tf=sublinear_tf,
            directory=directory,
        )
        # -------------------------------------------------------------------------------
        mds = MDS(random_state=random_state)
        mds.fit(tfidf.transpose())
        self.mds_map = pd.DataFrame(
            mds.embedding_,
            columns=["DIM-0", "DIM-1"],
            index=tfidf.columns.tolist(),
        )

        # -------------------------------------------------------------------------------
        clustering = AgglomerativeClustering(
            n_clusters=n_clusters,
            linkage=linkage,
            affinity=affinity,
        )
        clustering.fit(tfidf)
        tfidf = tfidf.assign(CLUSTER=clustering.labels_)
        clusters = tfidf.groupby("CLUSTER").sum()
        format_str = "CL_{:02d}" if n_clusters > 9 else "CL_{:d}"
        clusters.index = [format_str.format(i) for i in range(n_clusters)]
        self.clusters = clusters.transpose()

        # -------------------------------------------------------------------------------
        themes = self.clusters.copy()
        themes.index = themes.index.get_level_values(0)
        max_len = 0
        for i_cluster in range(n_clusters):
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
        documents = tfidf[["CLUSTER"]].copy()
        documents = documents.reset_index(drop=False)
        documents = documents.groupby("CLUSTER").agg(list)
        documents.columns = ["record_no"]
        self._documents = documents

        # -------------------------------------------------------------------------------
        partitions = documents.copy()
        partitions = partitions.assign(num_documents=partitions.record_no.apply(len))
        partitions = partitions["num_documents"]
        self._partitions = partitions

        # -------------------------------------------------------------------------------
        clusters = self.clusters.copy()
        clusters = clusters.transpose()
        mds = MDS(n_components=n_clusters - 1, random_state=random_state)
        mds_data = mds.fit_transform(clusters)
        mds_data = pd.DataFrame(
            mds_data,
            columns=[f"DIM-{i}" for i in range(n_clusters - 1)],
            index=clusters.index,
        )
        self.mds_data = mds_data

    @property
    def themes(self):
        return self._themes

    @property
    def documents(self):
        return self._documents

    @property
    def partitions(self):
        return self._partitions

    def map(
        self,
        dim_x=0,
        dim_y=1,
        color_scheme="clusters",
        figsize=(9, 9),
    ):

        return bubble_map(
            node_x=self.mds_data.loc[:, f"DIM-{dim_x}"],
            node_y=self.mds_data.loc[:, f"DIM-{dim_y}"],
            node_clusters=range(len(self.mds_data)),
            node_texts=self.mds_data.index.tolist(),
            node_sizes=self._partitions.tolist(),
            x_axis_at=0,
            y_axis_at=0,
            color_scheme=color_scheme,
            xlabel=f"X-Axis (Dim-{dim_x})",
            ylabel=f"Y-Axis (Dim-{dim_y})",
            figsize=figsize,
            fontsize=7,
        )
