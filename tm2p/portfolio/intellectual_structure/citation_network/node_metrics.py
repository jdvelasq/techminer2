"""
NodeDegreeDataFrame
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CitationUnit
    >>> from tm2p.synthesize.netw.cit import NodeDegreeDataFrame
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
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
    >>> df.head()
                                                    NAME  DEGREE
    0  Takeda A, 2021, INT J TECHNOL MANAG, V86, P67 ...       4
    1  Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.339...       4
    2  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7,...       3
    3  Anagnostopoulos I, 2018, J ECON BUS, V100, P7,...       3
    4  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55...       3



* **CitationUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
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
    >>> df.head()
                              NAME  DEGREE
    0        Zetzsche DA 008:00699      12
    1           Arner DW 007:00887      12
    2         Buckley RP 007:00887      12
    3  Anagnostopoulos I 002:00284      12
    4             Xia YF 004:00008      10


* **CitationUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> df = (
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()
                NAME  DEGREE
    0  GBR 026:01562      24
    1  AUS 024:01072      24
    2  JOR 003:00022      24
    3  CHN 046:01426      23
    4  USA 021:00494      23


* **CitationUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
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
    ... ).head()


* **CitationUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.SRC)
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
    ... ).head()


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import CitationUnit, ItemOrderBy
from tm2p.portfolio.intellectual_structure.citation_network._intern.doc import (
    DocNodeDegreeDataFrame,
)
from tm2p.portfolio.intellectual_structure.citation_network._intern.other import (
    OtherNodeDegreeDataFrame,
)

from ...._intern.helpers.check_database import check_database


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

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
