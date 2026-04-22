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


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

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





"""

from tm2p._intern import ParamsMixin
from tm2p._intern.netw.norma_mtx import normalize_matrix

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
