"""
UnitToCluster
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.latent import UnitToCluster  # type: ignore
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
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Alessio Burrello 0015:000114': 0,
     'Daniel G. Costa 0016:000312': 2,
     'Danilo Pau 0021:000125': 3,
     'Danilo Pietro Pau 0016:000064': 6,
     'Elisabetta Farella 0015:000129': 0,
     'Francesco Paissan 0013:000127': 0,
     'Ibrahim Ouahbi 0015:000178': 1,
     'Ismail Lamaakal 0014:000176': 1,
     'Ivanovitch Silva 0027:000442': 2,
     'Khalid El Makkaoui 0016:000178': 1,
     'Luca Benini 0041:000706': 0,
     'Manuel Roveri 0016:000160': 5,
     'Marco Zennaro 0018:000115': 4,
     'Marianne Silva 0020:000255': 2,
     'Michele Magno 0035:000501': 0,
     'Rajesh Gupta 0014:000003': 8,
     'Sebastian Bader 0015:000207': 0,
     'Sudeep Tanwar 0014:000003': 7,
     'Yassine Maleh 0015:000178': 1,
     'Yuxuan Zhang 0014:000220': 0}



"""

from tm2p._intern.netw.unit_to_clust import BaseUnitToCluster

from .latent_matrix import LatentMatrix


class UnitToCluster(
    BaseUnitToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return LatentMatrix()
