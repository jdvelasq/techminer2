"""
ItemsByCluster
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.cit_netw import ItemsByCluster  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                              0   ...                                                 39
    ITEM                                                     ...
    0        Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300  ...  Campuzano-Bolarín F, 2025, CENT EUR J OPER RES...
    1              Liu JK, 2020, ENV SCI POLLUT RES 1:00207  ...       Martin-Méndez A, 2026, J NAT CONSERV 1:00000
    2                    Ding ZK, 2016, WASTE MANAG 1:00201  ...
    3                   Ding ZK, 2018, J CLEAN PROD 1:00178  ...
    4                 Wang JY/1, 2015, J CLEAN PROD 1:00143  ...
    <BLANKLINE>
    [5 rows x 40 columns]


* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_units_in(None)
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                           0  ...                       4
    ITEM                                 ...
    0        Vivian W. Y. Tam 004:00532  ...     Lihong Li 003:00019
    1         Mohamed Marzouk 003:00323  ...  Chunbing Guo 003:00009
    2           Jingkuang Liu 003:00284  ...
    <BLANKLINE>
    [3 rows x 5 columns]


"""

from tm2p._intern.netw.unit_by_clust import BaseUnitByCluster

from .clust_to_items import ClusterToItems


class ItemsByCluster(
    BaseUnitByCluster,
):
    """:meta private:"""

    def cluster_to_units(self):
        return ClusterToItems()
