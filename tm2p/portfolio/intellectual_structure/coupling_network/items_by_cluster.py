"""
ItemsByCluster
===============================================================================

* **CouplingUnit.AUTH**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CouplingUnit, GraphClusteringAlgorithm, ItemOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     #
    ...     .having_items_in_top(100)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(1)
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                  0  ...                                3
    ITEM                                        ...
    0        Ioannis Anagnostopoulos 002:00284  ...  Joseph Jye-Cherng Lyu 002:00003
    1                Johan von Solms 002:00029  ...
    2                    Nir Kshetri 002:00006  ...
    3             Lawrence G. Baxter 001:00030  ...
    <BLANKLINE>
    [4 rows x 4 columns]


* **CouplingUnit.CTRY**

Smoke tests:
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER    0    1    2
    ITEM
    0        GBR  CHN  PAK
    1        AUS  USA  JOR
    2        DEU  IND  THA
    3        ITA  UKR
    4        FRA  JPN


* **CouplingUnit.DOC**

Smoke tests:
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                               0  ...                       8
    ITEM                                     ...
    0                 Arner DW 2020 1:00338  ...  Scholz FB 2018 1:00000
    1        Anagnostopoulos I 2018 1:00284  ...
    2                 Arner DW 2017 1:00242  ...
    3              Zetzsche DA 2020 1:00222  ...
    4                    Lui A 2018 1:00096  ...
    <BLANKLINE>
    [5 rows x 9 columns]


* **CouplingUnit.SRC**

Smoke tests:
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                0  ...                              3
    ITEM                                      ...
    0        EUR BUS ORGAN LAW REV 005:00506  ...         J BANK REGUL 005:00094
    1               J FINANC REGUL 004:00298  ...      INT J LAW MANAG 002:00012
    2                   J ECON BUS 002:00284  ...               COMPUT 002:00006
    3             EUR J RISK REGUL 002:00038  ...  J ISLAM ACC BUS RES 002:00001
    4          LAW FINANC MARK REV 002:00009  ...
    <BLANKLINE>
    [5 rows x 4 columns]


* **CouplingUnit.ORG**

Smoke tests:
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                       0  ...                           2
    ITEM                                             ...
    0                   JIANGSU NORM UNIV 004:00008  ...  UNIV SEBEL MARET 002:00005
    1                           R RD UNIV 003:00024  ...
    2                          UNIV MACAU 003:00019  ...
    3                         MONASH UNIV 003:00006  ...
    4        SOUTHWEST UNIV FINANC & ECON 002:00031  ...
    <BLANKLINE>
    [5 rows x 3 columns]



"""

from tm2p._intern.networks.items_by_cluster import BaseItemsByCluster

from ...._intern.helpers.check_database import check_database
from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):
        check_database(self.params.root_directory)
        return ClusterToItems()
