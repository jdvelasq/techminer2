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
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.latent_similarity_network import ClusterToItems
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['fintech 119:26148',
         'finance 029:07137',
         'innovation 020:03916',
         'china 018:03596',
         'financial technology 016:02809',
         'sustainable development 015:02158',
         'sustainability 013:02308',
         'green finance 011:02844',
         'covid-19 009:01743',
         'economic growth 009:01654',
         'technology 007:01409',
         'technology adoption 006:01500'],
     1: ['artificial intelligence 008:01915',
         'crowdfunding 007:01245',
         'commerce 006:02013'],
     2: ['financial inclusion 017:03823', 'financial services 011:02399'],
     3: ['banking 013:03043'],
     4: ['blockchain 012:03450'],
     5: ['financial service 007:02627']}


    >>> # ---------------------------------------------------------------------
    >>> # LOOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['finance 029:07137',
         'innovation 020:03916',
         'china 018:03596',
         'financial technology 016:02809',
         'sustainable development 015:02158',
         'banking 013:03043',
         'sustainability 013:02308',
         'green finance 011:02844',
         'covid-19 009:01743',
         'economic growth 009:01654',
         'technology 007:01409',
         'technology adoption 006:01500'],
     1: ['fintech 119:26148',
         'financial inclusion 017:03823',
         'blockchain 012:03450',
         'financial services 011:02399',
         'artificial intelligence 008:01915',
         'financial service 007:02627',
         'crowdfunding 007:01245',
         'commerce 006:02013']}


"""

from tm2p._intern.networks.cluster_to_items import BaseClusterToItems

from .item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()
