"""
MatrixList
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.cit_netw import MatrixList  # type: ignore
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                           CITED_UNIT                                     CITING_UNIT  OCC
    0            Yuan HP/1, 2012, WASTE MANAG 1:00109  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300    1
    1  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300        Liu JK, 2020, ENV SCI POLLUT RES 1:00207    1
    2           Wang JY/1, 2015, J CLEAN PROD 1:00143        Liu JK, 2020, ENV SCI POLLUT RES 1:00207    1
    3    Hao JLJ, 2010, ENG CONSTR ARCH MANAG 1:00025              Ding ZK, 2016, WASTE MANAG 1:00201    1
    4  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300              Ding ZK, 2016, WASTE MANAG 1:00201    1
    5              Ding ZK, 2016, WASTE MANAG 1:00201             Ding ZK, 2018, J CLEAN PROD 1:00178    1
    6           Wang JY/1, 2015, J CLEAN PROD 1:00143             Ding ZK, 2018, J CLEAN PROD 1:00178    1
    7            Lan TS, 2013, MATH PROBL ENG 1:00005           Orji IJ, 2015, COMPUT IND ENG 1:00125    1
    8            Wei SK, 2012, EUR J OPER RES 1:00105                 He L, 2022, WASTE MANAG 1:00091    1
    9           Wang JY/1, 2015, J CLEAN PROD 1:00143               Li CZ, 2017, J CLEAN PROD 1:00079    1


* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
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
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
                      CITING_UNIT                  CITED_UNIT  OCC
    0      Chunbing Guo 003:00009         Lihong Li 003:00019    4
    1     Baoquan Cheng 002:00091  Vivian W. Y. Tam 004:00532    3
    2     Baoquan Cheng 002:00091        Guizhen Yi 002:00379    3
    3     Baoquan Cheng 002:00091       Zhikun Ding 002:00379    3
    4      Jianchang Li 002:00091  Vivian W. Y. Tam 004:00532    3
    5      Jianchang Li 002:00091        Guizhen Yi 002:00379    3
    6      Jianchang Li 002:00091       Zhikun Ding 002:00379    3
    7  Vivian W. Y. Tam 004:00532   Mohamed Marzouk 003:00323    2
    8  Vivian W. Y. Tam 004:00532        Guizhen Yi 002:00379    2
    9  Vivian W. Y. Tam 004:00532       Shimaa Azab 002:00315    2


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit

from ...._intern.helpers.check_db import check_database
from ._intern.doc_matrix_list import DocMatrixList
from ._intern.other_matrix_list import OtherMatrixList


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
