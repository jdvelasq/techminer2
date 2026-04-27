"""
Matrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.intellect_struct.coupl_netw import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COUPLING UNIT:
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
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                    Arner DW 2020 1:00338  Anagnostopoulos I 2018 1:00284  Demirel P 2019 1:00279  Arner DW 2017 1:00242  Zetzsche DA 2020 1:00222  Mirza N 2023 1:00112
    Arner DW 2020 1:00338                               1                               4                       0                      4                         2                     1
    Anagnostopoulos I 2018 1:00284                      4                               1                       0                      4                         1                     1
    Demirel P 2019 1:00279                              0                               0                       1                      0                         0                     0
    Arner DW 2017 1:00242                               4                               4                       0                      1                         1                     0
    Zetzsche DA 2020 1:00222                            2                               1                       0                      1                         1                     1
    Mirza N 2023 1:00112                                1                               1                       0                      0                         1                     1


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     Matrix()
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
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                       Ioannis Anagnostopoulos 002:00284  Johan von Solms 002:00029  Andrea Miglionico 002:00011  Nir Kshetri 002:00006  Joseph Jye-Cherng Lyu 002:00003  Sanjiv R. Das 001:00090
    Ioannis Anagnostopoulos 002:00284                                  2                          2                            4                      0                                0                        0
    Johan von Solms 002:00029                                          2                          2                            2                      2                                0                        0
    Andrea Miglionico 002:00011                                        4                          2                            2                      0                                0                        0
    Nir Kshetri 002:00006                                              0                          2                            0                      2                                0                        0
    Joseph Jye-Cherng Lyu 002:00003                                    0                          0                            0                      0                                2                        0
    Sanjiv R. Das 001:00090                                            0                          0                            0                      0                                0                        1




"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .matrix_list import MatrixList


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix_list = MatrixList().update(**self.params.__dict__).run()

        nodes = list(
            set(matrix_list["ROWS"].to_list()).union(
                set(matrix_list["COLUMNS"].to_list())
            )
        )

        def f(x):
            counters = x.split(" ")[-1]
            occ = counters.split(":")[0]
            gcs = counters.split(":")[1]
            return int(occ), int(gcs), x

        sorted_nodes = sorted(nodes, key=f, reverse=True)

        df = pd.DataFrame(0, index=sorted_nodes, columns=sorted_nodes)

        for _, row in matrix_list.iterrows():
            citing_unit = row["ROWS"]
            cited_unit = row["COLUMNS"]
            occ = row["OCC"]
            df.loc[citing_unit, cited_unit] = occ
            df.loc[cited_unit, citing_unit] = occ

        for col in df.columns:
            counters = col.split(" ")[-1]
            occ = counters.split(":")[0]
            df.loc[col, col] = int(occ)

        return df
