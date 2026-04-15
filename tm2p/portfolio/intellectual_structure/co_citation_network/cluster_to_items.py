"""
ClusterToItems
===============================================================================

* **CITED_REF**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CoCitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ClusterToItems
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # CO-CITATION UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_citation_count(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Kurum E, 2023, Journal of Financial Crime 9:0',
         'Becker M, 2020, INTELL SYST ACCOUNT 9:0',
         'Turki M, 2020, HELIYON 8:0',
         'Singh C, 2021, J MONEY LAUND CONTRO 7:0',
    ...


"""

from tm2p._intern.networks.cluster_to_items import BaseClusterToItems

from .item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()
