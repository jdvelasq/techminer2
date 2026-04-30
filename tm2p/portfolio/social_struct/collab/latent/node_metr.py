"""
NodeMetrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.latent import NodeMetrics  # type: ignore
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
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
    METRIC                          DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE                                                                                                                                                                
    Ibrahim Ouahbi 0015:000178                  0.158                     0.0                 0.158     0.061                     0.5         1.0            3     0.196
    Yassine Maleh 0015:000178                   0.158                     0.0                 0.158     0.061                     0.5         1.0            3     0.196
    Ismail Lamaakal 0014:000176                 0.158                     0.0                 0.158     0.061                     0.5         1.0            3     0.196
    Khalid El Makkaoui 0016:000178              0.158                     0.0                 0.158     0.059                     0.5         1.0            3     0.188
    Rajesh Gupta 0014:000003                    0.053                     0.0                 0.053     0.060                     0.0         0.0            1     0.071

"""

from tm2p._intern.netw import BaseNodeMetrics


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):

        from .._intern.create_nx_graph import create_nx_graph

        return create_nx_graph(self.params)
