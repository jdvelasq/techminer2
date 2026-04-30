"""
ClusterToItems
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.direct import ClusterToItems  # type: ignore
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0',
         'Winz I, 2009, WATER RESOUR MANAG 16:0',
         'Sterman JD, 2001, CALIF MANAGE REV 14:0',
         'Xu ZX, 2002, WATER RESOUR MANAG 12:0',
         'Forrester J.W., 1980, TIMS STUDIES MANAGEM 11:0',
         'Feng YY, 2013, ECOL MODEL 11:0',
         'Saysel AK, 2002, J ENVIRON MANAGE 10:0',
    ...

"""

from tm2p._intern.netw.clust_to_unit import BaseClusterToUnits

from .item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToUnits,
):
    """:meta private:"""

    def unit_to_cluster(self):
        return ItemToCluster()
