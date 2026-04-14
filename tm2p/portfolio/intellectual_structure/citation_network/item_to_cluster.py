"""
ItemToCluster
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.citation_network import ItemToCluster
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Al Mamun MA 2025 1:00003': 2,
     'Anagnostopoulos I 2018 1:00284': 0,
     'Anagnostopoulos I 2022 1:00000': 0,
     'Arner DW 2019 1:00045': 4,
     'Arner DW 2020 1:00338': 4,
     'Arsyad I 2025 1:00005': 5,
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
