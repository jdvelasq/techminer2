"""
NodeMetrics
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.cit_netw import NodeMetrics  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
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
    >>> from pprint import pprint
    >>> pprint(df.head().round(3))  # doctest: +NORMALIZE_WHITESPACE
    METRIC                                          DEGREE_CENTRALITY  ...  STRENGTH
    NODE                                                               ...
    Ding ZK, 2016, WASTE MANAG 1:00201                          0.069  ...      14.0
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300              0.059  ...      12.0
    Ding ZK, 2018, J CLEAN PROD 1:00178                         0.045  ...       9.0
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207                    0.040  ...       8.0
    Wei SK, 2012, EUR J OPER RES 1:00105                        0.035  ...       7.0
    <BLANKLINE>
    [5 rows x 8 columns]


* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.cit_netw import NodeMetrics  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # OTHER
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(1)
    ...     .having_units_in(None)
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
    >>> from pprint import pprint
    >>> pprint(df.head().round(3))  # doctest: +NORMALIZE_WHITESPACE
    METRIC                      DEGREE_CENTRALITY  ...  STRENGTH
    NODE                                           ...
    Guizhen Yi 002:00379                    0.381  ...     2.958
    Zhikun Ding 002:00379                   0.381  ...     2.958
    Baoquan Cheng 002:00091                 0.238  ...     2.292
    Jianchang Li 002:00091                  0.238  ...     2.292
    Vivian W. Y. Tam 004:00532              0.381  ...     1.750
    <BLANKLINE>
    [5 rows x 8 columns]



"""

from tm2p._intern.netw.node_metric import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(params=self.params)
