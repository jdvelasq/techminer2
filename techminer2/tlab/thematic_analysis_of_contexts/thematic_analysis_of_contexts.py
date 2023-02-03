"""
Thematic Analysis of Contexts
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

>>> from techminer2 import tlab
>>> analysis = tlab.thematic_analysis_of_contexts.thematic_analysis_of_contexts(
...     criterion="author_keywords",
...     topic_min_occ=4,
...     directory=directory,
...     clustering_method=clustering_method,
... )

>>> analysis.themes_.head()
                            TH_00  ...           TH_04
0  artificial intelligence 04:023  ...  regtech 28:329
1     financial regulation 04:035  ...                
2       financial services 04:168  ...                
3                  regtech 28:329  ...                
4                  fintech 12:249  ...                
<BLANKLINE>
[5 rows x 5 columns]






"""
import pandas as pd

from ... import vantagepoint


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

        self._tfidf_matrix = vantagepoint.analyze.tfidf.tfidf_matrix(
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


def thematic_analysis_of_contexts(
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
