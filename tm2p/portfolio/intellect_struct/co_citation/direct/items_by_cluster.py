"""
ItemsByCluster
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.direct import ItemsByCluster  # type: ignore
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
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                          0  ...                        2
    UNIT                                ...
    0                Sterman J.D. 81:0  ...  Sterman J.D. J. D. 30:0
    1        Forrester JayWright. 74:0  ...             Ahmad S 25:0
    2                FORRESTER JW 56:0  ...           Saysel AK 20:0
    3              Forrester J.W. 51:0  ...              Winz I 16:0
    4                  Sterman JD 31:0  ...        Simonovic SP 16:0
    <BLANKLINE>
    [5 rows x 3 columns]


* **CITED_REF**

    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.direct import ItemsByCluster
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
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                                  0  ...                                           3
    UNIT                                                        ...
    0        Forrester JayWright., 2013, Industrial dynamic...  ...  Sterman J.D., 2000, BUSINESS DYNAMICS 70:0
    1                 FORRESTER JW, 1958, HARVARD BUS REV 25:0  ...     Homer JB, 2006, AM J PUBLIC HEALTH 18:0
    2                Forrester Jay., 1971, World dynamics 17:0  ...     Sterman JD, 2001, CALIF MANAGE REV 14:0
    3                Forrester J.W., 1969, URBAN DYNAMICS 15:0  ...           STERMAN JD, 1989, MANAGE SCI 12:0
    4                  FORRESTER JW, 1994, SYST DYNAM REV 14:0  ...  Shepherd SP, 2014, TRANSPORTMETRICA B 10:0
    <BLANKLINE>
    [5 rows x 4 columns]



* **CITED_SRC**

    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.direct import ItemsByCluster
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
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                         0  ...                          3
    UNIT                               ...
    0            SYST DYNAM REV 137:0  ...      EXPERT SYST APPL 44:0
    1            EUR J OPER RES 104:0  ...            SAFETY SCI 32:0
    2          BUSINESS DYNAMICS 77:0  ...         BUILD ENVIRON 31:0
    3        Industrial dynamics 76:0  ...  ENG CONSTR ARCHIT MA 29:0
    4             J OPER RES SOC 56:0  ...      INT J PROJ MANAG 27:0
    <BLANKLINE>
    [5 rows x 4 columns]



"""

from tm2p._intern.netw.unit_by_clust import BaseUnitByCluster

from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseUnitByCluster,
):
    """:meta private:"""

    def cluster_to_units(self):

        return ClusterToItems()
