"""
Network Metrics
===============================================================================

* **CouplingUnit.AUTH**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
                              DEGREE  BETWEENNESS  CLOSENESS  PAGERANK  EIGENVECTOR  CLUSTERING  CORE  STRENGTH
    Becker M 002:00017      0.655172     0.067639   0.667586  0.014239     0.245340    0.719298    15       106
    Miglionico A 002:00011  0.655172     0.067639   0.667586  0.020757     0.245340    0.719298    15       218
    Xia YF 004:00008        0.620690     0.015094   0.641910  0.043459     0.250664    0.836601    15       527
    Shi HY 002:00004        0.620690     0.015094   0.641910  0.024763     0.250664    0.836601    15       272
    Shi ZX 002:00003        0.620690     0.015094   0.641910  0.037544     0.250664    0.836601    15       446



* **CouplingUnit.CTRY**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
                     DEGREE  BETWEENNESS  CLOSENESS  PAGERANK  EIGENVECTOR  CLUSTERING  CORE  STRENGTH
    CHN 046:01426  0.965517     0.008613   0.966667  0.124097     0.200834    0.883598    23      4622
    GBR 026:01562  0.965517     0.008613   0.966667  0.087696     0.200834    0.883598    23      3286
    AUS 024:01072  0.965517     0.008613   0.966667  0.120769     0.200834    0.883598    23      4555
    USA 021:00494  0.965517     0.008613   0.966667  0.055047     0.200834    0.883598    23      1890
    ITA 012:00116  0.965517     0.008613   0.966667  0.047270     0.200834    0.883598    23      1538


* **CouplingUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                    DEGREE  BETWEENNESS  CLOSENESS  PAGERANK  EIGENVECTOR  CLUSTERING  CORE  STRENGTH
    Omarova ST, 2020, J FINANC REGUL 1:00065      0.653846     0.127481   0.702703  0.060487     0.309930    0.529412    10        31
    Arner DW, 2020, EUR BUS ORGAN LAW RE 1:00338  0.576923     0.038647   0.634146  0.093622     0.299687    0.657143    10        54
    Sangwan V, 2019, STUD ECON FINANC 1:00082     0.576923     0.093467   0.666667  0.083089     0.286860    0.590476    10        47
    Fast V, 2023, J TECHNOL 1:00040               0.576923     0.252514   0.702703  0.038973     0.277005    0.542857    10        18
    Anagnostopoulos I, 2018, J ECON BUS 1:00284   0.538462     0.028638   0.619048  0.047678     0.286553    0.692308    10        25


* **CouplingUnit.ORG**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE


* **CouplingUnit.SRC**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(5).to_string())  # doctest: +NORMALIZE_WHITESPACE




"""

from tm2p._intern.networks import BaseNodeMetrics
from tm2p.enum import CouplingUnit

from ...._intern.helpers.check_database import check_database
from ._intern.doc.create_nx_graph import doc_create_nx_graph
from ._intern.others.create_nx_graph import other_create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self, params):

        check_database(self.params.root_directory)

        if self.params.coupling_unit == CouplingUnit.DOC:
            create_nx_graph = doc_create_nx_graph
        else:
            create_nx_graph = other_create_nx_graph

        return create_nx_graph(params)


# from tm2p._intern import ParamsMixin, remove_counters
# from tm2p._intern.plots.nx import compute_node_metrics
# from tm2p.enum import CouplingUnit

# from ...._intern.helpers.check_database import check_database
# from ._intern.doc.create_nx_graph import doc_create_nx_graph
# from ._intern.others.create_nx_graph import other_create_nx_graph


# class NodeMetrics(
#     ParamsMixin,
# ):
#     """:meta private:"""

#     def run(self):

#         check_database(self.params.root_directory)

#         if self.params.coupling_unit == CouplingUnit.DOC:
#             create_nx_graph = doc_create_nx_graph
#         else:
#             create_nx_graph = other_create_nx_graph

#         use_counters = self.params.counters
#         self.params.counters = True
#         nx_graph = create_nx_graph(self.params)
#         df = compute_node_metrics(nx_graph=nx_graph)

#         if use_counters is False:
#             self.params.counters = False
#             names = df.index.tolist()
#             names = [remove_counters(name) for name in names]
#             df.index = names

#         return df
