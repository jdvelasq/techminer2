# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Term Occurrence by Cluster
===============================================================================

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
>>> from techminer2.pkgs.document_clustering import TermOccurrenceByCluster
>>> (
...     TermOccurrenceByCluster()
...     #
...     # FIELD:
...     .with_field("raw_keywords")
...     .having_terms_in_top(100)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # TFIDF:
...     .using_binary_term_frequencies(False)
...     .using_row_normalization(None)
...     .using_idf_reweighting(False)
...     .using_idf_weights_smoothing(False)
...     .using_sublinear_tf_scaling(False)
...     #
...     # CLUSTERING:
...     .using_clustering_algorithm_or_dict(kmeans)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head(20)
cluster                                0   1  2  3  4  5  6  7
raw_keywords                                                  
FINTECH 32:5393                        1  23  1  2  1  1  0  3
FINANCE 11:1950                        4   3  0  1  1  1  1  0
INNOVATION 08:0990                     0   4  0  4  0  0  0  0
FINANCIAL_SERVICES 05:0746             0   2  0  3  0  0  0  0
FINANCIAL_SERVICE 04:1036              1   0  0  1  0  1  1  0
BUSINESS_MODELS 03:1335                0   2  0  0  0  0  1  0
BLOCKCHAIN 03:0881                     0   2  0  0  0  0  1  0
COMMERCE 03:0846                       1   1  0  0  0  0  1  0
FINANCIAL_INCLUSION 03:0590            0   2  1  0  0  0  0  0
FINANCIAL_INSTITUTION 03:0488          0   2  0  1  0  0  0  0
SURVEYS 03:0484                        0   2  0  0  0  1  0  0
FINANCIAL_TECHNOLOGY 03:0461           1   2  0  0  0  0  0  0
BANKING 03:0370                        0   0  0  3  0  0  0  0
CROWDFUNDING 03:0335                   1   2  0  0  0  0  0  0
MARKETPLACE_LENDING 03:0317            0   0  0  0  0  0  0  3
ELECTRONIC_MONEY 03:0305               1   1  0  1  0  0  0  0
SUSTAINABILITY 03:0227                 3   0  0  0  0  0  0  0
SUSTAINABLE_DEVELOPMENT 03:0227        3   0  0  0  0  0  0  0
FINANCIAL_SERVICES_INDUSTRIES 02:0696  1   0  0  0  0  0  1  0
LITERATURE_REVIEW 02:0560              1   1  0  0  0  0  0  0




"""
from ..._internals.mixins import ParamsMixin
from ...database.metrics.tfidf import DataFrame as TfIdfDataFrame


class TermOccurrenceByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        tf_matrix = TfIdfDataFrame().update(**self.params.__dict__).run()
        self.params.clustering_algorithm_or_dict.fit(tf_matrix)
        tf_matrix["cluster"] = list(self.params.clustering_algorithm_or_dict.labels_)
        data_frame = tf_matrix.groupby("cluster").sum()
        data_frame = data_frame.T

        return data_frame
