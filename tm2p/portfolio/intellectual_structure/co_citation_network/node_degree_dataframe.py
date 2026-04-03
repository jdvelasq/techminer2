"""
NodeDegreeDataFrame
===============================================================================

* **CITED_AUTH**

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
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
    ... ).head()
                                    NAME  DEGREE
    0                     Arner DW 1:107      27
    1                  Zetzsche DA 1:033      27
    2            Anagnostopoulos I 1:031      27
    3  Financial Conduct Authority 1:037      26
    4                     Butler T 1:033      26


* **CITED_REF**

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
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
    ... ).head()
                                            NAME  DEGREE
    0      Arner DW, 2017, NW J INT LAW BUS 1:50      29
    1   Anagnostopoulos I, 2018, J ECON BUS 1:31      29
    2  Butler T, 2019, PALGR ST DIG BUS ENA 1:21      28
    3     Kavassalis P, 2018, J RISK FINANC 1:13      28
    4    Yang D, 2018, EMERG MARK FINANC TR 1:08      28


* **CITED_SRC**

Smoke tests:
    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthesize.netw.co_cit import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
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
    ... ).head()
                            NAME  DEGREE
    0              J FINANC 1:95      28
    1       REV FINANC STUD 1:80      28
    2   INT REV FINANC ANAL 1:65      28
    3       FINANC RES LETT 1:59      28
    4  TECHNOL FORECAST SOC 1:57      28




"""

from tm2p._intern import ParamsMixin
from tm2p._intern.nx import (
    assign_degree_to_nodes,
    collect_node_degrees,
    create_node_degree_dataframe,
)
from tm2p.portfolio.intellectual_structure.co_citation_network._intern.create_nx_graph import (
    create_nx_graph,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = create_nx_graph(self.params)
        nx_graph = assign_degree_to_nodes(nx_graph)
        node_degrees = collect_node_degrees(nx_graph)
        data_frame = create_node_degree_dataframe(node_degrees)

        return data_frame
