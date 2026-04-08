"""
ItemToCluster
===============================================================================

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AgglomerativeClustering
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  # linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  # always True
    ...     compute_distances=True,  # always True
    ... )
    >>> from tm2p.enum import Field, GraphClusteringAlgorithm, AssociationIndex, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 1,
     'banking 010:02599': 2,
     'banks 005:00769': 3,
     'blockchain 011:02023': 1,
     'china 009:01947': 4,
     'covid-19 006:01224': 3,
     'crowdfunding 007:01245': 1,
     'digital finance 005:02052': 1,
     'economic growth 005:00660': 0,
     'financial inclusion 017:03823': 5,
     'financial literacy 005:00665': 0,
     'financial services 007:01673': 2,
     'financial technology 015:02734': 0,
     'fintech 117:25478': 5,
     'green finance 011:02844': 3,
     'innovation 009:01703': 2,
     'regtech 006:01481': 4,
     'sustainability 006:01357': 4,
     'sustainable development 005:00604': 0,
     'technology 007:01409': 2}


    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence': 1,
     'banking': 2,
     'banks': 3,
     'blockchain': 1,
     'china': 4,
     'covid-19': 3,
     'crowdfunding': 1,
     'digital finance': 1,
     'economic growth': 0,
     'financial inclusion': 5,
     'financial literacy': 0,
     'financial services': 2,
     'financial technology': 0,
     'fintech': 5,
     'green finance': 3,
     'innovation': 2,
     'regtech': 4,
     'sustainability': 4,
     'sustainable development': 0,
     'technology': 2}


    >>> # ---------------------------------------------------------------------
    >>> # DBSCAN
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import DBSCAN
    >>> estimator = DBSCAN(
    ...     eps=0.1,  # eps ∈ [0.1, 0.4] (tune empirically)
    ...     min_samples=3,  # min_samples ∈ [3, 10]
    ...     metric="precomputed",
    ... )
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)
    {'artificial intelligence 008:01915': 0,
     'banking 010:02599': 0,
     'banks 005:00769': 0,
     'blockchain 011:02023': 0,
     'china 009:01947': 0,
     'covid-19 006:01224': 0,
     'crowdfunding 007:01245': 0,
     'digital finance 005:02052': 0,
     'economic growth 005:00660': 0,
     'financial inclusion 017:03823': 0,
     'financial literacy 005:00665': 0,
     'financial services 007:01673': 0,
     'financial technology 015:02734': 0,
     'fintech 117:25478': 0,
     'green finance 011:02844': 0,
     'innovation 009:01703': 0,
     'regtech 006:01481': 0,
     'sustainability 006:01357': 0,
     'sustainable development 005:00604': 0,
     'technology 007:01409': 0}


    >>> # ---------------------------------------------------------------------
    >>> # SpectralClustering
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import SpectralClustering
    >>> estimator = SpectralClustering(
    ...     n_clusters=6,
    ...     affinity="precomputed",
    ...     assign_labels="kmeans",  # assign_labels ∈ {"kmeans", "discretize"}
    ...     random_state=0,
    ...     n_init=10,  # Used only when assign_labels="kmeans"
    ...     eigen_solver = "arpack",  # eigen_solver ∈ {"arpack", "lobpcg", "amg"}
    ...     n_components=None,  # Used only when eigen_solver="arpack"
    ... )
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 4,
     'banking 010:02599': 0,
     'banks 005:00769': 2,
     'blockchain 011:02023': 0,
     'china 009:01947': 1,
     'covid-19 006:01224': 2,
     'crowdfunding 007:01245': 5,
     'digital finance 005:02052': 4,
     'economic growth 005:00660': 3,
     'financial inclusion 017:03823': 0,
     'financial literacy 005:00665': 3,
     'financial services 007:01673': 0,
     'financial technology 015:02734': 1,
     'fintech 117:25478': 0,
     'green finance 011:02844': 2,
     'innovation 009:01703': 0,
     'regtech 006:01481': 1,
     'sustainability 006:01357': 5,
     'sustainable development 005:00604': 3,
     'technology 007:01409': 0}



    >>> # ---------------------------------------------------------------------
    >>> # AffinityPropagation
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import AffinityPropagation
    >>> estimator = AffinityPropagation(
    ...     affinity="precomputed",
    ...     damping=0.5,  # damping ∈ [0.5, 1.0)
    ...     max_iter=200,  # or higher
    ...     convergence_iter=15,
    ...     preference=3,  # approx the number of clusters (tune empirically)
    ...     random_state=0,
    ... )
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 8,
     'banking 010:02599': 5,
     'banks 005:00769': 16,
     'blockchain 011:02023': 4,
     'china 009:01947': 6,
     'covid-19 006:01224': 14,
     'crowdfunding 007:01245': 11,
     'digital finance 005:02052': 15,
     'economic growth 005:00660': 18,
     'financial inclusion 017:03823': 1,
     'financial literacy 005:00665': 17,
     'financial services 007:01673': 9,
     'financial technology 015:02734': 2,
     'fintech 117:25478': 0,
     'green finance 011:02844': 3,
     'innovation 009:01703': 7,
     'regtech 006:01481': 12,
     'sustainability 006:01357': 13,
     'sustainable development 005:00604': 19,
     'technology 007:01409': 10}



    >>> # ---------------------------------------------------------------------
    >>> # LOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> from sklearn.cluster import AffinityPropagation
    >>> estimator = AffinityPropagation(
    ...     affinity="precomputed",
    ...     damping=0.5,  # damping ∈ [0.5, 1.0)
    ...     max_iter=200,  # or higher
    ...     convergence_iter=15,
    ...     preference=3,  # approx the number of clusters (tune empirically)
    ...     random_state=0,
    ... )
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 008:01915': 2,
     'banking 010:02599': 3,
     'banks 005:00769': 3,
     'blockchain 011:02023': 2,
     'china 009:01947': 0,
     'covid-19 006:01224': 2,
     'crowdfunding 007:01245': 2,
     'digital finance 005:02052': 2,
     'economic growth 005:00660': 1,
     'financial inclusion 017:03823': 0,
     'financial literacy 005:00665': 1,
     'financial services 007:01673': 3,
     'financial technology 015:02734': 1,
     'fintech 117:25478': 0,
     'green finance 011:02844': 1,
     'innovation 009:01703': 3,
     'regtech 006:01481': 0,
     'sustainability 006:01357': 0,
     'sustainable development 005:00604': 1,
     'technology 007:01409': 3}


"""

from tm2p._intern import ParamsMixin

from ._intern.get_item_to_cluster import get_item_to_cluster


class ItemToCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        i2c = get_item_to_cluster(params=self.params)

        return i2c
