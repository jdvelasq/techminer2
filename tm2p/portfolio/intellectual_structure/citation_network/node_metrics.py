"""
NodeMetrics
===============================================================================

* **CitationUnit.DOC**

* **CitationUnit.AUTH**

* **CitationUnit.CTRY**

* **CitationUnit.ORG**

* **CitationUnit.SRC**


Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import NodeMetrics
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
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
    >>> pprint(df.head().round(3))  # doctest: +NORMALIZE_WHITESPACE
    METRIC                          DEGREE_CENTRALITY  ...  STRENGTH
    NODE                                               ...
    El Khoury R 2025 1:00004                    0.343  ...      37.0
    Anagnostopoulos I 2018 1:00284              0.287  ...      31.0
    Grassi L 2022 1:00024                       0.287  ...      31.0
    Bagherifam N 2025 1:00000                   0.269  ...      29.0
    Becker M 2020 1:00012                       0.139  ...      15.0
    <BLANKLINE>
    [5 rows x 8 columns]




"""

from tm2p._intern.networks.node_metrics import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(params=self.params)
