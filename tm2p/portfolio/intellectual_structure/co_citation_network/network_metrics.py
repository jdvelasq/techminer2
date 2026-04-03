"""
NetworkMetrics
===============================================================================

* **CITED_AUTH**

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_AUTH)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
                                         DEGREE  BETWEENNESS  CLOSENESS  PAGERANK  EIGENVECTOR  CLUSTERING  CORE  STRENGTH
    Arner DW 1:107                     1.000000     0.018224   1.000000  0.043872     0.225937    0.777778    17        81
    Zetzsche DA 1:033                  1.000000     0.018224   1.000000  0.043872     0.225937    0.777778    17        81
    Anagnostopoulos I 1:031            1.000000     0.018224   1.000000  0.043872     0.225937    0.777778    17        81
    Financial Conduct Authority 1:037  0.962963     0.013892   0.964286  0.042328     0.220773    0.803077    17        78
    Butler T 1:033                     0.962963     0.014705   0.964286  0.042344     0.220578    0.800000    17        78


* **CITED_REF**

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                 DEGREE  BETWEENNESS  CLOSENESS  PAGERANK  EIGENVECTOR  CLUSTERING  CORE  STRENGTH
    Arner DW, 2017, NW J INT LAW BUS 1:50      1.000000     0.020319   1.000000  0.041386     0.217795    0.770936    19        87
    Anagnostopoulos I, 2018, J ECON BUS 1:31   1.000000     0.020319   1.000000  0.041386     0.217795    0.770936    19        87
    Butler T, 2019, PALGR ST DIG BUS ENA 1:21  0.965517     0.015397   0.966667  0.039953     0.214245    0.798942    19        84
    Kavassalis P, 2018, J RISK FINANC 1:13     0.965517     0.015397   0.966667  0.039953     0.214245    0.798942    19        84
    Yang D, 2018, EMERG MARK FINANC TR 1:08    0.965517     0.018015   0.966667  0.040059     0.212667    0.785714    19        84



* **CITED_SRC**

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_SRC)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
                               DEGREE  BETWEENNESS  CLOSENESS  PAGERANK  EIGENVECTOR  CLUSTERING  CORE  STRENGTH
    J FINANC 1:95                 1.0     0.001737        1.0  0.035628     0.191772    0.960317    24        84
    REV FINANC STUD 1:80          1.0     0.001737        1.0  0.035628     0.191772    0.960317    24        84
    INT REV FINANC ANAL 1:65      1.0     0.001737        1.0  0.035628     0.191772    0.960317    24        84
    FINANC RES LETT 1:59          1.0     0.001737        1.0  0.035628     0.191772    0.960317    24        84
    TECHNOL FORECAST SOC 1:57     1.0     0.001737        1.0  0.035628     0.191772    0.960317    24        84



"""

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx.compute_network_metrics import compute_network_metrics
from tm2p.portfolio.intellectual_structure.co_citation_network._intern.create_nx_graph import (
    create_nx_graph,
)


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = create_nx_graph(self.params)
        df = compute_network_metrics(nx_graph=nx_graph)

        if use_counters is False:
            self.params.counters = False
            names = df.index.tolist()
            names = [remove_counters(name) for name in names]
            df.index = names

        return df
