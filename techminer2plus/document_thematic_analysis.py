# flake8: noqa
# pylint: disable=line-too-long
"""
Document Thematic Analysis
==================================

**Algortihm:**

1. Compute the TF matrix.
2. Apply TF-IDF transformation
3. Clustering using cosine distance
4. Obtain the table of units by clusters


>>> import techminer2plus
>>> root_dir = "data/regtech/"
>>> # 1. Define the clustering method and number of clusters
>>> from sklearn.cluster import AgglomerativeClustering
>>> estimator = AgglomerativeClustering(
...     n_clusters=5,
... ) 
>>> # 2. Compute the TF-IDF matrix
>>> tf_matrix = techminer2plus.analyze.tfidf.tf_matrix(
...     field='author_keywords',
...     top_n=50,
...     root_dir=root_dir,
... )
>>> tf_idf_matrix = techminer2plus.analyze.tfidf.tf_idf_matrix(tf_matrix)


>>> # 3. Cluster the documents 
>>> analysis = techminer2plus.analyze.thematic_analysis.document_thematic_analysis(
...     tf_idf_matrix=tf_idf_matrix,
...     estimator=estimator,
...     report_dir="document_thematic_analysis",
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/document_thematic_analysis/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_thematic_analysis/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_thematic_analysis/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_thematic_analysis/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_thematic_analysis/CL_04_abstracts_report.txt' was created.


>>> analysis.themes_.head()



"""
# import pandas as pd

# from ... import vantagepoint
# from ...make_report_dir import make_report_dir
# from ...records_lib import create_records_report, read_records
# from ..matrix import co_occurrence_matrix


def document_thematic_analysis(
    tf_idf_matrix,
    estimator,
    report_dir,
    root_dir="./",
):
    """Document Thematic Analysis."""

    def extract_records_per_cluster(dt_matrix):
        """Creates a dict of records per cluster."""

        clusters = dt_matrix["CLUSTER"].drop_duplicates().to_list()

        records_main = read_records(
            root_dir=root_dir,
        )

        records_per_cluster = {}

        for cluster in clusters:
            articles_in_cluster = dt_matrix[
                dt_matrix.CLUSTER == cluster
            ].index.to_list()
            clustered_records = records_main[
                records_main.article.isin(articles_in_cluster)
            ].copy()
            clustered_records = clustered_records.sort_values(
                ["global_citations", "local_citations"],
                ascending=[False, False],
            )

            records_per_cluster[cluster] = clustered_records.copy()

        return records_per_cluster

    def create_report(records_per_cluster):
        """Creates the report."""

        for cluster in sorted(records_per_cluster.keys()):
            records = records_per_cluster[cluster]
            report_filename = f"{cluster}_abstracts_report.txt"
            create_records_report(
                root_dir=root_dir,
                target_dir=report_dir,
                records=records,
                report_filename=report_filename,
            )

    dt_matrix = tf_idf_matrix.table_.copy()
    estimator.fit(dt_matrix)
    dt_matrix["CLUSTER"] = [f"CL_{label:>02d}" for label in estimator.labels_]

    make_report_dir(root_dir, report_dir)

    records_per_cluster = extract_records_per_cluster(dt_matrix)
    create_report(records_per_cluster)

    cooc_matrix = co_occurrence_matrix()


# class _ThematicAnalysis:
#     def __init__(
#         self,
#         criterion,
#         topic_occ_min=None,
#         topic_occ_max=None,
#         topic_citations_min=None,
#         topic_citations_max=None,
#         topics_length=None,
#         custom_topics=None,
#         clustering_method=None,
#         root_dir="./",
#         database="main",
#         start_year=None,
#         end_year=None,
#         norm="l2",
#         use_idf=True,
#         smooth_idf=True,
#         sublinear_tf=False,
#         **filters,
#     ):
#         self.criterion = criterion
#         self.criterion = criterion
#         self.topic_occ_min = topic_occ_min
#         self.topic_occ_max = topic_occ_max
#         self.topic_citations_min = topic_citations_min
#         self.topic_citations_max = topic_citations_max
#         self.topics_length = topics_length
#         self.custom_topics = custom_topics
#         self.clustering_method = clustering_method
#         self.root_dir = root_dir
#         self.database = database
#         self.start_year = start_year
#         self.end_year = end_year
#         self.norm = norm
#         self.use_idf = use_idf
#         self.smooth_idf = smooth_idf
#         self.sublinear_tf = sublinear_tf
#         self.filters = filters
#         #
#         self._tfidf_matrix = None
#         self._clusters = None
#         self._themes = None
#         self._partitions = None
#         self._documents = None
#         #
#         self._run()

#     def _run(self):
#         self._build_tf_idf_matrix()
#         self._apply_clustering()
#         self._compute_clusters()
#         self._compute_themes()
#         self._obtain_documents()
#         self._compute_partitions()

#     def _compute_partitions(self):
#         value_counts = self._tfidf_matrix.CLUSTER.value_counts()
#         value_counts.index = [
#             "CL_{:>02d}".format(i) for i in range(len(value_counts))
#         ]
#         self._partitions = value_counts

#     def _obtain_documents(self):
#         documents = self._tfidf_matrix[["CLUSTER"]].copy()
#         documents = documents.reset_index(drop=False)
#         documents = documents.groupby("CLUSTER").agg(list)
#         documents.columns = ["article"]
#         self._documents = documents

#     def _compute_themes(self):
#         themes = {}
#         for cluster in self._clusters.columns:
#             themes[cluster] = [
#                 (value, word)
#                 for word, value in zip(
#                     self._clusters.index, self._clusters[cluster]
#                 )
#                 if value > 0
#             ]

#         for theme in themes:
#             themes[theme].sort(key=lambda x: x[0], reverse=True)

#         for theme in themes:
#             themes[theme] = [word for _, word in themes[theme]]

#         self._themes = pd.DataFrame.from_dict(themes, orient="index").T
#         self._themes = self._themes.fillna("")

#     def _compute_clusters(self):
#         self._tfidf_matrix = self._tfidf_matrix.assign(
#             CLUSTER=self.clustering_method.labels_
#         )
#         self._clusters = self._tfidf_matrix.groupby("CLUSTER").sum()
#         n_clusters = self.clustering_method.n_clusters
#         self._clusters.index = [
#             "TH_{:>02d}".format(i) for i in range(n_clusters)
#         ]
#         self._clusters = self._clusters.transpose()

#     def _apply_clustering(self):
#         self.clustering_method.fit(self._tfidf_matrix)

#     def _build_tf_idf_matrix(self):
#         self._tfidf_matrix = vantagepoint.analyze.tfidf.tfidf_matrix(
#             criterion=self.criterion,
#             topics_length=self.topics_length,
#             topic_min_occ=self.topic_min_occ,
#             topic_min_citations=self.topic_min_citations,
#             custom_topics=self.custom_topics,
#             scheme="binary",
#             directory=self.root_dir,
#             database=self.database,
#             start_year=self.start_year,
#             end_year=self.end_year,
#             norm=self.norm,
#             use_idf=self.use_idf,
#             smooth_idf=self.smooth_idf,
#             sublinear_tf=self.sublinear_tf,
#             **self.filters,
#         )

#     ######

#     @property
#     def partitions_(self):
#         """Returns partitions"""
#         return self._partitions

#     @property
#     def themes_(self):
#         """Returns themes"""
#         return self._themes


# def thematic_analysis_of_contexts(
#     criterion,
#     topic_occ_min=None,
#     topic_occ_max=None,
#     topic_citations_min=None,
#     topic_citations_max=None,
#     topics_length=None,
#     clustering_method=None,
#     root_dir="./",
#     database="main",
#     start_year=None,
#     end_year=None,
#     **filters,
# ):
#     """Thematic Analysis of Elementary Contexts."""

#     return _ThematicAnalysis(
#         criterion=criterion,
#         topic_occ_min=topic_occ_min,
#         topic_occ_max=topic_occ_max,
#         topic_citations_min=topic_citations_min,
#         topic_citations_max=topic_citations_max,
#         topics_length=topics_length,
#         clustering_method=clustering_method,
#         root_dir=root_dir,
#         database=database,
#         start_year=start_year,
#         end_year=end_year,
#         **filters,
#     )
