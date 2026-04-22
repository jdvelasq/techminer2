"""
Network Metrics
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, UnitOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import NodeMetrics
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.round(3).head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                     DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Grassi L 2022 1:00024                  0.566                   0.044                 0.678     0.027                   0.145       0.545           49     265.0
    Bagherifam N 2025 1:00000              0.538                   0.023                 0.656     0.026                   0.145       0.605           49     263.0
    El Khoury R 2025 1:00004               0.517                   0.016                 0.644     0.025                   0.143       0.635           49     258.0
    Miglionico A 2022 1:00007              0.573                   0.041                 0.678     0.024                   0.147       0.545           49     227.0
    Kanojia S 2024 1:00003                 0.538                   0.032                 0.653     0.021                   0.142       0.585           49     199.0


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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.round(3).head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                             DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Saule T. Omarova 001:00065                     0.444                   0.056                 0.444     0.202                   0.480       0.500            2       6.0
    Andrea Miglionico 002:00011                    0.444                   0.097                 0.500     0.175                   0.488       0.500            2       5.0
    Joseph Lee 001:00042                           0.222                   0.000                 0.364     0.103                   0.296       1.000            2       3.0
    Ioannis Anagnostopoulos 002:00284              0.444                   0.097                 0.500     0.101                   0.488       0.500            2       2.5
    Johan von Solms 002:00029                      0.333                   0.139                 0.444     0.082                   0.329       0.333            2       1.5


"""

from tm2p._intern.netw import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
