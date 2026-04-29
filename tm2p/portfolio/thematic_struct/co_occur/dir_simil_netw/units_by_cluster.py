"""
UnitsByCluster
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import UnitsByCluster  # type: ignore
    >>> df = (
    ...     UnitsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
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
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                  0                                          1                             2
    UNIT
    0                       tinyml 1031:010091                neural networks 0266:002432  embedded systems 0186:002145
    1             machine learning 0766:008244               microcontrollers 0247:003364   embedded-system 0116:001320
    2        tiny machine learning 0388:003654  convolutional neural networks 0173:001295
    3           internet of things 0346:005415   convolutional neural network 0144:001310
    4             learning systems 0343:003524           deep neural networks 0137:001533


    >>> df = (
    ...     UnitsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
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
    ...     .using_counters(False)
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
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                      0                              1                 2
    UNIT
    0                       tinyml                neural networks  embedded systems
    1             machine learning               microcontrollers   embedded-system
    2        tiny machine learning  convolutional neural networks
    3           internet of things   convolutional neural network
    4             learning systems           deep neural networks



"""

from tm2p._intern.netw.unit_by_clust import BaseUnitByCluster

from .cluster_to_units import ClusterToUnits


class UnitsByCluster(
    BaseUnitByCluster,
):
    """:meta private:"""

    def cluster_to_units(self):
        return ClusterToUnits()
