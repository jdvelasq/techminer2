"""
ItemsByCluster
===============================================================================


* **CouplingUnit.AUTH**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
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
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
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
                           0  ...                     7
    0       Xia YF 004:00008  ...   Currie WL 002:00061
    1  von Solms J 002:00029  ...  Seddon JJM 002:00061
    2   Lokanan ME 002:00021  ...
    3     Becker M 002:00017  ...
    4    Kshetri N 002:00006  ...
    <BLANKLINE>
    [5 rows x 8 columns]


* **CouplingUnit.CTRY**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
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
         0    1    2    3
    0  IND  CHN  USA  FRA
    1  CAN  GBR  ITA  NLD
    2  UKR  AUS  TWN  BEL
    3  JPN  DEU  ESP  KOR
    4  IDN  LUX  SGP  IRL


* **CouplingUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
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
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
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
                                                     0  ...                                            3
    0     Arner DW, 2020, EUR BUS ORGAN LAW RE 1:00338  ...      Mirza N, 2023, ECON ANAL POLICY 1:00112
    1        Zetzsche DA, 2020, J FINANC REGUL 1:00222  ...        Muganyi T, 2022, FINANC INNOV 1:00109
    2         Omarova ST, 2020, J FINANC REGUL 1:00065  ...    Sangwan V, 2019, STUD ECON FINANC 1:00082
    3  Zetzsche DA, 2022, EUR BUS ORGAN LAW RE 1:00051  ...  Takeda A, 2021, INT J TECHNOL MANAG 1:00066
    4     Arner DW, 2019, EUR BUS ORGAN LAW RE 1:00045  ...        Nasir A, 2021, APPL SCI-BASEL 1:00040
    <BLANKLINE>
    [5 rows x 4 columns]


* **CouplingUnit.SRC**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
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
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
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
                                         0  ...                              2
    0  J FINANC REGUL COMPLIANCE 005:00014  ...      INT J LAW MANAG 002:00012
    1                  J TECHNOL 004:00110  ...  J ISLAM ACC BUS RES 002:00001
    2      J MONEY LAUND CONTROL 003:00040  ...
    3            FINANC RES LETT 003:00002  ...
    4        INT REV FINANC ANAL 002:00030  ...
    <BLANKLINE>
    [5 rows x 3 columns]


* **CouplingUnit.ORG**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
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
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
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



"""

from tm2p._intern import ParamsMixin
from tm2p.enum import CouplingUnit, ItemOrderBy
from tm2p.portfolio.intellectual_structure.coupling_network._intern.doc import (
    DocItemsByCluster,
)
from tm2p.portfolio.intellectual_structure.coupling_network._intern.others import (
    OtherItemsByCluster,
)

from ...._intern.check_database import check_database


class ItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

        if self.params.coupling_unit == CouplingUnit.DOC:
            ItemsByCluster_ = DocItemsByCluster
        else:
            ItemsByCluster_ = OtherItemsByCluster

        return (
            ItemsByCluster_()
            .update(**self.params.__dict__)
            .update(items_order_by=ItemOrderBy.OCC)
            .run()
        )
