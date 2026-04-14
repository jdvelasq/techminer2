"""
ItemToCluster
===============================================================================

* **CouplingUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CouplingUnit, GraphClusteringAlgorithm, ItemOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(1, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Al Hudithi F 2021 1:00005': 3,
     'Al Mamun MA 2025 1:00003': 1,
     'Anagnostopoulos I 2018 1:00284': 0,
     'Arner DW 2017 1:00242': 0,
     'Arner DW 2019 1:00045': 0,
     'Arner DW 2020 1:00338': 0,
     'Arsyad I 2025 1:00005': 1,
    ...

* **CouplingUnit.AUTH**

Smoke tests:
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     #
    ...     .having_items_in_top(100)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Andrea Miglionico 002:00011': 1,
     'Ioannis Anagnostopoulos 002:00284': 0,
     'Johan von Solms 002:00029': 0,
     'Joseph Jye-Cherng Lyu 002:00003': 3,
     'Joseph Lee 001:00042': 1,
     'Lawrence G. Baxter 001:00030': 0,
     'Nir Kshetri 002:00006': 0,
    ...

* **CouplingUnit.CTRY**

Smoke tests:
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     #
    ...     # NETWORK:
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
    {'AUS 024:01072': 0,
     'CAN 008:00054': 0,
     'CHN 046:01426': 0,
     'DEU 014:00785': 0,
     'FRA 009:00232': 0,
     'GBR 026:01562': 0,
     'IND 009:00128': 0,
     'ITA 012:00116': 0,
     'USA 021:00494': 0}


* **CouplingUnit.ORG**

Smoke tests:
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.ORG)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'JIANGSU NORM UNIV 004:00008': 0,
     'MONASH UNIV 003:00006': 0,
     'R RD UNIV 003:00024': 1,
     'UNIV MACAU 003:00019': 0}

* **CouplingUnit.SRC**

Smoke tests:
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.SRC)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
    {'EUR BUS ORGAN LAW REV 005:00506': 0,
     'EUR J RISK REGUL 002:00038': 0,
     'FINANC RES LETT 003:00002': 1,
     'INT REV FINANC ANAL 002:00030': 1,
     'J BANK REGUL 005:00094': 0,
     'J ECON BUS 002:00284': 0,
     'J FINANC REGUL 004:00298': 0,
     'J FINANC REGUL COMPLIANCE 005:00014': 1,
     'J MONEY LAUND CONTROL 003:00040': 1,
     'J TECHNOL 004:00110': 1}


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
