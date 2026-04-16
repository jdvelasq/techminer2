"""
ItemToCluster
===============================================================================

* **CITED_REF**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CoCitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # CO-CITATION UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_citation_count(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Anagnostopoulos I, 2018, J ECON BUS 31:0': 0,
     'Armstrong P., 2018, DEV REGTECH SUPTECH 5:0': 1,
     'Arner DW, 2015, SSRN Electronic Journal 15:0': 1,
     'Arner DW, 2016, SSRN Electronic Journal 8:0': 1,
     'Arner DW, 2017, NW J INT LAW BUS 50:0': 1,
    ...

    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # CO-CITATION UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_citation_count(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Anagnostopoulos I, 2018, J ECON BUS': 0,
     'Armstrong P., 2018, DEV REGTECH SUPTECH': 1,
     'Arner DW, 2015, SSRN Electronic Journal': 1,
     'Arner DW, 2016, SSRN Electronic Journal': 1,
    ...
"""

from tm2p._intern.networks.item_to_cluster import BaseItemToCluster

from .direct_matrix import DirectMatrix


class ItemToCluster(
    BaseItemToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return DirectMatrix()
