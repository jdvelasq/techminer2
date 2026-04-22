"""
NodeMetrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.latent_similarity_network import NodeMetrics
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                             DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    fintech 119:26148                                1.0                     0.0                   1.0     0.064                   0.224         1.0           19    12.643
    innovation 020:03916                             1.0                     0.0                   1.0     0.060                   0.224         1.0           19    11.813
    finance 029:07137                                1.0                     0.0                   1.0     0.059                   0.224         1.0           19    11.607
    china 018:03596                                  1.0                     0.0                   1.0     0.056                   0.224         1.0           19    10.866
    sustainable development 015:02158                1.0                     0.0                   1.0     0.054                   0.224         1.0           19    10.448


"""

from tm2p._intern.networks import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
