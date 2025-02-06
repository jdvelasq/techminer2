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
...     .with_field("descriptors")
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
...     .using_clustering_estimator_or_dict(kmeans)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head(20)
cluster                                   0  1  2  3  4  5  6  7
descriptors                                                     
FINTECH 46:7183                          40  0  1  2  0  1  1  1
FINANCE 21:3481                          16  0  0  2  1  1  0  1
FINANCIAL_TECHNOLOGY 17:2359             14  0  1  0  0  1  0  1
THIS_PAPER 14:2240                       10  1  1  0  0  1  1  0
THIS_STUDY 14:1737                       11  0  1  1  0  1  0  0
INNOVATION 13:2394                        9  1  0  1  1  1  0  0
TECHNOLOGY 13:1594                        9  0  1  0  0  1  1  1
FINANCIAL_SERVICES 11:1862                9  0  1  0  1  0  0  0
THE_FINANCIAL_INDUSTRY 09:2006            7  0  0  2  0  0  0  0
SERVICES 09:1527                          6  0  0  0  1  0  1  1
BANKS 09:1133                             7  0  1  0  0  1  0  0
REGULATORS 08:0974                        4  0  1  1  0  0  1  1
DATA 07:1086                              6  0  0  0  0  0  1  0
THE_DEVELOPMENT 07:1073                   4  1  1  0  0  0  0  1
BANKING 07:0851                           5  1  1  0  0  0  0  0
THIS_ARTICLE 06:1360                      5  0  0  1  0  0  0  0
THE_FINANCIAL_SERVICES_INDUSTRY 06:1237   2  1  1  0  1  0  1  0
THE_PURPOSE 06:1046                       4  0  1  0  0  1  0  0
THE_FIELD 06:1031                         4  0  0  2  0  0  0  0
CONSUMERS 06:0804                         5  0  1  0  0  0  0  0

"""
from ...database.metrics.tfidf import DataFrame as TfIdfDataFrame
from ...internals.mixins import InputFunctionsMixin


class TermOccurrenceByCluster(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        tf_matrix = TfIdfDataFrame().update_params(**self.params.__dict__).build()
        self.params.clustering_algorithm_or_dict.fit(tf_matrix)
        tf_matrix["cluster"] = list(self.params.clustering_algorithm_or_dict.labels_)
        data_frame = tf_matrix.groupby("cluster").sum()
        data_frame = data_frame.T

        return data_frame
