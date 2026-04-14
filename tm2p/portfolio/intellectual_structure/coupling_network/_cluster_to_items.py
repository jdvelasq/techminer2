"""
ClusterToItems
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.citation_network import ClusterToItems
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS


* **CitationUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     #
    ...     .having_items_in_top(50)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(1)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS


* **CitationUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     #
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS


* **CitationUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
    ...     #
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS


* **CitationUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_citation_unit(CitationUnit.SRC)
    ...     #
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS


"""

from tm2p._intern.networks.cluster_to_items import BaseClusterToItems

from .item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()
