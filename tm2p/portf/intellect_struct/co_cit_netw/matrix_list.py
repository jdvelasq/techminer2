"""
MatrixList
===============================================================================

* **CITED_REF**


Smoke tests:
    >>> from tm2p.enum import AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.co_citation_network import MatrixList
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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                               ROWS                                       COLUMNS  OCC
    0      Anagnostopoulos I, 2018, J ECON BUS 31:0         Arner DW, 2017, NW J INT LAW BUS 50:0   20
    1         Arner DW, 2017, NW J INT LAW BUS 50:0      Anagnostopoulos I, 2018, J ECON BUS 31:0   20
    2         Arner DW, 2017, NW J INT LAW BUS 50:0     Butler T, 2019, PALGR ST DIG BUS ENA 21:0   16
    3     Butler T, 2019, PALGR ST DIG BUS ENA 21:0         Arner DW, 2017, NW J INT LAW BUS 50:0   16
    4         Arner DW, 2017, NW J INT LAW BUS 50:0        Kavassalis P, 2018, J RISK FINANC 13:0   13
    5        Kavassalis P, 2018, J RISK FINANC 13:0         Arner DW, 2017, NW J INT LAW BUS 50:0   13
    6  Arner DW, 2015, SSRN Electronic Journal 15:0         Arner DW, 2017, NW J INT LAW BUS 50:0   12
    7         Arner DW, 2017, NW J INT LAW BUS 50:0  Arner DW, 2015, SSRN Electronic Journal 15:0   12
    8         Arner DW, 2017, NW J INT LAW BUS 50:0              Baxter LG, 2016, DUKE LAW J 14:0   12
    9              Baxter LG, 2016, DUKE LAW J 14:0         Arner DW, 2017, NW J INT LAW BUS 50:0   12



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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                          ROWS                                  COLUMNS  OCC
    0      Anagnostopoulos I, 2018, J ECON BUS         Arner DW, 2017, NW J INT LAW BUS   20
    1         Arner DW, 2017, NW J INT LAW BUS      Anagnostopoulos I, 2018, J ECON BUS   20
    2         Arner DW, 2017, NW J INT LAW BUS     Butler T, 2019, PALGR ST DIG BUS ENA   16
    3     Butler T, 2019, PALGR ST DIG BUS ENA         Arner DW, 2017, NW J INT LAW BUS   16
    4         Arner DW, 2017, NW J INT LAW BUS        Kavassalis P, 2018, J RISK FINANC   13
    5        Kavassalis P, 2018, J RISK FINANC         Arner DW, 2017, NW J INT LAW BUS   13
    6  Arner DW, 2015, SSRN Electronic Journal         Arner DW, 2017, NW J INT LAW BUS   12
    7         Arner DW, 2017, NW J INT LAW BUS  Arner DW, 2015, SSRN Electronic Journal   12
    8         Arner DW, 2017, NW J INT LAW BUS              Baxter LG, 2016, DUKE LAW J   12
    9              Baxter LG, 2016, DUKE LAW J         Arner DW, 2017, NW J INT LAW BUS   12


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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                         ROWS                 COLUMNS  OCC
    0           Arner DW 61:0           Butler T 25:0   21
    1           Butler T 25:0           Arner DW 61:0   21
    2  Anagnostopoulos I 31:0           Arner DW 61:0   20
    3           Arner DW 61:0  Anagnostopoulos I 31:0   20
    4           Arner DW 61:0        Zetzsche DA 21:0   17
    5        Zetzsche DA 21:0           Arner DW 61:0   17
    6           Arner DW 61:0         Buckley RP 17:0   15
    7         Buckley RP 17:0           Arner DW 61:0   15
    8           Arner DW 61:0       Kavassalis P 14:0   14
    9       Kavassalis P 14:0           Arner DW 61:0   14


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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                               ROWS                       COLUMNS  OCC
    0         NW J INT LAW BUS 52:0  SSRN Electronic Journal 52:0   25
    1  SSRN Electronic Journal 52:0         NW J INT LAW BUS 52:0   25
    2               J ECON BUS 37:0         NW J INT LAW BUS 52:0   24
    3         NW J INT LAW BUS 52:0               J ECON BUS 37:0   24
    4            J FINANC ECON 31:0          REV FINANC STUD 33:0   21
    5          REV FINANC STUD 33:0            J FINANC ECON 31:0   21
    6             J BANK REGUL 29:0         NW J INT LAW BUS 52:0   20
    7         NW J INT LAW BUS 52:0             J BANK REGUL 29:0   20
    8     EUR BUS ORGAN LAW RE 26:0         NW J INT LAW BUS 52:0   19
    9                 J FINANC 29:0            J FINANC ECON 31:0   19


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import AnalysisUnit, Field

GCR = Field.GCR_WOS_FORMAT.value
ROWS = "ROWS"
COLUMNS = "COLUMNS"
OCC = "OCC"


def _extract_cited_auth(x):
    authors = [ref.strip().split(", ")[0].strip() for ref in x]
    authors = sorted(set(author for author in authors if author != "[Anonymous]"))
    return authors


def _extract_cited_src(x):
    refs = [ref for ref in x if len(ref.split(", ")) >= 3]
    sources = sorted(set(ref.strip().split(", ")[2].strip() for ref in refs))
    return sources


def _extract_cited_doc(x):
    docs = sorted(set(", ".join(ref.strip().split(", ")[:3]).strip() for ref in x))
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

        return df
