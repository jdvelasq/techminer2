"""
Network Degree Frame
===============================================================================

* **CouplingUnit.AUTH**

Smoke tests:
    >>> from tm2p import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreeDataFrame
    >>> df = (
    ...     NodeDegreeDataFrame()
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                         NAME  DEGREE
    0      Becker M 002:00017      19
    1  Miglionico A 002:00011      19
    2        Xia YF 004:00008      18
    3        Shi HY 002:00004      18
    4        Shi ZX 002:00003      18


* **CouplingUnit.CTRY**

Smoke tests:
    >>> from tm2p import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreeDataFrame
    >>> df = (
    ...     NodeDegreeDataFrame()
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                               NAME  DEGREE
    0      Omarova ST, 2020, J FINANC REGUL 1:00065      17
    1  Arner DW, 2020, EUR BUS ORGAN LAW RE 1:00338      15
    2     Sangwan V, 2019, STUD ECON FINANC 1:00082      15
    3               Fast V, 2023, J TECHNOL 1:00040      15
    4   Anagnostopoulos I, 2018, J ECON BUS 1:00284      14



* **CouplingUnit.DOC**

Smoke tests:
    >>> from tm2p import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreeDataFrame
    >>> df = (
    ...     NodeDegreeDataFrame()
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                               NAME  DEGREE
    0      Omarova ST, 2020, J FINANC REGUL 1:00065      17
    1  Arner DW, 2020, EUR BUS ORGAN LAW RE 1:00338      15
    2     Sangwan V, 2019, STUD ECON FINANC 1:00082      15
    3               Fast V, 2023, J TECHNOL 1:00040      15
    4   Anagnostopoulos I, 2018, J ECON BUS 1:00284      14



* **CouplingUnit.ORG**

Smoke tests:
    >>> from tm2p import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import NodeDegreeDataFrame
    >>> df = (
    ...     NodeDegreeDataFrame()
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
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                               NAME  DEGREE
    0      Omarova ST, 2020, J FINANC REGUL 1:00065      17
    1  Arner DW, 2020, EUR BUS ORGAN LAW RE 1:00338      15
    2     Sangwan V, 2019, STUD ECON FINANC 1:00082      15
    3               Fast V, 2023, J TECHNOL 1:00040      15
    4   Anagnostopoulos I, 2018, J ECON BUS 1:00284      14


* **CouplingUnit.SRC**

    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                       NAME  DEGREE
    0      Omarova ST, 2020, J FINANC REGUL      17
    1  Arner DW, 2020, EUR BUS ORGAN LAW RE      15
    2     Sangwan V, 2019, STUD ECON FINANC      15
    3               Fast V, 2023, J TECHNOL      15
    4   Anagnostopoulos I, 2018, J ECON BUS      14


"""

from tm2p import CouplingUnit, ItemOrderBy
from tm2p._intern import ParamsMixin
from tm2p.synthesize.netw.coupl._intern.doc import DocNodeDegreeDataFrame
from tm2p.synthesize.netw.coupl._intern.other import OtherNodeDegreeDataFrame

from .._check_database import check_database


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

        if self.params.coupling_unit == CouplingUnit.DOC:
            NodeDegree = DocNodeDegreeDataFrame
        else:
            NodeDegree = OtherNodeDegreeDataFrame

        return (
            NodeDegree()
            .update(**self.params.__dict__)
            .update(items_order_by=ItemOrderBy.OCC)
            .run()
        )
