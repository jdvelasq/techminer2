"""
ItemsToCluster
===============================================================================

Smoke test:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.latent_simil_netw import ItemToCluster
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
    >>> from pprint import pprint
    >>> pprint(mapping)
    {'artificial intelligence 008:01915': 1,
     'banking 013:03043': 0,
     'blockchain 012:03450': 1,
     'china 018:03596': 0,
     'commerce 006:02013': 1,
     'covid-19 009:01743': 0,
    ...


"""

from tm2p._intern.netw.item_to_clust import BaseItemToCluster

from .latent_matrix import LatentMatrix


class ItemToCluster(
    BaseItemToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return LatentMatrix()
