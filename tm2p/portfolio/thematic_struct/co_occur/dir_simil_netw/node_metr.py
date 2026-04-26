"""
NodeMetrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.direct_similarity_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.KW)
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
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                             DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    sustainability 013:02308                       0.842                   0.029                 0.864     0.070                   0.268       0.700            9     0.236
    sustainable development 015:02158              0.789                   0.025                 0.826     0.068                   0.253       0.714            9     0.230
    innovation 020:03916                           0.947                   0.053                 0.950     0.065                   0.288       0.627            9     0.216
    finance 029:07137                              1.000                   0.057                 1.000     0.065                   0.303       0.632            9     0.211
    economic growth 009:01654                      0.526                   0.005                 0.679     0.059                   0.183       0.822            9     0.196

"""

from tm2p._intern.netw import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
