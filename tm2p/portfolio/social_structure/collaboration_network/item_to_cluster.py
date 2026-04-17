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
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
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
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Armin Schwienbacher 002:00611': 4,
     'Chichuan Lee 002:00717': 2,
     'Chinhsien Yu 002:00717': 2,
     'Douglas W. Arner 003:00911': 1,
     'Gerhard Schwabe 003:00330': 0,
     'Guangyou Zhou 002:00670': 5,
     'Huaping Sun 002:00656': 3,
     'Janos N. Barberis 003:00445': 1,
     'Jinsong Zhao 002:00717': 2,
     'Julapa A. Jagtiani 005:01156': 0,
     'Lars Hornuf 003:00904': 4,
     'Linnan Yan 002:00656': 3,
     'Liudmila Zavolokina 003:00330': 0,
     'Mateusz Dolata 003:00330': 0,
     'Peter Gomber 002:02579': 0,
     'Robert J. Kauffman 002:01445': 0,
     'Ross P. Buckley 002:00898': 1,
     'Sumei Luo 002:00670': 5,
     'Tadiwanashe Muganyi 002:00656': 3,
     'Victor Murinde 002:01022': 0}


    >>> mapping = (
    ...     ItemToCluster()
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
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Armin Schwienbacher': 4,
     'Chichuan Lee': 2,
     'Chinhsien Yu': 2,
     'Douglas W. Arner': 1,
     'Gerhard Schwabe': 0,
     'Guangyou Zhou': 5,
     'Huaping Sun': 3,
     'Janos N. Barberis': 1,
     'Jinsong Zhao': 2,
     'Julapa A. Jagtiani': 0,
     'Lars Hornuf': 4,
     'Linnan Yan': 3,
     'Liudmila Zavolokina': 0,
     'Mateusz Dolata': 0,
     'Peter Gomber': 0,
     'Robert J. Kauffman': 0,
     'Ross P. Buckley': 1,
     'Sumei Luo': 5,
     'Tadiwanashe Muganyi': 3,
     'Victor Murinde': 0}


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
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
    >>> pprint(mapping)
    {'Armin Schwienbacher 002:00611': 0,
     'Chichuan Lee 002:00717': 2,
     'Chinhsien Yu 002:00717': 2,
     'Douglas W. Arner 003:00911': 0,
     'Gerhard Schwabe 003:00330': 1,
     'Guangyou Zhou 002:00670': 0,
     'Huaping Sun 002:00656': 3,
     'Janos N. Barberis 003:00445': 0,
     'Jinsong Zhao 002:00717': 2,
     'Julapa A. Jagtiani 005:01156': 0,
     'Lars Hornuf 003:00904': 0,
     'Linnan Yan 002:00656': 3,
     'Liudmila Zavolokina 003:00330': 1,
     'Mateusz Dolata 003:00330': 1,
     'Peter Gomber 002:02579': 0,
     'Robert J. Kauffman 002:01445': 0,
     'Ross P. Buckley 002:00898': 0,
     'Sumei Luo 002:00670': 0,
     'Tadiwanashe Muganyi 002:00656': 3,
     'Victor Murinde 002:01022': 0}


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
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Armin Schwienbacher 002:00611': 3,
     'Chichuan Lee 002:00717': 0,
     'Chinhsien Yu 002:00717': 0,
     'Douglas W. Arner 003:00911': 0,
     'Gerhard Schwabe 003:00330': 1,
     'Guangyou Zhou 002:00670': 5,
     'Huaping Sun 002:00656': 2,
     'Janos N. Barberis 003:00445': 0,
     'Jinsong Zhao 002:00717': 0,
     'Julapa A. Jagtiani 005:01156': 0,
     'Lars Hornuf 003:00904': 3,
     'Linnan Yan 002:00656': 2,
     'Liudmila Zavolokina 003:00330': 1,
     'Mateusz Dolata 003:00330': 1,
     'Peter Gomber 002:02579': 4,
     'Robert J. Kauffman 002:01445': 4,
     'Ross P. Buckley 002:00898': 0,
     'Sumei Luo 002:00670': 5,
     'Tadiwanashe Muganyi 002:00656': 2,
     'Victor Murinde 002:01022': 0}


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
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Armin Schwienbacher 002:00611': 19,
     'Chichuan Lee 002:00717': 13,
     'Chinhsien Yu 002:00717': 12,
     'Douglas W. Arner 003:00911': 1,
     'Gerhard Schwabe 003:00330': 6,
     'Guangyou Zhou 002:00670': 15,
     'Huaping Sun 002:00656': 18,
     'Janos N. Barberis 003:00445': 3,
     'Jinsong Zhao 002:00717': 11,
     'Julapa A. Jagtiani 005:01156': 0,
     'Lars Hornuf 003:00904': 2,
     'Linnan Yan 002:00656': 17,
     'Liudmila Zavolokina 003:00330': 5,
     'Mateusz Dolata 003:00330': 4,
     'Peter Gomber 002:02579': 7,
     'Robert J. Kauffman 002:01445': 8,
     'Ross P. Buckley 002:00898': 10,
     'Sumei Luo 002:00670': 14,
     'Tadiwanashe Muganyi 002:00656': 16,
     'Victor Murinde 002:01022': 9}

    >>> # ---------------------------------------------------------------------
    >>> # LOUVAIN
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Armin Schwienbacher 002:00611': 4,
     'Chichuan Lee 002:00717': 2,
     'Chinhsien Yu 002:00717': 2,
     'Douglas W. Arner 003:00911': 0,
     'Gerhard Schwabe 003:00330': 1,
     'Guangyou Zhou 002:00670': 6,
     'Huaping Sun 002:00656': 3,
     'Janos N. Barberis 003:00445': 0,
     'Jinsong Zhao 002:00717': 2,
     'Julapa A. Jagtiani 005:01156': 7,
     'Lars Hornuf 003:00904': 4,
     'Linnan Yan 002:00656': 3,
     'Liudmila Zavolokina 003:00330': 1,
     'Mateusz Dolata 003:00330': 1,
     'Peter Gomber 002:02579': 5,
     'Robert J. Kauffman 002:01445': 5,
     'Ross P. Buckley 002:00898': 0,
     'Sumei Luo 002:00670': 6,
     'Tadiwanashe Muganyi 002:00656': 3,
     'Victor Murinde 002:01022': 8}

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
