"""
NodeMetrics
===============================================================================

* **CITED_AUTH**

* **CITED_REF**

* **CITED_SRC**


Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
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
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC            DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Kurum E 9:0                   0.793                   0.002                 0.829     0.051                   0.179       0.945           19     0.645
    Yang D 8:0                    0.862                   0.008                 0.879     0.048                   0.186       0.853           19     0.587
    von Solms J 10:0              0.828                   0.002                 0.853     0.046                   0.186       0.931           19     0.567
    Currie WL 12:0                0.931                   0.009                 0.935     0.044                   0.200       0.843           19     0.528
    Becker M 12:0                 0.828                   0.003                 0.853     0.042                   0.185       0.920           19     0.509

"""

from tm2p._intern.netw import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
