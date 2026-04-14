"""
Matrix
===============================================================================

* **CouplingUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit, ItemOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                    Arner DW 2020 1:00338  Anagnostopoulos I 2018 1:00284  Demirel P 2019 1:00279  Arner DW 2017 1:00242  Zetzsche DA 2020 1:00222  Mirza N 2023 1:00112
    Arner DW 2020 1:00338                               1                               4                       0                      4                         2                     1
    Anagnostopoulos I 2018 1:00284                      4                               1                       0                      4                         1                     1
    Demirel P 2019 1:00279                              0                               0                       1                      0                         0                     0
    Arner DW 2017 1:00242                               4                               4                       0                      1                         1                     0
    Zetzsche DA 2020 1:00222                            2                               1                       0                      1                         1                     1
    Mirza N 2023 1:00112                                1                               1                       0                      0                         1                     1


* **CouplingUnit.AUTH**

Smoke tests:
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     #
    ...     .having_items_in_top(100)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                       Ioannis Anagnostopoulos 002:00284  Johan von Solms 002:00029  Andrea Miglionico 002:00011  Nir Kshetri 002:00006  Joseph Jye-Cherng Lyu 002:00003  Sanjiv R. Das 001:00090
    Ioannis Anagnostopoulos 002:00284                                  2                          2                            4                      0                                0                        0
    Johan von Solms 002:00029                                          2                          2                            2                      2                                0                        0
    Andrea Miglionico 002:00011                                        4                          2                            2                      0                                0                        0
    Nir Kshetri 002:00006                                              0                          2                            0                      2                                0                        0
    Joseph Jye-Cherng Lyu 002:00003                                    0                          0                            0                      0                                2                        0
    Sanjiv R. Das 001:00090                                            0                          0                            0                      0                                0                        1


* **CouplingUnit.CTRY**

Smoke tests:
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                   CHN 046:01426  GBR 026:01562  AUS 024:01072  USA 021:00494  DEU 014:00785  ITA 012:00116
    CHN 046:01426             46             71             59             22             70             48
    GBR 026:01562             71             26             48             20             53             37
    AUS 024:01072             59             48             24             13             52             37
    USA 021:00494             22             20             13             21             13              6
    DEU 014:00785             70             53             52             13             14             31
    ITA 012:00116             48             37             37              6             31             12


* **CouplingUnit.ORG**

Smoke tests:
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.ORG)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                 JIANGSU NORM UNIV 004:00008  R RD UNIV 003:00024  UNIV MACAU 003:00019  MONASH UNIV 003:00006
    JIANGSU NORM UNIV 004:00008                            4                    0                     7                      1
    R RD UNIV 003:00024                                    0                    3                     0                      0
    UNIV MACAU 003:00019                                   7                    0                     3                      0
    MONASH UNIV 003:00006                                  1                    0                     0                      3


* **CouplingUnit.SRC**

Smoke tests:
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.SRC)
    ...     #
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
                                         EUR BUS ORGAN LAW REV 005:00506  J BANK REGUL 005:00094  J FINANC REGUL COMPLIANCE 005:00014  J FINANC REGUL 004:00298  J TECHNOL 004:00110  J MONEY LAUND CONTROL 003:00040
    EUR BUS ORGAN LAW REV 005:00506                                    5                      20                                    9                        28                    3                                4
    J BANK REGUL 005:00094                                            20                       5                                   16                        13                    2                                6
    J FINANC REGUL COMPLIANCE 005:00014                                9                      16                                    5                        12                   14                                7
    J FINANC REGUL 004:00298                                          28                      13                                   12                         4                   10                                6
    J TECHNOL 004:00110                                                3                       2                                   14                        10                    4                                3
    J MONEY LAUND CONTROL 003:00040                                    4                       6                                    7                         6                    3                                3



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
            return occ, gcs, x

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
