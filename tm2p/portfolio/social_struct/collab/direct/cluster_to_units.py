"""
ClusterToUnits
===============================================================================

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # LOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.direct import ClusterToUnits  # type: ignore
    >>> mapping = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
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
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Khalid El Makkaoui 0016:000178',
         'Ibrahim Ouahbi 0015:000178',
         'Yassine Maleh 0015:000178',
         'Ismail Lamaakal 0014:000176'],
     1: ['Luca Benini 0041:000706',
         'Michele Magno 0035:000501',
         'Alessio Burrello 0015:000114'],
     2: ['Ivanovitch Silva 0027:000442',
         'Marianne Silva 0020:000255',
         'Daniel G. Costa 0016:000312'],
     3: ['Sebastian Bader 0015:000207', 'Yuxuan Zhang 0014:000220'],
     4: ['Elisabetta Farella 0015:000129', 'Francesco Paissan 0013:000127'],
     5: ['Rajesh Gupta 0014:000003', 'Sudeep Tanwar 0014:000003'],
     6: ['Danilo Pau 0021:000125'],
     7: ['Marco Zennaro 0018:000115'],
     8: ['Manuel Roveri 0016:000160'],
     9: ['Danilo Pietro Pau 0016:000064']}

     
"""

from tm2p._intern.netw.clust_to_unit import BaseClusterToUnits

from .unit_to_cluster import UnitToCluster


class ClusterToUnits(
    BaseClusterToUnits,
):
    """:meta private:"""

    def unit_to_cluster(self):
        return UnitToCluster()
