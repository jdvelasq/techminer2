"""
Matrix
===============================================================================

* **CITED_REF**


Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw import Matrix  # type: ignore
    >>> df = (
    ...     Matrix()
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
    COLUMNS                                               Forrester JayWright., 2013, Industrial dynamics 74:0  Sterman J.D., 2000, BUSINESS DYNAMICS 70:0  Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0  Barlas Y, 1996, SYST DYNAM REV 27:0  FORRESTER JW, 1958, HARVARD BUS REV 25:0  Swanson J, 2002, J OPER RES SOC 21:0
    ROWS
    Forrester JayWright., 2013, Industrial dynamics 74:0                                                    74                                          26                                                   10                                    7                                         8                                     3
    Sterman J.D., 2000, BUSINESS DYNAMICS 70:0                                                              26                                          70                                                    0                                    5                                         6                                     0
    Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0                                                     10                                           0                                                   30                                    5                                         0                                     0
    Barlas Y, 1996, SYST DYNAM REV 27:0                                                                      7                                           5                                                    5                                   27                                         1                                     2
    FORRESTER JW, 1958, HARVARD BUS REV 25:0                                                                 8                                           6                                                    0                                    1                                        25                                     1
    Swanson J, 2002, J OPER RES SOC 21:0                                                                     3                                           0                                                    0                                    2                                         1                                    21


    >>> df = (
    ...     Matrix()
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

* **CITED_AUTH**

Smoke tests:

    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_AUTH)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    COLUMNS               Sterman J.D.  Forrester JayWright.  FORRESTER JW  Forrester J.W.  Sterman JD  Sterman J.D. J. D.
    ROWS
    Sterman J.D.                    81                    26            15               8           6                   0
    Forrester JayWright.            26                    74            14              20           6                  10
    FORRESTER JW                    15                    14            56              11           4                   2
    Forrester J.W.                   8                    20            11              51           6                   8
    Sterman JD                       6                     6             4               6          31                   2
    Sterman J.D. J. D.               0                    10             2               8           2                  30


* **CITED_SRC**

Smoke tests:
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_SRC)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    COLUMNS               J CLEAN PROD  SYST DYNAM REV  EUR J OPER RES  SUSTAINABILITY-BASEL  SCI TOTAL ENVIRON  J ENVIRON MANAGE
    ROWS
    J CLEAN PROD                   142              29              38                    64                 45                39
    SYST DYNAM REV                  29             137              33                    21                 20                25
    EUR J OPER RES                  38              33             104                    23                 18                18
    SUSTAINABILITY-BASEL            64              21              23                   103                 34                27
    SCI TOTAL ENVIRON               45              20              18                    34                 87                38
    J ENVIRON MANAGE                39              25              18                    27                 38                86


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

        if self.params.use_counters is False:
            df.columns = [" ".join(col.split(" ")[:-1]) for col in df.columns]
            df.index = [" ".join(idx.split(" ")[:-1]) for idx in df.index]

        df.columns.name = "COLUMNS"
        df.index.name = "ROWS"

        return df
