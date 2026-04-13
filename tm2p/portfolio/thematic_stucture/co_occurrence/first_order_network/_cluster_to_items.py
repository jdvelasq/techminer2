"""
ClusterToItems
===============================================================================

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AgglomerativeClustering
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  #       linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  #  always
    ...     compute_distances=True,  #  always True
    ... )
    >>> from tm2p.enum import AssociationIndex, Field, GraphClusteringAlgorithm, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import ClusterToItems
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_co_occurrence_threshold(1)
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
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['financial technology 015:02734',
         'financial literacy 005:00665',
         'economic growth 005:00660',
         'sustainable development 005:00604'],
     1: ['blockchain 011:02023',
         'artificial intelligence 008:01915',
         'crowdfunding 007:01245',
         'digital finance 005:02052'],
     2: ['banking 010:02599',
         'innovation 009:01703',
         'financial services 007:01673',
         'technology 007:01409'],
     3: ['green finance 011:02844', 'covid-19 006:01224', 'banks 005:00769'],
     4: ['china 009:01947', 'regtech 006:01481', 'sustainability 006:01357'],
     5: ['fintech 117:25478', 'financial inclusion 017:03823']}


    >>> # ---------------------------------------------------------------------
    >>> # LOOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['fintech 117:25478',
         'financial inclusion 017:03823',
         'china 009:01947',
         'regtech 006:01481',
         'sustainability 006:01357'],
     1: ['financial technology 015:02734',
         'green finance 011:02844',
         'financial literacy 005:00665',
         'economic growth 005:00660',
         'sustainable development 005:00604'],
     2: ['blockchain 011:02023',
         'artificial intelligence 008:01915',
         'crowdfunding 007:01245',
         'covid-19 006:01224',
         'digital finance 005:02052'],
     3: ['banking 010:02599',
         'innovation 009:01703',
         'financial services 007:01673',
         'technology 007:01409',
         'banks 005:00769']}





"""

from tm2p._intern.networks.cluster_to_items import BaseClusterToItems

from ._item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()
