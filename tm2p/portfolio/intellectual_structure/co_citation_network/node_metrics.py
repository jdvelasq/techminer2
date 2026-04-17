"""
NodeMetrics
===============================================================================

* **CITED_AUTH**

* **CITED_REF**

* **CITED_SRC**


Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CoCitationUnit
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_AUTH)
    ...     #
    ...     .having_top_n_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC              DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Alam T.M. 1:0                   0.089                     0.0                 0.481     0.002                   0.039         1.0           89    68.409
    Almuhammadi A. 1:0              0.089                     0.0                 0.481     0.002                   0.039         1.0           89    68.409
    Ampomah EK 1:0                  0.089                     0.0                 0.481     0.002                   0.039         1.0           89    68.409
    Birch D.G.W. 1:0                0.089                     0.0                 0.481     0.002                   0.039         1.0           89    68.409
    Ceaparu C. 1:0                  0.089                     0.0                 0.481     0.002                   0.039         1.0           89    68.409

"""

from tm2p._intern.networks import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
