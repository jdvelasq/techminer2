"""
Thematic analysis of documents
===============================================================================

The implemented methodology is based on the Thematic Analysis of Elementary
Contexts implemented in T-LAB.

**Algortihm:**

1. Compute the TF matrix.
2. Apply TF-IDF transformation
3. Clustering using cosine distance
4. Obtain the table of units by clusters


>>> from sklearn.cluster import AgglomerativeClustering
>>> clustering_alg = AgglomerativeClustering(n_clusters=5)

>>> from sklearn.feature_extraction.text import TfidfTransformer
>>> tfidf_transformer = TfidfTransformer(
...     norm='l2', 
...     use_idf=True, 
...     smooth_idf=True, 
...     sublinear_tf=False,
... )

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> analysis = thematic_analysis(
...     column="author_keywords",
...     min_occ=4,
...     directory=directory,
...     tfidf_transformer=tfidf_transformer,
...     clustering_alg=clustering_alg,
... )

>>> analysis.themes_.head()
                            CL_00  ...                    CL_04
0                  fintech 42:406  ...        blockchain 18:109
1                  regtech 70:462  ...           regtech 70:462
2  artificial intelligence 13:065  ...           fintech 42:406
3     financial regulation 08:091  ...        compliance 12:020
4               regulation 06:120  ...  cryptocurrencies 04:029
<BLANKLINE>
[5 rows x 5 columns]

>>> analysis.partitions_
CL_00    36
CL_01    16
CL_02    13
CL_03     9
CL_04     9
Name: CLUSTER, dtype: int64




"""
import pandas as pd

from .tf_matrix import tf_matrix


class _ThematicAnalysis:
    def __init__(
        self,
        # TF Matrix parameters
        column,
        min_occ=None,
        max_occ=None,
        directory="./",
        #
        tfidf_transformer=None,
        clustering_alg=None,
    ):
        self.column = column
        self.min_occ = min_occ
        self.max_occ = max_occ
        self.directory = directory
        self.tfidf_transformer = tfidf_transformer
        self.clustering_alg = clustering_alg
        #
        self._n_clusters = self.clustering_alg.n_clusters
        #
        self._tf_matrix = None
        self._tfidf_matrix = None
        self._clusters = None
        self._themes = None
        self._documents = None
        self._partitions = None
        #
        self._run()

    @property
    def partitions_(self):
        return self._partitions

    @property
    def themes_(self):
        return self._themes

    def _run(self):

        self._build_tf_matrix()
        self._build_tf_idf_matrix()
        self._apply_clustering()
        self._compute_clusters()
        self._compute_themes()
        self._obtain_documents()
        self._compute_partitions()

    def _obtain_documents(self):
        documents = self._tfidf_matrix[["CLUSTER"]].copy()
        documents = documents.reset_index(drop=False)
        documents = documents.groupby("CLUSTER").agg(list)
        documents.columns = ["record_no"]
        self._documents = documents

    def _compute_themes(self):

        themes = {}
        for cluster in self._clusters.columns:
            themes[cluster] = [
                (value, word)
                for word, value in zip(self._clusters.index, self._clusters[cluster])
                if value > 0
            ]

        for theme in themes:
            themes[theme].sort(key=lambda x: x[0], reverse=True)

        for theme in themes:
            themes[theme] = [word for _, word in themes[theme]]

        self._themes = pd.DataFrame.from_dict(themes, orient="index").T
        self._themes = self._themes.fillna("")

    def _compute_clusters(self):
        """Compute the clusters."""
        self._tfidf_matrix = self._tfidf_matrix.assign(
            CLUSTER=self.clustering_alg.labels_
        )
        self._clusters = self._tfidf_matrix.groupby("CLUSTER").sum()
        n_clusters = self.clustering_alg.n_clusters
        self._clusters.index = ["CL_{:>02d}".format(i) for i in range(n_clusters)]
        self._clusters = self._clusters.transpose()

    def _compute_partitions(self):
        value_counts = self._tfidf_matrix.CLUSTER.value_counts()
        value_counts.index = ["CL_{:>02d}".format(i) for i in range(len(value_counts))]
        self._partitions = value_counts

    def _apply_clustering(self):
        self.clustering_alg.fit(self._tfidf_matrix)

    def _build_tf_idf_matrix(self):
        tfidf_values = self.tfidf_transformer.fit_transform(self._tf_matrix.values)
        tfidf_matrix = pd.DataFrame(
            tfidf_values.todense(),
            index=self._tf_matrix.index,
            columns=self._tf_matrix.columns,
        )
        self._tfidf_matrix = tfidf_matrix

    def _build_tf_matrix(self):
        """Build the TF matrix."""

        self._tf_matrix = tf_matrix(
            column=self.column,
            min_occ=self.min_occ,
            max_occ=self.max_occ,
            directory=self.directory,
        )


def thematic_analysis(
    column,
    min_occ=None,
    max_occ=None,
    directory="./",
    #
    tfidf_transformer=None,
    clustering_alg=None,
):

    return _ThematicAnalysis(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        tfidf_transformer=tfidf_transformer,
        clustering_alg=clustering_alg,
    )


#####

# import pandas as pd
# from sklearn.cluster import AgglomerativeClustering
# from sklearn.manifold import MDS

# from .bubble_map import bubble_map
# from .tf_idf_matrix import tf_idf_matrix


# class ThematicAnalysis_:
#     def __init__(
#         self,
#         column,
#         min_occ=None,
#         norm="l2",
#         use_idf=True,
#         smooth_idf=True,
#         sublinear_tf=False,
#         n_clusters=6,
#         linkage="ward",
#         affinity="euclidean",
#         directory="./",
#         random_state=0,
#     ):
#         # -------------------------------------------------------------------------------
#         tfidf = tf_idf_matrix(
#             column=column,
#             min_occ=min_occ,
#             scheme="binary",
#             norm=norm,
#             use_idf=use_idf,
#             smooth_idf=smooth_idf,
#             sublinear_tf=sublinear_tf,
#             directory=directory,
#         )
#         # -------------------------------------------------------------------------------
#         mds = MDS(random_state=random_state)
#         mds.fit(tfidf.transpose())
#         self.mds_map = pd.DataFrame(
#             mds.embedding_,
#             columns=["DIM-0", "DIM-1"],
#             index=tfidf.columns.tolist(),
#         )

#         # -------------------------------------------------------------------------------
#         clustering = AgglomerativeClustering(
#             n_clusters=n_clusters,
#             linkage=linkage,
#             affinity=affinity,
#         )
#         clustering.fit(tfidf)
#         tfidf = tfidf.assign(CLUSTER=clustering.labels_)

#         clusters = tfidf.groupby("CLUSTER").sum()
#         format_str = "CL_{:02d}" if n_clusters > 9 else "CL_{:d}"
#         clusters.index = [format_str.format(i) for i in range(n_clusters)]
#         self.clusters = clusters.transpose()

#         # -------------------------------------------------------------------------------

#         # -------------------------------------------------------------------------------

#         # -------------------------------------------------------------------------------
#         partitions = documents.copy()
#         partitions = partitions.assign(num_documents=partitions.record_no.apply(len))
#         partitions = partitions["num_documents"]
#         self._partitions = partitions

#         # -------------------------------------------------------------------------------
#         clusters = self.clusters.copy()
#         clusters = clusters.transpose()
#         mds = MDS(n_components=n_clusters - 1, random_state=random_state)
#         mds_data = mds.fit_transform(clusters)
#         mds_data = pd.DataFrame(
#             mds_data,
#             columns=[f"DIM-{i}" for i in range(n_clusters - 1)],
#             index=clusters.index,
#         )
#         self.mds_data = mds_data

#     @property
#     def themes(self):
#         return self._themes

#     @property
#     def documents(self):
#         return self._documents

#     @property
#     def partitions(self):
#         return self._partitions

#     def map(
#         self,
#         dim_x=0,
#         dim_y=1,
#         color_scheme="clusters",
#         figsize=(9, 9),
#     ):

#         return bubble_map(
#             node_x=self.mds_data.loc[:, f"DIM-{dim_x}"],
#             node_y=self.mds_data.loc[:, f"DIM-{dim_y}"],
#             node_clusters=range(len(self.mds_data)),
#             node_texts=self.mds_data.index.tolist(),
#             node_sizes=self._partitions.tolist(),
#             x_axis_at=0,
#             y_axis_at=0,
#             color_scheme=color_scheme,
#             xlabel=f"X-Axis (Dim-{dim_x})",
#             ylabel=f"Y-Axis (Dim-{dim_y})",
#             figsize=figsize,
#             fontsize=7,
#         )
