"""
NodeMetrics
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CitationUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import NodeMetrics
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
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
                                    DEGREE_CENTRALITY  ...  STRENGTH
    El Khoury R 2025 1:00004                 0.342593  ...      37.0
    Anagnostopoulos I 2018 1:00284           0.287037  ...      31.0
    Grassi L 2022 1:00024                    0.287037  ...      31.0
    Bagherifam N 2025 1:00000                0.268519  ...      29.0
    Becker M 2020 1:00012                    0.138889  ...      15.0
    <BLANKLINE>
    [5 rows x 8 columns]


* **CitationUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
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
                                DEGREE_CENTRALITY  ...  STRENGTH
    Michael Becker 002:00017             0.263158  ...  1.250000
    Johan von Solms 002:00029            0.263158  ...  1.125000
    Zhengxu Shi 002:00003                0.315789  ...  0.955357
    Huiyi Shi 002:00004                  0.315789  ...  0.830357
    Douglas W. Arner 007:00887           0.578947  ...  0.752551
    <BLANKLINE>
    [5 rows x 8 columns]


* **CitationUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
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
                   DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  ...  CORE_NUMBER  STRENGTH
    LBN 002:00116           0.652174                0.030396  ...           10  2.078692
    CHE 004:00086           0.695652                0.025677  ...           10  1.870764
    JOR 003:00022           0.782609                0.062858  ...           10  1.784321
    BHR 002:00019           0.434783                0.010229  ...            9  1.336310
    MYS 002:00016           0.434783                0.003809  ...            9  1.004108
    <BLANKLINE>
    [5 rows x 8 columns]


* **CitationUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
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
    ... )
    >>> df.head()
                                 DEGREE_CENTRALITY  ...  STRENGTH
    HARV UNIV 002:00046                     0.4375  ...  2.708333
    LEBAN AMER UNIV 002:00116               0.5000  ...  2.166667
    JIANGSU NORM UNIV 004:00008             0.4375  ...  1.666667
    MONASH UNIV 003:00006                   0.4375  ...  1.444444
    FOM UNIV APPL SCI 002:00017             0.2500  ...  1.083333
    <BLANKLINE>
    [5 rows x 8 columns]


* **CitationUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     NodeMetrics()
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
    ... )
    >>> df.head()
                                   DEGREE_CENTRALITY  ...  STRENGTH
    INT REV FINANC ANAL 002:00030           0.200000  ...  0.750000
    J BANK REGUL 005:00094                  0.533333  ...  0.646667
    SUSTAIN FUTUR 002:00003                 0.266667  ...  0.641667
    INT J LAW MANAG 002:00012               0.200000  ...  0.600000
    RES INT BUS FINANC 002:00006            0.133333  ...  0.350000
    <BLANKLINE>
    [5 rows x 8 columns]


"""

from tm2p._intern.networks.node_metrics import BaseNodeMetrics

from .item_to_cluster import _create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return _create_nx_graph(params=self.params)
