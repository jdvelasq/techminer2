"""
ItemsByCluster
===============================================================================


Smoke tests:
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  #       linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  #  always
    ...     compute_distances=True,  #  always True
    ... )
    >>> from tm2p.enum import AnalysisUnit, Field, AssociationIndex, UnitOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(estimator)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                              0                            1                       2                              3                              4                        5
    ITEM
    0         Julapa A. Jagtiani 005:01156   Douglas W. Arner 003:00911  Chichuan Lee 002:00717          Huaping Sun 002:00656          Lars Hornuf 003:00904  Guangyou Zhou 002:00670
    1            Gerhard Schwabe 003:00330  Janos N. Barberis 003:00445  Chinhsien Yu 002:00717           Linnan Yan 002:00656  Armin Schwienbacher 002:00611      Sumei Luo 002:00670
    2        Liudmila Zavolokina 003:00330    Ross P. Buckley 002:00898  Jinsong Zhao 002:00717  Tadiwanashe Muganyi 002:00656
    3             Mateusz Dolata 003:00330
    4               Peter Gomber 002:02579


"""

from tm2p._intern.netw.item_by_clust import BaseItemsByCluster

from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    BaseItemsByCluster,
):
    """:meta private:"""

    def cluster_to_items(self):
        return ClusterToItems()
