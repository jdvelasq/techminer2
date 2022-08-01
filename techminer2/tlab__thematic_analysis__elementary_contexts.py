"""
Thematic Analysis of Documents
===============================================================================

The implemented methodology is based on the Thematic Analysis of Elementary
Contexts implemented in T-LAB.

**Algortihm:**

1. Compute the TF matrix.
2. Apply TF-IDF transformation
3. Clustering using cosine distance
4. Obtain the table of units by clusters

>>> directory = "data/regtech/"

>>> from sklearn.cluster import AgglomerativeClustering
>>> clustering_method = AgglomerativeClustering(n_clusters=5)

>>> from techminer2 import tlab__thematic_analysis__elementary_contexts
>>> analysis = tlab__thematic_analysis__elementary_contexts(
...     criterion="author_keywords",
...     topic_min_occ=4,
...     directory=directory,
...     clustering_method=clustering_method,
... )

>>> analysis.themes_.head()
                            TH_00  ...                  TH_04
0                  fintech 42:406  ...      blockchain 18:109
1                  regtech 69:461  ...         regtech 69:461
2  artificial intelligence 13:065  ...         fintech 42:406
3     financial regulation 08:091  ...      compliance 12:020
4               regulation 06:120  ...  cryptocurrency 04:029
<BLANKLINE>
[5 rows x 5 columns]






"""
import pandas as pd

from .vantagepoint__tf_idf_matrix import vantagepoint__tf_idf_matrix


class _ThematicAnalysis:
    def __init__(
        self,
        criterion,
        topics_length=None,
        topic_min_occ=None,
        topic_min_citations=None,
        custom_topics=None,
        clustering_method=None,
        directory="./",
        database="documents",
        start_year=None,
        end_year=None,
        norm="l2",
        use_idf=True,
        smooth_idf=True,
        sublinear_tf=False,
        **filters,
    ):
        self.criterion = criterion
        self.criterion = criterion
        self.topics_length = topics_length
        self.topic_min_occ = topic_min_occ
        self.topic_min_citations = topic_min_citations
        self.custom_topics = custom_topics
        self.clustering_method = clustering_method
        self.directory = directory
        self.database = database
        self.start_year = start_year
        self.end_year = end_year
        self.norm = norm
        self.use_idf = use_idf
        self.smooth_idf = smooth_idf
        self.sublinear_tf = sublinear_tf
        self.filters = filters
        #
        self._tfidf_matrix = None
        self._clusters = None
        self._themes = None
        self._partitions = None
        self._documents = None
        #
        self._run()

    def _run(self):

        self._build_tf_idf_matrix()
        self._apply_clustering()
        self._compute_clusters()
        self._compute_themes()
        self._obtain_documents()
        self._compute_partitions()

    def _compute_partitions(self):
        value_counts = self._tfidf_matrix.CLUSTER.value_counts()
        value_counts.index = ["CL_{:>02d}".format(i) for i in range(len(value_counts))]
        self._partitions = value_counts

    def _obtain_documents(self):
        documents = self._tfidf_matrix[["CLUSTER"]].copy()
        documents = documents.reset_index(drop=False)
        documents = documents.groupby("CLUSTER").agg(list)
        documents.columns = ["article"]
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
        self._tfidf_matrix = self._tfidf_matrix.assign(
            CLUSTER=self.clustering_method.labels_
        )
        self._clusters = self._tfidf_matrix.groupby("CLUSTER").sum()
        n_clusters = self.clustering_method.n_clusters
        self._clusters.index = ["TH_{:>02d}".format(i) for i in range(n_clusters)]
        self._clusters = self._clusters.transpose()

    def _apply_clustering(self):
        self.clustering_method.fit(self._tfidf_matrix)

    def _build_tf_idf_matrix(self):

        self._tfidf_matrix = vantagepoint__tf_idf_matrix(
            criterion=self.criterion,
            topics_length=self.topics_length,
            topic_min_occ=self.topic_min_occ,
            topic_min_citations=self.topic_min_citations,
            custom_topics=self.custom_topics,
            scheme="binary",
            directory=self.directory,
            database=self.database,
            start_year=self.start_year,
            end_year=self.end_year,
            norm=self.norm,
            use_idf=self.use_idf,
            smooth_idf=self.smooth_idf,
            sublinear_tf=self.sublinear_tf,
            **self.filters,
        )

    ######

    @property
    def partitions_(self):
        """Returns partitions"""
        return self._partitions

    @property
    def themes_(self):
        """Returns themes"""
        return self._themes


def tlab__thematic_analysis__elementary_contexts(
    criterion,
    topic_min_occ=None,
    topic_min_citations=None,
    clustering_method=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Thematic Analysis of Elementary Contexts."""

    return _ThematicAnalysis(
        criterion=criterion,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        clustering_method=clustering_method,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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
