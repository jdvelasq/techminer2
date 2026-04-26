"""
ClusterToItems
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.intellect_struct.coupl_netw import ClusterToItems
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
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

* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Dirk A. Zetzsche 008:00699',
         'Ross P. Buckley 007:00887',
         'Douglas W. Arner 007:00887',
         'Michael Becker 002:00017',
    ...


"""

from tm2p._intern.netw.clust_to_item import BaseClusterToItems

from .item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()
