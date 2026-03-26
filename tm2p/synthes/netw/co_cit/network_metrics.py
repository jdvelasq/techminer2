"""
NetworkMetrics
===============================================================================

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthes.netw.co_cit import NetworkMetrics
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



"""

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx.compute_network_metrics import compute_network_metrics
from tm2p.synthes.netw.co_cit._intern.create_nx_graph import create_nx_graph


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
