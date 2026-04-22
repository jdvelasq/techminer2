"""
ClusterToItems
===============================================================================

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # LOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import ClusterToItems
    >>> mapping = (
    ...     ClusterToItems()
    ...     #
    ...     # UNIT OF ANALYSIS:
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
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Douglas W. Arner 003:00911',
         'Janos N. Barberis 003:00445',
         'Ross P. Buckley 002:00898'],
     1: ['Gerhard Schwabe 003:00330',
         'Liudmila Zavolokina 003:00330',
         'Mateusz Dolata 003:00330'],
     2: ['Chichuan Lee 002:00717',
         'Chinhsien Yu 002:00717',
         'Jinsong Zhao 002:00717'],
     3: ['Huaping Sun 002:00656',
         'Linnan Yan 002:00656',
         'Tadiwanashe Muganyi 002:00656'],
     4: ['Lars Hornuf 003:00904', 'Armin Schwienbacher 002:00611'],
     5: ['Peter Gomber 002:02579', 'Robert J. Kauffman 002:01445'],
     6: ['Guangyou Zhou 002:00670', 'Sumei Luo 002:00670'],
     7: ['Julapa A. Jagtiani 005:01156'],
     8: ['Victor Murinde 002:01022']}

"""

from tm2p._intern.netw.clust_to_item import BaseClusterToItems

from .item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()
