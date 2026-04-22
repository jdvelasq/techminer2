"""
Matrix
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import Matrix
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
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

* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     Matrix()
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




"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .mtx_list import MatrixList


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
            return int(occ), int(gcs), x

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
