"""
MatrixList
===============================================================================

* **CITED_REF**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw import MatrixList  # type: ignore
    >>> df = (
    ...     MatrixList()
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
    >>> type(df).__name__
    'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                       ROWS                                               COLUMNS  OCC
    0  Forrester JayWright., 2013, Industrial dynamics 74:0            Sterman J.D., 2000, BUSINESS DYNAMICS 70:0   26
    1            Sterman J.D., 2000, BUSINESS DYNAMICS 70:0  Forrester JayWright., 2013, Industrial dynamics 74:0   26
    2             Forrester J.W., 1969, URBAN DYNAMICS 15:0  Forrester JayWright., 2013, Industrial dynamics 74:0   11
    3             Forrester Jay., 1971, World dynamics 17:0  Forrester JayWright., 2013, Industrial dynamics 74:0   11
    4  Forrester JayWright., 2013, Industrial dynamics 74:0             Forrester J.W., 1969, URBAN DYNAMICS 15:0   11
    5  Forrester JayWright., 2013, Industrial dynamics 74:0             Forrester Jay., 1971, World dynamics 17:0   11
    6  Forrester JayWright., 2013, Industrial dynamics 74:0   Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0   10
    7   Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY 30:0  Forrester JayWright., 2013, Industrial dynamics 74:0   10
    8  Forrester JayWright., 2013, Industrial dynamics 74:0                     STERMAN JD, 1989, MANAGE SCI 12:0    9
    9                     STERMAN JD, 1989, MANAGE SCI 12:0  Forrester JayWright., 2013, Industrial dynamics 74:0    9



    >>> df = (
    ...     MatrixList()
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
    >>> type(df).__name__
    'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                  ROWS                                          COLUMNS  OCC
    0  Forrester JayWright., 2013, Industrial dynamics            Sterman J.D., 2000, BUSINESS DYNAMICS   26
    1            Sterman J.D., 2000, BUSINESS DYNAMICS  Forrester JayWright., 2013, Industrial dynamics   26
    2             Forrester J.W., 1969, URBAN DYNAMICS  Forrester JayWright., 2013, Industrial dynamics   11
    3             Forrester Jay., 1971, World dynamics  Forrester JayWright., 2013, Industrial dynamics   11
    4  Forrester JayWright., 2013, Industrial dynamics             Forrester J.W., 1969, URBAN DYNAMICS   11
    5  Forrester JayWright., 2013, Industrial dynamics             Forrester Jay., 1971, World dynamics   11
    6  Forrester JayWright., 2013, Industrial dynamics   Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY   10
    7   Sterman J.D. J. D., 2000, BUSINESS DYNAMICS SY  Forrester JayWright., 2013, Industrial dynamics   10
    8  Forrester JayWright., 2013, Industrial dynamics                     STERMAN JD, 1989, MANAGE SCI    9
    9                     STERMAN JD, 1989, MANAGE SCI  Forrester JayWright., 2013, Industrial dynamics    9


* **CITED_AUTH**

Smoke tests:
    >>> df = (
    ...     MatrixList()
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
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                            ROWS                    COLUMNS  OCC
    0  Forrester JayWright. 74:0          Sterman J.D. 81:0   26
    1          Sterman J.D. 81:0  Forrester JayWright. 74:0   26
    2        Forrester J.W. 51:0  Forrester JayWright. 74:0   20
    3  Forrester JayWright. 74:0        Forrester J.W. 51:0   20
    4          FORRESTER JW 56:0          Sterman J.D. 81:0   15
    5          Sterman J.D. 81:0          FORRESTER JW 56:0   15
    6          FORRESTER JW 56:0  Forrester JayWright. 74:0   14
    7  Forrester JayWright. 74:0          FORRESTER JW 56:0   14
    8          FORRESTER JW 56:0        Forrester J.W. 51:0   11
    9        Forrester J.W. 51:0          FORRESTER JW 56:0   11


* **CITED_SRC**

Smoke tests:
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_SRC)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(1)
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
    >>> type(df).__name__
    'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                             ROWS                     COLUMNS  OCC
    0          J CLEAN PROD 142:0  SUSTAINABILITY-BASEL 103:0   64
    1  SUSTAINABILITY-BASEL 103:0          J CLEAN PROD 142:0   64
    2          J CLEAN PROD 142:0    RESOUR CONSERV RECY 78:0   56
    3    RESOUR CONSERV RECY 78:0          J CLEAN PROD 142:0   56
    4          J CLEAN PROD 142:0   RENEW SUST ENERG REV 80:0   51
    5   RENEW SUST ENERG REV 80:0          J CLEAN PROD 142:0   51
    6          J CLEAN PROD 142:0      SCI TOTAL ENVIRON 87:0   45
    7      SCI TOTAL ENVIRON 87:0          J CLEAN PROD 142:0   45
    8           ENERG POLICY 70:0          J CLEAN PROD 142:0   42
    9          J CLEAN PROD 142:0           ENERG POLICY 70:0   42


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import AnalysisUnit, Field

GCR = Field.GCR_WOS_FORMAT.value
ROWS = "ROWS"
COLUMNS = "COLUMNS"
OCC = "OCC"


def _extract_cited_auth(refs):
    refs = [ref for ref in refs if len(ref.split(", ")) >= 3]
    authors = [ref.strip().split(", ")[0].strip() for ref in refs]
    authors = sorted(set(author for author in authors if author != "[Anonymous]"))
    return authors


def _extract_cited_src(refs):
    refs = [ref for ref in refs if len(ref.split(", ")) >= 3]
    sources = sorted(set(ref.strip().split(", ")[2].strip() for ref in refs))
    return sources


def _extract_cited_doc(refs):
    refs = [ref for ref in refs if len(ref.split(", ")) >= 3]
    docs = sorted(set(", ".join(ref.strip().split(", ")[:3]).strip() for ref in refs))
    return docs


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = self._load_and_prepare_references()
        df = self._transform_refs_to_cited_units(df)
        counts = self._get_counts(df)
        filtered_df = self._filter_df(df, counts)
        matrix_list = self._build_matrix_list(filtered_df)
        matrix_list = self._add_counters(matrix_list, counts)

        return matrix_list

    def _add_counters(self, matrix_list, counts):

        if not self.params.use_counters:
            return matrix_list

        mapping = dict(
            zip(
                counts.index.tolist(),
                [f"{item} {count}:0" for item, count in counts.items()],
            )
        )

        matrix_list["ROWS"] = matrix_list["ROWS"].map(mapping)
        matrix_list["COLUMNS"] = matrix_list["COLUMNS"].map(mapping)

        return matrix_list

    def _build_matrix_list(self, df):

        rows = []
        columns = []
        occ = []

        for _, row in df.iterrows():

            references = row[GCR]

            for i, ref_i in enumerate(references):
                for j, ref_j in enumerate(references):

                    if i < j:

                        ref_i = ref_i.strip()
                        ref_j = ref_j.strip()

                        rows.append(ref_i)
                        columns.append(ref_j)
                        occ.append(1)

                        rows.append(ref_j)
                        columns.append(ref_i)
                        occ.append(1)

        raw_df = pd.DataFrame({ROWS: rows, COLUMNS: columns, OCC: occ})

        df = raw_df.groupby([ROWS, COLUMNS], as_index=False).aggregate({"OCC": "sum"})
        df = df.sort_values([OCC, ROWS, COLUMNS], ascending=[False, True, True])

        df = df.reset_index(drop=True)

        return df

    def _filter_df(self, df, counts):

        valid_units = set(counts.index.tolist())

        df = df.copy()
        df[GCR] = df[GCR].apply(
            lambda refs: [ref for ref in refs if ref in valid_units]
        )
        df = df.loc[df[GCR].map(len) >= 2, :]

        return df

    def _get_counts(self, df):

        df = df.copy()
        df = df.explode(GCR)  # type: ignore
        df[GCR] = df[GCR].str.strip()
        counts = df[GCR].value_counts()
        counts = counts.loc[counts >= self.params.minimum_cited_unit_occurrences]
        counts = counts.head(self.params.top_n_cited_units)
        return counts

    def _transform_refs_to_cited_units(self, df):

        if self.params.analysis_unit == AnalysisUnit.CITED_AUTH:
            df[GCR] = df[GCR].apply(_extract_cited_auth)
        elif self.params.analysis_unit == AnalysisUnit.CITED_SRC:
            df[GCR] = df[GCR].apply(_extract_cited_src)
        elif self.params.analysis_unit == AnalysisUnit.CITED_REF:
            df[GCR] = df[GCR].apply(_extract_cited_doc)
        else:
            raise ValueError("Bad analysis unit")

        return df

    def _load_and_prepare_references(self):

        df = load_filtered_main_csv_zip(params=self.params)
        df = df[[GCR]]
        df = df.dropna()
        df[GCR] = df[GCR].str.split("; ")
        df[GCR] = df[GCR].map(lambda x: [ref.strip() for ref in x])
        df[GCR] = df[GCR].map(lambda x: [ref.strip() for ref in x])

        return df
