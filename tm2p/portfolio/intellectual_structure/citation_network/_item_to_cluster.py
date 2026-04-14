"""
ItemToCluster
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.intellectual_structure.citation_network import ItemToCluster
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
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
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Al Mamun MA 2025 1:00003': 2,
     'Anagnostopoulos I 2018 1:00284': 0,
     'Anagnostopoulos I 2022 1:00000': 0,
     'Arner DW 2019 1:00045': 4,
     'Arner DW 2020 1:00338': 4,
     'Arsyad I 2025 1:00005': 5,
    ...

* **CitationUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     #
    ...     .having_items_in_top(50)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(1)
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
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Aishath Muneeza 002:00016': 0,
     'Ananda Maiti 002:00019': 3,
     'Andrea Miglionico 002:00011': 0,
     "Auwal Adam Sa'ad 002:00016": 0,
    ...


* **CitationUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     #
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
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'AUS 024:01072': 0,
     'BEL 003:00013': 0,
     'BHR 002:00019': 2,
     'CAN 008:00054': 0,
     'CHE 004:00086': 0,
     'CHN 046:01426': 0,
    ...

* **CitationUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
    ...     #
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
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'FOM UNIV APPL SCI 002:00017': 0,
     'GOETHE UNIV FRANKF 002:00027': 2,
     'HARV UNIV 002:00046': 0,
     'HEINRICH HEINE UNIV 004:00642': 1,
     'JIANGSU NORM UNIV 004:00008': 2,
     'LEBAN AMER UNIV 002:00116': 1,
    ...


* **CitationUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_citation_unit(CitationUnit.SRC)
    ...     #
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
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'COMPUT': 1,
     'EUR BUS ORGAN LAW REV': 0,
     'FUTUR INTERNET': 1,
     'INT J INNOV SCI': 3,
     'INT J LAW MANAG': 1,
     'INT REV FINANC ANAL': 3,
     'J BANK REGUL': 1,
    ...

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.assign_cluter_numbers_by_cluster_size import (
    assign_cluster_numbers_by_cluster_size,
)
from tm2p._intern.networks import normalize_matrix
from tm2p._intern.plots.nx import (
    create_nx_graph_from_matrix,
    detect_communities,
    nodes_to_clusters,
)

from .matrix import Matrix


def _create_nx_graph(params):
    matrix = Matrix().update(**params.__dict__).using_counters(True).run()
    matrix = normalize_matrix(
        association_index=params.association_index,
        matrix=matrix,
        params=params,
    )
    nx_graph = create_nx_graph_from_matrix(matrix)
    return nx_graph


class ItemToCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        use_counters = self.params.counters
        nx_graph = _create_nx_graph(params=self.params)
        nx_graph = detect_communities(self.params, nx_graph)
        i2c = nodes_to_clusters(nx_graph)

        c2i = assign_cluster_numbers_by_cluster_size(
            items=list(i2c.keys()),
            clusters=list(i2c.values()),
        )
        i2c = {item: cluster for cluster, items in c2i.items() for item in items}

        i2c = {item: cluster for cluster, items in c2i.items() for item in items}

        if use_counters is False:

            i2c = {
                " ".join(item.split(" ")[:-1]): cluster for item, cluster in i2c.items()
            }

        return i2c
