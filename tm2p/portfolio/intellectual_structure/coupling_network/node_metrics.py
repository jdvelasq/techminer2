"""
Network Metrics
===============================================================================

* **CouplingUnit.AUTH**

* **CouplingUnit.CTRY**

* **CouplingUnit.DOC**

* **CouplingUnit.ORG**

* **CouplingUnit.SRC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CouplingUnit, GraphClusteringAlgorithm, ItemOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     #
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(1)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.round(3).head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                             DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Ioannis Anagnostopoulos 002:00284              0.667                   0.000                  0.75     0.286                   0.523       1.000            2       1.5
    Johan von Solms 002:00029                      1.000                   0.667                  1.00     0.305                   0.612       0.333            2       1.5
    Andrea Miglionico 002:00011                    0.667                   0.000                  0.75     0.286                   0.523       1.000            2       1.5
    Nir Kshetri 002:00006                          0.333                   0.000                  0.60     0.124                   0.282       0.000            1       0.5


"""

from tm2p._intern.networks import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
