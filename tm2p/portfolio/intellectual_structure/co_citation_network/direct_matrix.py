"""
DirectMatrix
===============================================================================

* **CITED_REF**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import DirectMatrix
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                                     Williams JW, 2013, ACCOUNT ORG SOC 9:0  Kurum E, 2023, Journal of Financial Crime 9:0  Becker M, 2020, INTELL SYST ACCOUNT 9:0  Yang D, 2018, EMERG MARK FINANC TR 8:0  Turki M, 2020, HELIYON 8:0  PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review 8:0
    ROWS
    Williams JW, 2013, ACCOUNT ORG SOC 9:0                                                       0.000                                          0.025                                    0.012                                   0.028                       0.000                                                       0.028
    Kurum E, 2023, Journal of Financial Crime 9:0                                                0.025                                          0.000                                    0.062                                   0.056                       0.069                                                       0.056
    Becker M, 2020, INTELL SYST ACCOUNT 9:0                                                      0.012                                          0.062                                    0.000                                   0.056                       0.042                                                       0.042
    Yang D, 2018, EMERG MARK FINANC TR 8:0                                                       0.028                                          0.056                                    0.056                                   0.000                       0.047                                                       0.047
    Turki M, 2020, HELIYON 8:0                                                                   0.000                                          0.069                                    0.042                                   0.047                       0.000                                                       0.031
    PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review 8:0                                   0.028                                          0.056                                    0.042                                   0.047                       0.031                                                       0.000


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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                                 Williams JW, 2013, ACCOUNT ORG SOC  Kurum E, 2023, Journal of Financial Crime  Becker M, 2020, INTELL SYST ACCOUNT  Yang D, 2018, EMERG MARK FINANC TR  Turki M, 2020, HELIYON  PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review
    ROWS
    Williams JW, 2013, ACCOUNT ORG SOC                                                   0.000                                      0.025                                0.012                               0.028                   0.000                                                   0.028
    Kurum E, 2023, Journal of Financial Crime                                            0.025                                      0.000                                0.062                               0.056                   0.069                                                   0.056
    Becker M, 2020, INTELL SYST ACCOUNT                                                  0.012                                      0.062                                0.000                               0.056                   0.042                                                   0.042
    Yang D, 2018, EMERG MARK FINANC TR                                                   0.028                                      0.056                                0.056                               0.000                   0.047                                                   0.047
    Turki M, 2020, HELIYON                                                               0.000                                      0.069                                0.042                               0.047                   0.000                                                   0.031
    PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review                               0.028                                      0.056                                0.042                               0.047                   0.031                                                   0.000


* **CITED_AUTH**

Smoke tests:

    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_AUTH)
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS          Williams JW 9:0  Magnuson W 9:0  Kurum E 9:0  Brummer C 9:0  Yeung K 8:0  Yang D 8:0
    ROWS
    Williams JW 9:0            0.000           0.000        0.025          0.000        0.014       0.028
    Magnuson W 9:0             0.000           0.000        0.000          0.049        0.000       0.014
    Kurum E 9:0                0.025           0.000        0.000          0.000        0.000       0.056
    Brummer C 9:0              0.000           0.049        0.000          0.000        0.000       0.000
    Yeung K 8:0                0.014           0.000        0.000          0.000        0.000       0.000
    Yang D 8:0                 0.028           0.014        0.056          0.000        0.000       0.000


* **CITED_SRC**

Smoke tests:
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_SRC)
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
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                       SSRN Electronic Journal 52:0  NW J INT LAW BUS 52:0  J ECON BUS 37:0  REV FINANC STUD 33:0  TECHNOL FORECAST SOC 32:0  J FINANC ECON 31:0
    ROWS
    SSRN Electronic Journal 52:0                         0.000                  0.009            0.006                 0.008                      0.006               0.006
    NW J INT LAW BUS 52:0                                0.009                  0.000            0.012                 0.006                      0.004               0.007
    J ECON BUS 37:0                                      0.006                  0.012            0.000                 0.007                      0.008               0.008
    REV FINANC STUD 33:0                                 0.008                  0.006            0.007                 0.000                      0.009               0.021
    TECHNOL FORECAST SOC 32:0                            0.006                  0.004            0.008                 0.009                      0.000               0.010
    J FINANC ECON 31:0                                   0.006                  0.007            0.008                 0.021                      0.010               0.000


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.networks.normalize_matrix import normalize_matrix

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
