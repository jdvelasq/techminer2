"""
ItemsByCluster
===============================================================================


Smoke tests:
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  #       linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  #  always
    ...     compute_distances=True,  #  always True
    ... )
    >>> from tm2p.enum import CoOccurrenceUnit, Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.latent_similarity_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
    ...     #
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_item_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(estimator)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                               0                                  1                              2                  3                     4                            5
    ITEM
    0                     fintech 119:26148  artificial intelligence 008:01915  financial inclusion 017:03823  banking 013:03043  blockchain 012:03450  financial service 007:02627
    1                     finance 029:07137             crowdfunding 007:01245   financial services 011:02399
    2                  innovation 020:03916                 commerce 006:02013
    3                       china 018:03596
    4        financial technology 016:02809

    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
    ...     #
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(estimator)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                     0                        1                    2        3           4                  5
    ITEM
    0                     fintech  artificial intelligence  financial inclusion  banking  blockchain  financial service
    1                     finance             crowdfunding   financial services
    2                  innovation                 commerce
    3                       china
    4        financial technology


"""

from tm2p._intern.networks.items_by_cluster import BaseItemsByCluster

from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):
        return ClusterToItems()
