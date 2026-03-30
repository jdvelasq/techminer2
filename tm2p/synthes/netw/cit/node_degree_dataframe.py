"""
NodeDegreeDataFrame
===============================================================================

Smoke tests:
    >>> from tm2p import CitationUnit
    >>> from tm2p.synthes.netw.cit import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       NODE                                               NAME  DEGREE
    0     0  Takeda A, 2021, INT J TECHNOL MANAG, V86, P67 ...       4
    1     1  Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.339...       4
    2     2  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7,...       3
    3     3  Anagnostopoulos I, 2018, J ECON BUS, V100, P7,...       3
    4     4  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55...       3


    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       NODE                                               NAME  DEGREE
    0     0      Takeda A, 2021, INT J TECHNOL MANAG, V86, P67       4
    1     1  Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.339...       4
    2     2  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7,...       3
    3     3  Anagnostopoulos I, 2018, J ECON BUS, V100, P7,...       3
    4     4  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55...       3


    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       NODE           NAME  DEGREE
    0     0  GBR 026:01562      24
    1     1  AUS 024:01072      24
    2     2  JOR 003:00022      24
    3     3  CHN 046:01426      23
    4     4  USA 021:00494      23


    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       NODE NAME  DEGREE
    0     0  GBR      24
    1     1  AUS      24
    2     2  JOR      24
    3     3  CHN      23
    4     4  USA      23

"""

from tm2p import CitationUnit, ItemOrderBy
from tm2p._intern import ParamsMixin
from tm2p.synthes.netw.cit._intern.doc import (
    NodeDegreeDataFrame as DocNodeDegreeDataFrame,
)
from tm2p.synthes.netw.cit._intern.other import (
    NodeDegreeDataFrame as OtherNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.citation_unit == CitationUnit.DOC:
            NodeDegree = DocNodeDegreeDataFrame
        else:
            NodeDegree = OtherNodeDegreeDataFrame

        return (
            NodeDegree()
            .update(**self.params.__dict__)
            .update(items_order_by=ItemOrderBy.OCC)
            .run()
        )
