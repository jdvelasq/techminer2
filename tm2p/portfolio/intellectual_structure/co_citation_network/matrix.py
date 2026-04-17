"""
Matrix
===============================================================================

* **CITED_REF**


Smoke tests:
    >>> from tm2p.enum import CoCitationUnit
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(CoCitationUnit.CITED_REF)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                                     Williams JW, 2013, ACCOUNT ORG SOC 9:0  Kurum E, 2023, Journal of Financial Crime 9:0  Becker M, 2020, INTELL SYST ACCOUNT 9:0  Yang D, 2018, EMERG MARK FINANC TR 8:0  Turki M, 2020, HELIYON 8:0  PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review 8:0
    ROWS
    Williams JW, 2013, ACCOUNT ORG SOC 9:0                                                           9                                              2                                        1                                       2                           0                                                           2
    Kurum E, 2023, Journal of Financial Crime 9:0                                                    2                                              9                                        5                                       4                           5                                                           4
    Becker M, 2020, INTELL SYST ACCOUNT 9:0                                                          1                                              5                                        9                                       4                           3                                                           3
    Yang D, 2018, EMERG MARK FINANC TR 8:0                                                           2                                              4                                        4                                       8                           3                                                           3
    Turki M, 2020, HELIYON 8:0                                                                       0                                              5                                        3                                       3                           8                                                           2
    PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review 8:0                                       2                                              4                                        3                                       3                           2                                                           8


    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.iloc[:6, :6].to_string())  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                                 Williams JW, 2013, ACCOUNT ORG SOC  Kurum E, 2023, Journal of Financial Crime  Becker M, 2020, INTELL SYST ACCOUNT  Yang D, 2018, EMERG MARK FINANC TR  Turki M, 2020, HELIYON  PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review
    ROWS
    Williams JW, 2013, ACCOUNT ORG SOC                                                       9                                          2                                    1                                   2                       0                                                       2
    Kurum E, 2023, Journal of Financial Crime                                                2                                          9                                    5                                   4                       5                                                       4
    Becker M, 2020, INTELL SYST ACCOUNT                                                      1                                          5                                    9                                   4                       3                                                       3
    Yang D, 2018, EMERG MARK FINANC TR                                                       2                                          4                                    4                                   8                       3                                                       3
    Turki M, 2020, HELIYON                                                                   0                                          5                                    3                                   3                       8                                                       2
    PACKIN Nizan Geslevich., 2018, Chicago-Kent Law Review                                   2                                          4                                    3                                   3                       2                                                       8


* **CITED_AUTH**

Smoke tests:

    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_AUTH)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    COLUMNS          Williams JW 9:0  Magnuson W 9:0  Kurum E 9:0  Brummer C 9:0  Yeung K 8:0  Yang D 8:0
    ROWS
    Williams JW 9:0                9               0            2              0            1           2
    Magnuson W 9:0                 0               9            0              4            0           1
    Kurum E 9:0                    2               0            9              0            0           4
    Brummer C 9:0                  0               4            0              9            0           0
    Yeung K 8:0                    1               0            0              0            8           0
    Yang D 8:0                     2               1            4              0            0           8


* **CITED_SRC**

Smoke tests:
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_SRC)
    ...     #
    ...     .having_cited_items_in_top(50)
    ...     .having_minimum_cited_unit_occurrences(0)
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
    COLUMNS                       SSRN Electronic Journal 52:0  NW J INT LAW BUS 52:0  J ECON BUS 37:0  REV FINANC STUD 33:0  TECHNOL FORECAST SOC 32:0  J FINANC ECON 31:0
    ROWS
    SSRN Electronic Journal 52:0                            52                     25               11                    13                         10                  10
    NW J INT LAW BUS 52:0                                   25                     52               24                    11                          7                  11
    J ECON BUS 37:0                                         11                     24               37                     9                         10                   9
    REV FINANC STUD 33:0                                    13                     11                9                    33                          9                  21
    TECHNOL FORECAST SOC 32:0                               10                      7               10                     9                         32                  10
    J FINANC ECON 31:0                                      10                     11                9                    21                         10                  31


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .matrix_list import MatrixList


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix_list = (
            MatrixList().update(**self.params.__dict__).using_counters(True).run()
        )

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

        if self.params.use_counters is False:
            df.columns = [" ".join(col.split(" ")[:-1]) for col in df.columns]
            df.index = [" ".join(idx.split(" ")[:-1]) for idx in df.index]

        df.columns.name = "COLUMNS"
        df.index.name = "ROWS"

        return df
