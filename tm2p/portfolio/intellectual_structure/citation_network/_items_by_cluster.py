"""
ItemsByCluster
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.citation_network import ItemsByCluster
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
                                    0  ...                        7
    0  Anagnostopoulos I 2018 1:00284  ...    Kraus NM 2020 1:00004
    1              Lui A 2018 1:00096  ...  Manzhura O 2022 1:00003
    2             Das SR 2019 1:00090  ...
    3           Takeda A 2021 1:00066  ...
    4          Currie WL 2018 1:00043  ...
    <BLANKLINE>
    [5 rows x 8 columns]

* **CitationUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
                                 0  ...                             2
    0   Dirk A. Zetzsche 008:00699  ...         Nir Kshetri 002:00006
    1    Ross P. Buckley 007:00887  ...        Jamal Wiwoho 002:00005
    2   Douglas W. Arner 007:00887  ...         Ifan Arsyad 002:00005
    3     Michael Becker 002:00017  ...  Dona Budi Kharisma 002:00005
    4  Zakariya Mustapha 002:00016  ...
    <BLANKLINE>
    [5 rows x 3 columns]


* **CitationUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
                   0              1              2
    0  CHN 046:01426  DEU 014:00785  IND 009:00128
    1  GBR 026:01562  LUX 009:00703  IDN 004:00019
    2  AUS 024:01072  FRA 009:00232  PAK 003:00152
    3  USA 021:00494  JPN 004:00184  BHR 002:00019
    4  ITA 012:00116  NLD 003:00066


* **CitationUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
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
                                 0  ...                           3
    0         UNIV MACAU 003:00019  ...      UNIV N CAROL 002:00006
    1        MONASH UNIV 003:00006  ...  UNIV SEBEL MARET 002:00005
    2          HARV UNIV 002:00046  ...
    3        UNIV TASMAN 002:00019  ...
    4  FOM UNIV APPL SCI 002:00017  ...
    <BLANKLINE>
    [5 rows x 4 columns]



* **CitationUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_citation_unit(CitationUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
                               0  ...                    3
    0      EUR BUS ORGAN LAW REV  ...  INT REV FINANC ANAL
    1  J FINANC REGUL COMPLIANCE  ...   RES INT BUS FINANC
    2             J FINANC REGUL  ...      INT J INNOV SCI
    3        LAW FINANC MARK REV  ...
    4               J GLOB MANAG  ...
    <BLANKLINE>
    [5 rows x 4 columns]


"""

from tm2p._intern.networks.items_by_cluster import BaseItemsByCluster

from ._cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):
        return ClusterToItems()
