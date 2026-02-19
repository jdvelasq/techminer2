"""
Terms by Cluster Dataframe
===============================================================================


Smoke tests:
    >>> from sklearn.cluster import KMeans
    >>> kmeans = KMeans(
    ...     n_clusters=4,
    ...     init="k-means++",
    ...     n_init=10,
    ...     max_iter=300,
    ...     tol=0.0001,
    ...     algorithm="lloyd",
    ...     random_state=0,
    ... )
    >>> from techminer2.packages.document_clustering import TermsByClusterDataFrame
    >>> (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_terms_in_top(50)
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
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(10)
                                   0  ...                             3
    0     FINANCIAL_SERVICES 05:0746  ...               FINTECH 32:5393
    1        BUSINESS_MODELS 03:1335  ...            BLOCKCHAIN 03:0881
    2  FINANCIAL_INSTITUTION 03:0488  ...   FINANCIAL_INCLUSION 03:0590
    3   FINANCIAL_TECHNOLOGY 03:0461  ...          CROWDFUNDING 03:0335
    4                BANKING 03:0370  ...   MARKETPLACE_LENDING 03:0317
    5             TECHNOLOGY 02:0310  ...      ELECTRONIC_MONEY 03:0305
    6                REGTECH 02:0266  ...           LENDINGCLUB 02:0253
    7                  CHINA 02:0150  ...  PEER_TO_PEER_LENDING 02:0253
    8                                 ...        SHADOW_BANKING 02:0253
    9                                 ...           P2P_LENDING 02:0161
    <BLANKLINE>
    [10 rows x 4 columns]


"""

import pandas as pd  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2.analyze.document_clustering.clusters_to_terms_mapping import (
    ClustersToTermsMapping,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        mapping = ClustersToTermsMapping().update(**self.params.__dict__).run()
        frame = pd.DataFrame.from_dict(mapping, orient="index").T
        frame = frame.fillna("")
        frame = frame.sort_index(axis=1)
        return frame
        frame = frame.sort_index(axis=1)
        return frame
