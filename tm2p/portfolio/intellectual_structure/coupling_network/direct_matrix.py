"""
DirectMatrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import DirectMatrix
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
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
    COLUMNS                         Arner DW 2020 1:00338  Anagnostopoulos I 2018 1:00284  Demirel P 2019 1:00279  Arner DW 2017 1:00242  Zetzsche DA 2020 1:00222  Mirza N 2023 1:00112
    ROWS
    Arner DW 2020 1:00338                             0.0                             4.0                     0.0                    4.0                       2.0                   1.0
    Anagnostopoulos I 2018 1:00284                    4.0                             0.0                     0.0                    4.0                       1.0                   1.0
    Demirel P 2019 1:00279                            0.0                             0.0                     0.0                    0.0                       0.0                   0.0
    Arner DW 2017 1:00242                             4.0                             4.0                     0.0                    0.0                       1.0                   0.0
    Zetzsche DA 2020 1:00222                          2.0                             1.0                     0.0                    1.0                       0.0                   1.0
    Mirza N 2023 1:00112                              1.0                             1.0                     0.0                    0.0                       1.0                   0.0


* **AnalysisUnit.AUTH**

Smoke tests:
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
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
    COLUMNS                            Ioannis Anagnostopoulos 002:00284  Johan von Solms 002:00029  Andrea Miglionico 002:00011  Nir Kshetri 002:00006  Joseph Jye-Cherng Lyu 002:00003  Sanjiv R. Das 001:00090
    ROWS
    Ioannis Anagnostopoulos 002:00284                                0.0                        0.5                          1.0                    0.0                              0.0                      0.0
    Johan von Solms 002:00029                                        0.5                        0.0                          0.5                    0.5                              0.0                      0.0
    Andrea Miglionico 002:00011                                      1.0                        0.5                          0.0                    0.0                              0.0                      0.0
    Nir Kshetri 002:00006                                            0.0                        0.5                          0.0                    0.0                              0.0                      0.0
    Joseph Jye-Cherng Lyu 002:00003                                  0.0                        0.0                          0.0                    0.0                              0.0                      0.0
    Sanjiv R. Das 001:00090                                          0.0                        0.0                          0.0                    0.0                              0.0                      0.0


* **AnalysisUnit.CTRY**

Smoke tests:
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CTRY)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
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
    COLUMNS        CHN 046:01426  GBR 026:01562  AUS 024:01072  USA 021:00494  DEU 014:00785  ITA 012:00116
    ROWS
    CHN 046:01426          0.000          0.059          0.053          0.023          0.109          0.087
    GBR 026:01562          0.059          0.000          0.077          0.037          0.146          0.119
    AUS 024:01072          0.053          0.077          0.000          0.026          0.155          0.128
    USA 021:00494          0.023          0.037          0.026          0.000          0.044          0.024
    DEU 014:00785          0.109          0.146          0.155          0.044          0.000          0.185
    ITA 012:00116          0.087          0.119          0.128          0.024          0.185          0.000



* **AnalysisUnit.ORG**

Smoke tests:
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.ORG)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
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
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                      JIANGSU NORM UNIV 004:00008  R RD UNIV 003:00024  UNIV MACAU 003:00019  MONASH UNIV 003:00006
    ROWS
    JIANGSU NORM UNIV 004:00008                     0.000000                  0.0              0.583333               0.083333
    R RD UNIV 003:00024                             0.000000                  0.0              0.000000               0.000000
    UNIV MACAU 003:00019                            0.583333                  0.0              0.000000               0.000000
    MONASH UNIV 003:00006                           0.083333                  0.0              0.000000               0.000000



* **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.SRC)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
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
    COLUMNS                              EUR BUS ORGAN LAW REV 005:00506  J BANK REGUL 005:00094  J FINANC REGUL COMPLIANCE 005:00014  J FINANC REGUL 004:00298  J TECHNOL 004:00110  J MONEY LAUND CONTROL 003:00040
    ROWS
    EUR BUS ORGAN LAW REV 005:00506                                0.000                    0.80                                0.360                     1.400                0.150                            0.267
    J BANK REGUL 005:00094                                         0.800                    0.00                                0.640                     0.650                0.100                            0.400
    J FINANC REGUL COMPLIANCE 005:00014                            0.360                    0.64                                0.000                     0.600                0.700                            0.467
    J FINANC REGUL 004:00298                                       1.400                    0.65                                0.600                     0.000                0.625                            0.500
    J TECHNOL 004:00110                                            0.150                    0.10                                0.700                     0.625                0.000                            0.250
    J MONEY LAUND CONTROL 003:00040                                0.267                    0.40                                0.467                     0.500                0.250                            0.000




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
        direct_matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )

        direct_matrix.columns.name = "COLUMNS"
        direct_matrix.index.name = "ROWS"

        return direct_matrix
