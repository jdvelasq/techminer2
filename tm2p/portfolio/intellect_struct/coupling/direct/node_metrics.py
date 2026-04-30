"""
Network Metrics
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.coupling.direct import NodeMetrics  # type: ignore
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.round(3).head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                                                     DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE                                                                                                                                                                                           
    Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAG 1:00030               0.269                   0.005                 0.521     0.008                   0.116       0.662           73     245.0
    Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAGa 1:00018              0.269                   0.005                 0.521     0.008                   0.116       0.662           73     243.0
    Poornikoo M, 2019, J MODEL MANAG 1:00017                               0.309                   0.007                 0.533     0.007                   0.120       0.540           73     210.0
    Khan S, 2009, ENV MODEL SOFTW 1:00084                                  0.300                   0.017                 0.534     0.008                   0.095       0.425           73     204.0
    Yuan HP/1, 2012, WASTE MANAG 1:00109                                   0.298                   0.006                 0.532     0.007                   0.119       0.566           73     200.0


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**


Smoke tests:
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(100)
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.round(3).head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                          DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE                                                                                                                                                                
    Tae Ho Woo 004:00007                          1.0                     0.0                   1.0     0.412                   0.577         1.0            2     0.583
    T. H. Woo 003:00005                           1.0                     0.0                   1.0     0.320                   0.577         1.0            2     0.444
    Yahia Zare Mehrjerdi 003:00008                1.0                     0.0                   1.0     0.268                   0.577         1.0            2     0.361


"""

from tm2p._intern.netw import BaseNodeMetrics


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):

        from .._intern.create_nx_graph import create_nx_graph

        return create_nx_graph(self.params)
