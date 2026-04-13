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
    {'Al Mamun MA, 2025, SUSTAIN FUTUR, V10, DOI 10.1016/j.sftr.2025.101234 1:00003': 4,
     'Anagnostopoulos I, 2018, J ECON BUS, V100, P7, DOI 10.1016/j.jeconbus.2018.07.003 1:00284': 0,
     'Anagnostopoulos I, 2022, J ECON BUS, V118, DOI 10.1016/j.jeconbus.2020.105982 1:00000': 0,
     'Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55, DOI 10.1007/s40804-019-00135-1 1:00045': 2,
     'Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7, DOI 10.1007/s40804-020-00183-y 1:00338': 2,
     'Arsyad I, 2025, INT J LAW MANAG, DOI 10.1108/IJLMA-07-2024-0236 1:00005': 6,
     'Azzutti A, 2021, UNIV PA J INT LAW, V43, P79 1:00010': 3,
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
    ...     .having_citation_threshold(0)
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
    ...     .having_citation_threshold(0)
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
     'BHR 002:00019': 1,
     'CAN 008:00054': 0,
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
    ...     .having_citation_threshold(0)
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
    ...     .having_citation_threshold(0)
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
    ...

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import CitationUnit

from ...._intern.helpers.check_database import check_database
from ._intern.doc import DocItemToCluster
from ._intern.other import OtherItemToCluster


class ItemToCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

        if self.params.citation_unit == CitationUnit.DOC:
            item_to_cluster = DocItemToCluster
        else:
            item_to_cluster = OtherItemToCluster

        return item_to_cluster().update(**self.params.__dict__).run()
