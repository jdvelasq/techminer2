"""
UnitsByCluster
===============================================================================


Smoke tests:
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  #       linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  #  always
    ...     compute_distances=True,  #  always True
    ... )
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.direct import UnitsByCluster  # type: ignore
    >>> df = (
    ...     UnitsByCluster()
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
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                               0                             1                               2                          3                          4                              5
    UNIT                                                                                                                                                                                      
    0               Luca Benini 0041:000706  Ivanovitch Silva 0027:000442  Khalid El Makkaoui 0016:000178   Rajesh Gupta 0014:000003  Manuel Roveri 0016:000160  Danilo Pietro Pau 0016:000064
    1             Michele Magno 0035:000501        Danilo Pau 0021:000125      Ibrahim Ouahbi 0015:000178  Sudeep Tanwar 0014:000003                                                          
    2           Sebastian Bader 0015:000207    Marianne Silva 0020:000255       Yassine Maleh 0015:000178                                                                                     
    3        Elisabetta Farella 0015:000129     Marco Zennaro 0018:000115     Ismail Lamaakal 0014:000176                                                                                     
    4          Alessio Burrello 0015:000114   Daniel G. Costa 0016:000312                                                                                                                     


"""

from tm2p._intern.netw.unit_by_clust import BaseUnitByCluster

from .cluster_to_units import ClusterToUnits


class UnitsByCluster(
    BaseUnitByCluster,
):
    """:meta private:"""

    def cluster_to_units(self):
        return ClusterToUnits()
