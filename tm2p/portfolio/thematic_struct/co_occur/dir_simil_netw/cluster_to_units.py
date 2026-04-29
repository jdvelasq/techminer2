"""
ClusterToUnits
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
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import ClusterToUnits
    >>> mapping = (
    ...     ClusterToUnits()
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
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(estimator)
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
    {0: ['tinyml 1031:010091',
         'machine learning 0766:008244',
         'tiny machine learning 0388:003654',
         'internet of things 0346:005415',
         'learning systems 0343:003524',
         'deep learning 0269:004143',
         'neural networks 0266:002432',
         'microcontrollers 0247:003364',
         'edge computing 0228:002411',
         'embedded systems 0186:002145',
         'energy efficiency 0153:002034',
         'deep neural networks 0137:001533',
         'embedded-system 0116:001320'],
     1: ['convolutional neural networks 0173:001295',
         'convolutional neural network 0144:001310',
         'real- time 0121:000533'],
     2: ['artificial intelligence 0129:001262'],
     3: ['iot 0118:001423'],
     4: ['edge ai 0104:001085'],
     5: ['machine learning models 0104:000937']}


    >>> # ---------------------------------------------------------------------
    >>> # LOOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ClusterToUnits()
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
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['tinyml 1031:010091',
         'machine learning 0766:008244',
         'tiny machine learning 0388:003654',
         'internet of things 0346:005415',
         'learning systems 0343:003524',
         'deep learning 0269:004143',
         'edge computing 0228:002411',
         'energy efficiency 0153:002034',
         'artificial intelligence 0129:001262',
         'iot 0118:001423',
         'edge ai 0104:001085',
         'machine learning models 0104:000937'],
     1: ['neural networks 0266:002432',
         'microcontrollers 0247:003364',
         'convolutional neural networks 0173:001295',
         'convolutional neural network 0144:001310',
         'deep neural networks 0137:001533',
         'real- time 0121:000533'],
     2: ['embedded systems 0186:002145', 'embedded-system 0116:001320']}


"""

from tm2p._intern.netw.clust_to_unit import BaseClusterToUnits

from .unit_to_cluster import UnitToCluster


class ClusterToUnits(
    BaseClusterToUnits,
):
    """:meta private:"""

    def item_to_cluster(self):
        return UnitToCluster()
