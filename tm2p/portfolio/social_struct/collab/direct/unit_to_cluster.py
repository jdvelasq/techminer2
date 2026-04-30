"""
UnitToCluster
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
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.direct import UnitToCluster  # type: ignore
    >>> mapping = (
    ...     UnitToCluster()
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
    {'Alessio Burrello 0015:000114': 0,
     'Daniel G. Costa 0016:000312': 1,
     'Danilo Pau 0021:000125': 1,
     'Danilo Pietro Pau 0016:000064': 5,
     'Elisabetta Farella 0015:000129': 0,
     'Francesco Paissan 0013:000127': 0,
     'Ibrahim Ouahbi 0015:000178': 2,
     'Ismail Lamaakal 0014:000176': 2,
     'Ivanovitch Silva 0027:000442': 1,
     'Khalid El Makkaoui 0016:000178': 2,
     'Luca Benini 0041:000706': 0,
     'Manuel Roveri 0016:000160': 4,
     'Marco Zennaro 0018:000115': 1,
     'Marianne Silva 0020:000255': 1,
     'Michele Magno 0035:000501': 0,
     'Rajesh Gupta 0014:000003': 3,
     'Sebastian Bader 0015:000207': 0,
     'Sudeep Tanwar 0014:000003': 3,
     'Yassine Maleh 0015:000178': 2,
     'Yuxuan Zhang 0014:000220': 0}


    >>> mapping = (
    ...     UnitToCluster()
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
    {'Alessio Burrello': 0,
     'Daniel G. Costa': 1,
     'Danilo Pau': 1,
     'Danilo Pietro Pau': 5,
     'Elisabetta Farella': 0,
     'Francesco Paissan': 0,
     'Ibrahim Ouahbi': 2,
     'Ismail Lamaakal': 2,
     'Ivanovitch Silva': 1,
     'Khalid El Makkaoui': 2,
     'Luca Benini': 0,
     'Manuel Roveri': 4,
     'Marco Zennaro': 1,
     'Marianne Silva': 1,
     'Michele Magno': 0,
     'Rajesh Gupta': 3,
     'Sebastian Bader': 0,
     'Sudeep Tanwar': 3,
     'Yassine Maleh': 2,
     'Yuxuan Zhang': 0}


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
    ...     UnitToCluster()
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
    {'Alessio Burrello 0015:000114': 0,
     'Daniel G. Costa 0016:000312': 0,
     'Danilo Pau 0021:000125': 0,
     'Danilo Pietro Pau 0016:000064': 0,
     'Elisabetta Farella 0015:000129': 0,
     'Francesco Paissan 0013:000127': 0,
     'Ibrahim Ouahbi 0015:000178': 1,
     'Ismail Lamaakal 0014:000176': 1,
     'Ivanovitch Silva 0027:000442': 0,
     'Khalid El Makkaoui 0016:000178': 1,
     'Luca Benini 0041:000706': 0,
     'Manuel Roveri 0016:000160': 0,
     'Marco Zennaro 0018:000115': 0,
     'Marianne Silva 0020:000255': 0,
     'Michele Magno 0035:000501': 0,
     'Rajesh Gupta 0014:000003': 0,
     'Sebastian Bader 0015:000207': 0,
     'Sudeep Tanwar 0014:000003': 0,
     'Yassine Maleh 0015:000178': 1,
     'Yuxuan Zhang 0014:000220': 0}



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
    ...     UnitToCluster()
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
    {'Alessio Burrello 0015:000114': 1,
     'Daniel G. Costa 0016:000312': 2,
     'Danilo Pau 0021:000125': 0,
     'Danilo Pietro Pau 0016:000064': 0,
     'Elisabetta Farella 0015:000129': 4,
     'Francesco Paissan 0013:000127': 4,
     'Ibrahim Ouahbi 0015:000178': 0,
     'Ismail Lamaakal 0014:000176': 0,
     'Ivanovitch Silva 0027:000442': 2,
     'Khalid El Makkaoui 0016:000178': 0,
     'Luca Benini 0041:000706': 1,
     'Manuel Roveri 0016:000160': 0,
     'Marco Zennaro 0018:000115': 0,
     'Marianne Silva 0020:000255': 2,
     'Michele Magno 0035:000501': 1,
     'Rajesh Gupta 0014:000003': 5,
     'Sebastian Bader 0015:000207': 3,
     'Sudeep Tanwar 0014:000003': 5,
     'Yassine Maleh 0015:000178': 0,
     'Yuxuan Zhang 0014:000220': 3}



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
    ...     UnitToCluster()
    ...     #
    ...     # FIELD:
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
    {'Alessio Burrello 0015:000114': 14,
     'Daniel G. Costa 0016:000312': 6,
     'Danilo Pau 0021:000125': 3,
     'Danilo Pietro Pau 0016:000064': 9,
     'Elisabetta Farella 0015:000129': 13,
     'Francesco Paissan 0013:000127': 19,
     'Ibrahim Ouahbi 0015:000178': 12,
     'Ismail Lamaakal 0014:000176': 16,
     'Ivanovitch Silva 0027:000442': 2,
     'Khalid El Makkaoui 0016:000178': 7,
     'Luca Benini 0041:000706': 0,
     'Manuel Roveri 0016:000160': 8,
     'Marco Zennaro 0018:000115': 5,
     'Marianne Silva 0020:000255': 4,
     'Michele Magno 0035:000501': 1,
     'Rajesh Gupta 0014:000003': 18,
     'Sebastian Bader 0015:000207': 10,
     'Sudeep Tanwar 0014:000003': 17,
     'Yassine Maleh 0015:000178': 11,
     'Yuxuan Zhang 0014:000220': 15}

    >>> # ---------------------------------------------------------------------
    >>> # LOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     UnitToCluster()
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Alessio Burrello 0015:000114': 1,
     'Daniel G. Costa 0016:000312': 2,
     'Danilo Pau 0021:000125': 6,
     'Danilo Pietro Pau 0016:000064': 9,
     'Elisabetta Farella 0015:000129': 4,
     'Francesco Paissan 0013:000127': 4,
     'Ibrahim Ouahbi 0015:000178': 0,
     'Ismail Lamaakal 0014:000176': 0,
     'Ivanovitch Silva 0027:000442': 2,
     'Khalid El Makkaoui 0016:000178': 0,
     'Luca Benini 0041:000706': 1,
     'Manuel Roveri 0016:000160': 8,
     'Marco Zennaro 0018:000115': 7,
     'Marianne Silva 0020:000255': 2,
     'Michele Magno 0035:000501': 1,
     'Rajesh Gupta 0014:000003': 5,
     'Sebastian Bader 0015:000207': 3,
     'Sudeep Tanwar 0014:000003': 5,
     'Yassine Maleh 0015:000178': 0,
     'Yuxuan Zhang 0014:000220': 3}


"""

from tm2p._intern.netw.unit_to_clust import BaseUnitToCluster

from .direct_matrix import DirectMatrix


class UnitToCluster(
    BaseUnitToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return DirectMatrix()
