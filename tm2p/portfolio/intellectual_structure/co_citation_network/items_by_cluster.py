"""
ItemsByCluster
===============================================================================

* **CITED_AUTH**

    >>> from tm2p.enum import AssociationIndex, CoCitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_AUTH)
    ...     #
    ...     .having_items_in_top(30)
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
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                            0  ...               8
    ITEM                                  ...
    0                        Kurum E 9:0  ...     Kumar S 4:0
    1                         Yang D 8:0  ...    Hair JF. 3:0
    2                        Turki M 8:0  ...   KAISER HF 2:0
    3        PACKIN Nizan Geslevich. 8:0  ...  Dwivedi YK 2:0
    4                     Micheler E 8:0  ...    Jahre M. 1:0
    <BLANKLINE>
    [5 rows x 9 columns]


* **CITED_REF**

    >>> from tm2p.enum import AssociationIndex, CoCitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     #
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_items_in(None)
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
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                                 0   ...                                                 10
    ITEM                                                        ...
    0                   Williams JW, 2013, ACCOUNT ORG SOC 9:0  ...            The Open Group, 2016, ARCH 3 0 SPEC 1:0
    1            Kurum E, 2023, Journal of Financial Crime 9:0  ...  ITU (International Telecommunication Union), 2...
    2                  Becker M, 2020, INTELL SYST ACCOUNT 9:0  ...           Fredriksen R., 2002, Computer Safety 1:0
    3                               Turki M, 2020, HELIYON 8:0  ...            Faulkner L, 2014, TRANSPORT RES REC 1:0
    4        PACKIN Nizan Geslevich., 2018, Chicago-Kent La...  ...  Bundesamt fur Sicherheit in der Informationste...
    <BLANKLINE>
    [5 rows x 11 columns]



* **CITED_SRC**

    >>> from tm2p.enum import AssociationIndex, CoCitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_SRC)
    ...     #
    ...     .having_items_in_top(50)
    ...     .having_minimum_citation_count(0)
    ...     .having_items_in(None)
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
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                       0   ...                                                 11
    ITEM                              ...
    0          TELECOMMUN POLICY 9:0  ...                            DEV REGTECH SUPTECH 5:0
    1                   Q J ECON 9:0  ...                                 Banque & Droit 1:0
    2         PAC-BASIN FINANC J 9:0  ...                                           BRDA 1:0
    3        J INT FINANC MARK I 9:0  ...                                       BJBMarch 1:0
    4        J FINANC QUANT ANAL 9:0  ...  Artificial Intelligence: challenges for the fi...
    <BLANKLINE>
    [5 rows x 12 columns]




"""

from tm2p._intern.networks.items_by_cluster import BaseItemsByCluster

from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):

        return ClusterToItems()
