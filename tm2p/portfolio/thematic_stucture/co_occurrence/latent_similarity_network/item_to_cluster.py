"""
ItemsToCluster
===============================================================================

Smoke test:
    >>> from tm2p.enum import AssociationIndex, CoOccurrenceUnit, GraphClusteringAlgorithm, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.latent_similarity_network import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
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
    >>> pprint(mapping)
    {'artificial intelligence 008:01915': 1,
     'banking 013:03043': 0,
     'blockchain 012:03450': 1,
     'china 018:03596': 0,
     'commerce 006:02013': 1,
     'covid-19 009:01743': 0,
    ...


"""

from tm2p._intern.networks.item_to_cluster import BaseItemToCluster

from .latent_matrix import LatentMatrix


class ItemToCluster(
    BaseItemToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return LatentMatrix()
