"""
TermOccurrenceByCluster
===============================================================================

Smoke tests:
    >>> from sklearn.cluster import KMeans
    >>> kmeans = KMeans(
    ...     n_clusters=8,
    ...     init="k-means++",
    ...     n_init=10,
    ...     max_iter=300,
    ...     tol=0.0001,
    ...     algorithm="lloyd",
    ...     random_state=0,
    ... )
    >>> from tm2p.packages.document_clustering import TermOccurrenceByCluster
    >>> df = (
    ...     TermOccurrenceByCluster()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by("OCC")
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_row_normalization(None)
    ...     .using_idf_reweighting(False)
    ...     .using_idf_weights_smoothing(False)
    ...     .using_sublinear_tf_scaling(False)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict(kmeans)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(20))  # doctest: +NORMALIZE_WHITESPACE

    >>> df = (
    ...     TermOccurrenceByCluster()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by("OCC")
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_row_normalization(None)
    ...     .using_idf_reweighting(False)
    ...     .using_idf_weights_smoothing(False)
    ...     .using_sublinear_tf_scaling(False)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict(kmeans)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(20))  # doctest: +NORMALIZE_WHITESPACE



"""

from tm2p._intern import ParamsMixin
from tm2p.portf.themat_struct.tfidf.mtx import Matrix as TfIdf


class TermOccurrenceByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        tf_matrix = TfIdf().update(**self.params.__dict__).run()
        self.params.clustering.fit(tf_matrix)
        tf_matrix["cluster"] = list(self.params.clustering.labels_)
        data_frame = tf_matrix.groupby("cluster").sum()
        data_frame = data_frame.T

        return data_frame
