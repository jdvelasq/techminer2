"""
Matrix
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CitationUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import Matrix
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
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
    >>> df.shape
    (109, 109)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE
                                    Arner DW 2020 1:00338  ...  Omarova ST 2020 1:00065
    Arner DW 2020 1:00338                               1  ...                        0
    Anagnostopoulos I 2018 1:00284                      0  ...                        0
    Zetzsche DA 2020 1:00222                            0  ...                        1
    Mirza N 2023 1:00112                                0  ...                        0
    Muganyi T 2022 1:00109                              0  ...                        0
    Lui A 2018 1:00096                                  0  ...                        0
    Das SR 2019 1:00090                                 0  ...                        0
    Sangwan V 2019 1:00082                              0  ...                        0
    Takeda A 2021 1:00066                               0  ...                        0
    Omarova ST 2020 1:00065                             0  ...                        1
    <BLANKLINE>
    [10 rows x 10 columns]

* **CitationUnit.AUTH**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
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
    >>> df.shape
    (27, 27)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE
                                 Dirk A. Zetzsche 008:00699  ...  Sherin Kunhibava 002:00016
    Dirk A. Zetzsche 008:00699                            8  ...                           1
    Ross P. Buckley 007:00887                             1  ...                           1
    Douglas W. Arner 007:00887                            1  ...                           1
    Yufei Xia 004:00008                                   2  ...                           0
    Johan von Solms 002:00029                             0  ...                           0
    Jinying Li 002:00019                                  0  ...                           0
    Ananda Maiti 002:00019                                0  ...                           0
    Michael Becker 002:00017                              0  ...                           1
    Zakariya Mustapha 002:00016                           1  ...                           0
    Sherin Kunhibava 002:00016                            1  ...                           2
    <BLANKLINE>
    [10 rows x 10 columns]


* **CitationUnit.CTRY**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
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
    >>> df.shape
    (24, 24)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE
                   CHN 046:01426  GBR 026:01562  ...  IND 009:00128  CAN 008:00054
    CHN 046:01426             46              4  ...             10              0
    GBR 026:01562              4             26  ...              4              0
    AUS 024:01072              4              2  ...              2              1
    USA 021:00494             10              4  ...              1              0
    DEU 014:00785              1              1  ...              8              0
    ITA 012:00116              5              4  ...              2              0
    LUX 009:00703              1              4  ...              5              0
    FRA 009:00232              1              2  ...              4              0
    IND 009:00128             10              4  ...              9              0
    CAN 008:00054              0              0  ...              0              8
    <BLANKLINE>
    [10 rows x 10 columns]


* **CitationUnit.ORG**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
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
    >>> df.shape
    (17, 17)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE
                                            UNIV HONG KONG 008:00903  ...  GOETHE UNIV FRANKF 002:00027
    UNIV HONG KONG 008:00903                                       8  ...                             0
    UNIV LUXEMBG 008:00699                                         1  ...                             0
    HEINRICH HEINE UNIV 004:00642                                  1  ...                             0
    JIANGSU NORM UNIV 004:00008                                    2  ...                             2
    UNIV MACAU 003:00019                                           0  ...                             0
    MONASH UNIV 003:00006                                          0  ...                             0
    LEBAN AMER UNIV 002:00116                                      3  ...                             1
    HARV UNIV 002:00046                                            0  ...                             0
    SOUTHWEST UNIV FINANC & ECON 002:00031                         0  ...                             0
    GOETHE UNIV FRANKF 002:00027                                   0  ...                             2
    <BLANKLINE>
    [10 rows x 10 columns]



* **CitationUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_citation_unit(CitationUnit.SRC)
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
    >>> df.shape
    (16, 16)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE
                                         EUR BUS ORGAN LAW REV 005:00506  ...  LAW FINANC MARK REV 002:00009
    EUR BUS ORGAN LAW REV 005:00506                                    5  ...                              1
    J BANK REGUL 005:00094                                             1  ...                              0
    J FINANC REGUL COMPLIANCE 005:00014                                1  ...                              0
    J FINANC REGUL 004:00298                                           0  ...                              1
    J TECHNOL 004:00110                                                0  ...                              0
    J MONEY LAUND CONTROL 003:00040                                    0  ...                              0
    INT REV FINANC ANAL 002:00030                                      0  ...                              0
    FUTUR INTERNET 002:00019                                           0  ...                              0
    INT J LAW MANAG 002:00012                                          0  ...                              0
    LAW FINANC MARK REV 002:00009                                      1  ...                              2
    <BLANKLINE>
    [10 rows x 10 columns]


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
            set(matrix_list["CITING_UNIT"].to_list()).union(
                set(matrix_list["CITED_UNIT"].to_list())
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
            citing_unit = row["CITING_UNIT"]
            cited_unit = row["CITED_UNIT"]
            occ = row["OCC"]
            df.loc[citing_unit, cited_unit] = occ
            df.loc[cited_unit, citing_unit] = occ

        for col in df.columns:
            counters = col.split(" ")[-1]
            occ = counters.split(":")[0]
            df.loc[col, col] = int(occ)

        return df
