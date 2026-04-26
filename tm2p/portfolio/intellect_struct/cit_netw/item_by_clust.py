"""
ItemsByCluster
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellect_struct.cit_netw import ItemsByCluster
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # CITATION UNIT:
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
    CLUSTER                               0  ...                        7
    ITEM                                     ...
    0        Anagnostopoulos I 2018 1:00284  ...    Kraus NM 2020 1:00004
    1                    Lui A 2018 1:00096  ...  Manzhura O 2022 1:00003
    2                   Das SR 2019 1:00090  ...
    3                 Takeda A 2021 1:00066  ...
    4                Currie WL 2018 1:00043  ...
    <BLANKLINE>
    [5 rows x 8 columns]


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
    CLUSTER                            0  ...                             2
    ITEM                                  ...
    0         Dirk A. Zetzsche 008:00699  ...         Nir Kshetri 002:00006
    1          Ross P. Buckley 007:00887  ...        Jamal Wiwoho 002:00005
    2         Douglas W. Arner 007:00887  ...         Ifan Arsyad 002:00005
    3           Michael Becker 002:00017  ...  Dona Budi Kharisma 002:00005
    4        Zakariya Mustapha 002:00016  ...
    <BLANKLINE>
    [5 rows x 3 columns]



"""

from tm2p._intern.netw.item_by_clust import BaseItemsByCluster

from .clust_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):
        return ClusterToItems()
