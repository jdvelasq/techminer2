"""
DirectMatrix
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.direct import DirectMatrix  # type: ignore
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                               Forrester JayWright., 2013, Industrial dynamics 74:0  Sterman J.D., 2000, BUSINESS DYNAMICS 70:0  Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0  Barlas Y, 1996, SYST DYNAM REV 27:0  FORRESTER JW, 1958, HARVARD BUS REV 25:0  Swanson J, 2002, J OPER RES SOC 21:0
    ROWS
    Forrester JayWright., 2013, Industrial dynamics 74:0                                                 0.000                                       0.005                                                0.005                                0.004                                     0.004                                 0.002
    Sterman J.D., 2000, BUSINESS DYNAMICS 70:0                                                           0.005                                       0.000                                                0.000                                0.003                                     0.003                                 0.000
    Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0                                                  0.005                                       0.000                                                0.000                                0.006                                     0.000                                 0.000
    Barlas Y, 1996, SYST DYNAM REV 27:0                                                                  0.004                                       0.003                                                0.006                                0.000                                     0.001                                 0.004
    FORRESTER JW, 1958, HARVARD BUS REV 25:0                                                             0.004                                       0.003                                                0.000                                0.001                                     0.000                                 0.002
    Swanson J, 2002, J OPER RES SOC 21:0                                                                 0.002                                       0.000                                                0.000                                0.004                                     0.002                                 0.000


    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                          Forrester JayWright., 2013, Industrial dynamics  Sterman J.D., 2000, BUSINESS DYNAMICS  Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY  Barlas Y, 1996, SYST DYNAM REV  FORRESTER JW, 1958, HARVARD BUS REV  Swanson J, 2002, J OPER RES SOC
    ROWS
    Forrester JayWright., 2013, Industrial dynamics                                            0.000                                  0.005                                           0.005                           0.004                                0.004                            0.002
    Sterman J.D., 2000, BUSINESS DYNAMICS                                                      0.005                                  0.000                                           0.000                           0.003                                0.003                            0.000
    Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY                                             0.005                                  0.000                                           0.000                           0.006                                0.000                            0.000
    Barlas Y, 1996, SYST DYNAM REV                                                             0.004                                  0.003                                           0.006                           0.000                                0.001                            0.004
    FORRESTER JW, 1958, HARVARD BUS REV                                                        0.004                                  0.003                                           0.000                           0.001                                0.000                            0.002
    Swanson J, 2002, J OPER RES SOC                                                            0.002                                  0.000                                           0.000                           0.004                                0.002                            0.000


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.normaliz_matrix import normalize_matrix

from .matrix import Matrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()

        matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )

        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
