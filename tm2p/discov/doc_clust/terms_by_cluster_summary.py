"""
Terms by Cluster Summary
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
    >>> from tm2p.packages.document_clustering import TermsByClusterSummary
    >>> (
    ...     TermsByClusterSummary()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_item_counters(True)
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
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
       Cluster  ...                                              Terms
    0        0  ...  FINANCIAL_SERVICES 05:0746; BUSINESS_MODELS 03...
    1        1  ...  SUSTAINABILITY 03:0227; SUSTAINABLE_DEVELOPMEN...
    2        2  ...  FINANCE 11:1950; INNOVATION 08:0990; FINANCIAL...
    3        3  ...  FINTECH 32:5393; BLOCKCHAIN 03:0881; FINANCIAL...
    <BLANKLINE>
    [4 rows x 4 columns]



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.discov.doc_clust.clusters_to_terms_mapping import ClustersToTermsMapping


class TermsByClusterSummary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        mapping = ClustersToTermsMapping().update(**self.params.__dict__).run()
        clusters = sorted(mapping.keys())
        n_terms = [len(mapping[label]) for label in clusters]
        terms = ["; ".join(mapping[label]) for label in clusters]
        percentage = [round(n_term / sum(n_terms) * 100, 1) for n_term in n_terms]

        summary = pd.DataFrame(
            {
                "Cluster": clusters,
                "Num Terms": n_terms,
                "Percentage": percentage,
                "Terms": terms,
            }
        )

        return summary

        return summary
