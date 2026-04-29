"""
ItemToCluster
===============================================================================

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AgglomerativeClustering
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  # linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  # always True
    ...     compute_distances=True,  # always True
    ... )
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.direct_similarity_network import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
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
    {'artificial intelligence 008:01915': 4,
     'banking 013:03043': 0,
     'blockchain 012:03450': 1,
     'china 018:03596': 0,
     'commerce 006:02013': 1,
     'covid-19 009:01743': 0,
     'crowdfunding 007:01245': 1,
     'economic growth 009:01654': 0,
     'finance 029:07137': 0,
     'financial inclusion 017:03823': 0,
     'financial service 007:02627': 5,
     'financial services 011:02399': 0,
     'financial technology 016:02809': 3,
     'fintech 119:26148': 0,
     'green finance 011:02844': 0,
     'innovation 020:03916': 0,
     'sustainability 013:02308': 0,
     'sustainable development 015:02158': 0,
     'technology 007:01409': 2,
     'technology adoption 006:01500': 2}


    >>> mapping = (
    ...     ItemToCluster()
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence': 4,
     'banking': 0,
     'blockchain': 1,
     'china': 0,
     'commerce': 1,
     'covid-19': 0,
     'crowdfunding': 1,
     'economic growth': 0,
     'finance': 0,
     'financial inclusion': 0,
     'financial service': 5,
     'financial services': 0,
     'financial technology': 3,
     'fintech': 0,
     'green finance': 0,
     'innovation': 0,
     'sustainability': 0,
     'sustainable development': 0,
     'technology': 2,
     'technology adoption': 2}

    >>> # ---------------------------------------------------------------------
    >>> # DBSCAN
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import DBSCAN
    >>> estimator = DBSCAN(
    ...     eps=0.1,  # eps ∈ [0.1, 0.4] (tune empirically)
    ...     min_samples=3,  # min_samples ∈ [3, 10]
    ...     metric="precomputed",
    ... )
    >>> mapping = (
    ...     ItemToCluster()
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
    >>> pprint(mapping)
    {'artificial intelligence 008:01915': 0,
     'banking 013:03043': 0,
     'blockchain 012:03450': 0,
     'china 018:03596': 0,
     'commerce 006:02013': 0,
     'covid-19 009:01743': 0,
     'crowdfunding 007:01245': 0,
     'economic growth 009:01654': 0,
     'finance 029:07137': 0,
     'financial inclusion 017:03823': 0,
     'financial service 007:02627': 0,
     'financial services 011:02399': 0,
     'financial technology 016:02809': 0,
     'fintech 119:26148': 0,
     'green finance 011:02844': 0,
     'innovation 020:03916': 0,
     'sustainability 013:02308': 0,
     'sustainable development 015:02158': 0,
     'technology 007:01409': 0,
     'technology adoption 006:01500': 0}

    >>> # ---------------------------------------------------------------------
    >>> # SpectralClustering
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import SpectralClustering
    >>> estimator = SpectralClustering(
    ...     n_clusters=6,
    ...     affinity="precomputed",
    ...     assign_labels="kmeans",  # assign_labels ∈ {"kmeans", "discretize"}
    ...     random_state=0,
    ...     n_init=10,  # Used only when assign_labels="kmeans"
    ...     eigen_solver = "arpack",  # eigen_solver ∈ {"arpack", "lobpcg", "amg"}
    ...     n_components=None,  # Used only when eigen_solver="arpack"
    ... )
    >>> mapping = (
    ...     ItemToCluster()
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 2,
     'banking 013:03043': 5,
     'blockchain 012:03450': 3,
     'china 018:03596': 0,
     'commerce 006:02013': 3,
     'covid-19 009:01743': 5,
     'crowdfunding 007:01245': 3,
     'economic growth 009:01654': 0,
     'finance 029:07137': 0,
     'financial inclusion 017:03823': 4,
     'financial service 007:02627': 4,
     'financial services 011:02399': 1,
     'financial technology 016:02809': 2,
     'fintech 119:26148': 0,
     'green finance 011:02844': 0,
     'innovation 020:03916': 1,
     'sustainability 013:02308': 0,
     'sustainable development 015:02158': 0,
     'technology 007:01409': 1,
     'technology adoption 006:01500': 2}


    >>> # ---------------------------------------------------------------------
    >>> # AffinityPropagation
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import AffinityPropagation
    >>> estimator = AffinityPropagation(
    ...     affinity="precomputed",
    ...     damping=0.5,  # damping ∈ [0.5, 1.0)
    ...     max_iter=200,  # or higher
    ...     convergence_iter=15,
    ...     preference=3,  # approx the number of clusters (tune empirically)
    ...     random_state=0,
    ... )
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 14,
     'banking 013:03043': 7,
     'blockchain 012:03450': 9,
     'china 018:03596': 3,
     'commerce 006:02013': 18,
     'covid-19 009:01743': 12,
     'crowdfunding 007:01245': 17,
     'economic growth 009:01654': 13,
     'finance 029:07137': 1,
     'financial inclusion 017:03823': 4,
     'financial service 007:02627': 15,
     'financial services 011:02399': 11,
     'financial technology 016:02809': 5,
     'fintech 119:26148': 0,
     'green finance 011:02844': 10,
     'innovation 020:03916': 2,
     'sustainability 013:02308': 8,
     'sustainable development 015:02158': 6,
     'technology 007:01409': 16,
     'technology adoption 006:01500': 19}


    >>> # ---------------------------------------------------------------------
    >>> # LOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
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
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 0,
     'banking 013:03043': 2,
     'blockchain 012:03450': 0,
     'china 018:03596': 1,
     'commerce 006:02013': 0,
     'covid-19 009:01743': 2,
     'crowdfunding 007:01245': 0,
     'economic growth 009:01654': 1,
     'finance 029:07137': 0,
     'financial inclusion 017:03823': 0,
     'financial service 007:02627': 0,
     'financial services 011:02399': 2,
     'financial technology 016:02809': 1,
     'fintech 119:26148': 0,
     'green finance 011:02844': 1,
     'innovation 020:03916': 1,
     'sustainability 013:02308': 1,
     'sustainable development 015:02158': 1,
     'technology 007:01409': 2,
     'technology adoption 006:01500': 2}

"""

from tm2p._intern.netw.item_to_clust import BaseItemToCluster

from .dir_matrix import DirectMatrix


class ItemToCluster(
    BaseItemToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return DirectMatrix()
