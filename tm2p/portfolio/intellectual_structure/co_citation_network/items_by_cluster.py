"""
ItemsByCluster
===============================================================================

* **CITED_AUTH**

    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_AUTH)
    ...     #
    ...     .having_top_n_cited_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    CLUSTER                 0                       1                  2
    ITEM
    0          Magnuson W 9:0             Kurum E 9:0    Williams JW 9:0
    1           Brummer C 9:0              Yang D 8:0      Butler T 25:0
    2               Lee I 8:0  Anagnostopoulos I 31:0  Bamberger KA 13:0
    3           Arner DW 61:0       Kavassalis P 14:0     Currie WL 12:0
    4        Zetzsche DA 21:0           Grassi L 12:0      Gozman D 10:0


* **CITED_REF**

    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_units_in(None)
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
    CLUSTER                                                  0  ...                                                  2
    ITEM                                                        ...
    0            Kurum E, 2023, Journal of Financial Crime 9:0  ...             Williams JW, 2013, ACCOUNT ORG SOC 9:0
    1                  Becker M, 2020, INTELL SYST ACCOUNT 9:0  ...  PACKIN Nizan Geslevich., 2018, Chicago-Kent La...
    2                   Yang D, 2018, EMERG MARK FINANC TR 8:0  ...  Butler T, 2017, Journal of financial transform...
    3                               Turki M, 2020, HELIYON 8:0  ...          Butler T, 2019, PALGR ST DIG BUS ENA 21:0
    4        Johansson E., 2019, ACRN Journal of Finance an...  ...             Currie WL, 2018, J INF TECHNOL-UK 12:0
    <BLANKLINE>
    [5 rows x 3 columns]


* **CITED_SRC**

    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_SRC)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_units_in(None)
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
    CLUSTER                             0  ...                          3
    ITEM                                   ...
    0        SSRN Electronic Journal 52:0  ...           IEEE ACCESS 22:0
    1               NW J INT LAW BUS 52:0  ...    DECIS SUPPORT SYST 22:0
    2                     J ECON BUS 37:0  ...      EXPERT SYST APPL 16:0
    3                   J BANK REGUL 29:0  ...                 Arxiv 16:0
    4           EUR BUS ORGAN LAW RE 26:0  ...  LECT NOTES COMPUT SC 15:0
    <BLANKLINE>
    [5 rows x 4 columns]



"""

from tm2p._intern.networks.items_by_cluster import BaseItemsByCluster

from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):

        return ClusterToItems()
