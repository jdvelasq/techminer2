"""
ClusterToItems
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.citation_network import ClusterToItems
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
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
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Anagnostopoulos I 2018 1:00284',
         'Lui A 2018 1:00096',
         'Das SR 2019 1:00090',
         'Takeda A 2021 1:00066',
         'Currie WL 2018 1:00043',
         'Fast V 2023 1:00040',
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
