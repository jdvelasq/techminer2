"""
NodeMetrics
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw import NodeMetrics  # type: ignore
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC               DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Wang JY 14:0                     0.552                   0.004                 0.690     0.048                   0.143       0.842           14     0.174
    Yuan HP 26:0                     0.690                   0.010                 0.763     0.047                   0.176       0.768           15     0.170
    Lu WS 13:0                       0.483                   0.002                 0.659     0.045                   0.127       0.890           13     0.163
    Ding ZK 18:0                     0.793                   0.016                 0.829     0.045                   0.199       0.715           15     0.161
    Qudrat-Ullah H 16:0              0.690                   0.007                 0.763     0.040                   0.180       0.805           15     0.141


"""

from tm2p._intern.netw import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
