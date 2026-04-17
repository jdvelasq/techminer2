"""
MatrixList
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import MatrixList
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                           CITED_UNIT               CITING_UNIT  OCC
    0           Arner DW 2019 1:00045     Arner DW 2020 1:00338    1
    1         Buckley RP 2020 1:00037     Arner DW 2020 1:00338    1
    2         Omarova ST 2020 1:00065  Zetzsche DA 2020 1:00222    1
    3       Kavassalis P 2018 1:00026      Mirza N 2023 1:00112    1
    4  Anagnostopoulos I 2018 1:00284    Muganyi T 2022 1:00109    1
    5  Anagnostopoulos I 2018 1:00284     Takeda A 2021 1:00066    1
    6          Currie WL 2018 1:00043     Takeda A 2021 1:00066    1
    7              Lui A 2018 1:00096     Takeda A 2021 1:00066    1
    8             Yang D 2018 1:00043     Takeda A 2021 1:00066    1
    9          Baxter LG 2016 1:00030   Omarova ST 2020 1:00065    1


* **AnalysisUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
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
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
                       CITING_UNIT                  CITED_UNIT  OCC
    0          Yufei Xia 004:00008  Dirk A. Zetzsche 008:00699    2
    1          Yufei Xia 004:00008  Douglas W. Arner 007:00887    2
    2          Yufei Xia 004:00008   Ross P. Buckley 007:00887    2
    3  Andrea Miglionico 002:00011  Dirk A. Zetzsche 008:00699    2
    4  Andrea Miglionico 002:00011  Douglas W. Arner 007:00887    2
    5  Andrea Miglionico 002:00011   Ross P. Buckley 007:00887    2
    6        Zhengxu Shi 002:00003         Yufei Xia 004:00008    2
    7   Dirk A. Zetzsche 008:00699  Douglas W. Arner 007:00887    1
    8   Dirk A. Zetzsche 008:00699   Ross P. Buckley 007:00887    1
    9   Douglas W. Arner 007:00887  Dirk A. Zetzsche 008:00699    1


* **AnalysisUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CTRY)
    ...     #
    ...     .having_top_n_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
         CITING_UNIT     CITED_UNIT  OCC
    0  CHN 046:01426  CHE 004:00086   11
    1  CHN 046:01426  USA 021:00494   10
    2  CHN 046:01426  DEU 014:00785   10
    3  IND 009:00128  CHN 046:01426   10
    4  AUS 024:01072  CHN 046:01426    8
    5  IND 009:00128  AUS 024:01072    8
    6  IND 009:00128  DEU 014:00785    8
    7  LBN 002:00116  DEU 014:00785    7
    8  GBR 026:01562  DEU 014:00785    6
    9  AUS 024:01072  DEU 014:00785    6


* **AnalysisUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.ORG)
    ...     #
    ...     .having_top_n_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
                       CITING_UNIT                              CITED_UNIT  OCC
    0  JIANGSU NORM UNIV 004:00008                     HARV UNIV 002:00046    5
    1  JIANGSU NORM UNIV 004:00008  SOUTHWEST UNIV FINANC & ECON 002:00031    3
    2    LEBAN AMER UNIV 002:00116                UNIV HONG KONG 008:00903    3
    3    LEBAN AMER UNIV 002:00116                  UNIV LUXEMBG 008:00699    3
    4    LEBAN AMER UNIV 002:00116           HEINRICH HEINE UNIV 004:00642    3
    5  JIANGSU NORM UNIV 004:00008                UNIV HONG KONG 008:00903    2
    6  JIANGSU NORM UNIV 004:00008                  UNIV LUXEMBG 008:00699    2
    7  JIANGSU NORM UNIV 004:00008           HEINRICH HEINE UNIV 004:00642    2
    8  JIANGSU NORM UNIV 004:00008            GOETHE UNIV FRANKF 002:00027    2
    9        MONASH UNIV 003:00006             JIANGSU NORM UNIV 004:00008    2



* **AnalysisUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_analysis_unit(AnalysisUnit.SRC)
    ...     #
    ...     .having_top_n_units(30)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
                               CITING_UNIT                       CITED_UNIT  OCC
    0      EUR BUS ORGAN LAW REV 005:00506           J BANK REGUL 005:00094    1
    1  J FINANC REGUL COMPLIANCE 005:00014  EUR BUS ORGAN LAW REV 005:00506    1
    2  J FINANC REGUL COMPLIANCE 005:00014           J BANK REGUL 005:00094    1
    3  J FINANC REGUL COMPLIANCE 005:00014         J FINANC REGUL 004:00298    1
    4      J MONEY LAUND CONTROL 003:00040           J BANK REGUL 005:00094    1
    5             FUTUR INTERNET 002:00019           J BANK REGUL 005:00094    1
    6            INT J INNOV SCI 002:00002    INT REV FINANC ANAL 002:00030    1
    7            INT J LAW MANAG 002:00012           J BANK REGUL 005:00094    1
    8            INT J LAW MANAG 002:00012                 COMPUT 002:00006    1
    9               J GLOB MANAG 002:00004         J FINANC REGUL 004:00298    1


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit

from ...._intern.helpers.check_database import check_database
from ._intern.doc import DocMatrixList
from ._intern.other import OtherMatrixList


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

        if self.params.analysis_unit == AnalysisUnit.DOC:
            matrix_list = DocMatrixList
        else:
            matrix_list = OtherMatrixList

        return matrix_list().update(**self.params.__dict__).run()
