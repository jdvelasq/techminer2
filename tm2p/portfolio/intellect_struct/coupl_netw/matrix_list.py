"""
MatrixList
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.intellect_struct.coupl_netw import MatrixList
    >>> df = (
    ...     MatrixList()
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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                            ROWS                    COLUMNS  OCC
    0   von Solms J 2021 1:00027  von Solms J 2021a 1:00002   52
    1  von Solms J 2021a 1:00002   von Solms J 2021 1:00027   52
    2   El Khoury R 2025 1:00004      Grassi L 2022 1:00024   24
    3      Grassi L 2022 1:00024   El Khoury R 2025 1:00004   24
    4  Bagherifam N 2025 1:00000   El Khoury R 2025 1:00004   19
    5   El Khoury R 2025 1:00004  Bagherifam N 2025 1:00000   19
    6      Arsyad I 2025 1:00005   Kharisma DB 2025 1:00000   17
    7   Kharisma DB 2025 1:00000      Arsyad I 2025 1:00005   17
    8     Sangwan V 2019 1:00082      Takeda A 2021 1:00066   17
    9      Takeda A 2021 1:00066     Sangwan V 2019 1:00082   17


* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     MatrixList()
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
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                    ROWS                            COLUMNS  OCC
    0          Johan von Solms 002:00029          Johan von Solms 002:00029  104
    1        Andrea Miglionico 002:00011         Saule T. Omarova 001:00065    5
    2         Saule T. Omarova 001:00065        Andrea Miglionico 002:00011    5
    3        Andrea Miglionico 002:00011  Ioannis Anagnostopoulos 002:00284    4
    4  Ioannis Anagnostopoulos 002:00284        Andrea Miglionico 002:00011    4
    5    Joseph Jye-Cherng Lyu 002:00003    Joseph Jye-Cherng Lyu 002:00003    4
    6        Andrea Miglionico 002:00011          Johan von Solms 002:00029    2
    7        Andrea Miglionico 002:00011               Joseph Lee 001:00042    2
    8  Ioannis Anagnostopoulos 002:00284          Johan von Solms 002:00029    2
    9          Johan von Solms 002:00029        Andrea Miglionico 002:00011    2



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.helpers.get_zero_digit import get_zero_digits
from tm2p.enum import AnalysisUnit, Field
from tm2p.portfolio.perform_metr.unit.metr import Metrics

GCR = Field.GCR_WOS_FORMAT.value
DOC = Field.REC_SHORT_NAME.value
GCS = Field.GCS.value


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.use_counters
        self.params.use_counters = True

        matrix_list = self._compute_document_bibliographic_coupling()

        def remove_counters(matrix_list):
            if use_counters is False:
                self.params.use_counters = False
                matrix_list["ROWS"] = matrix_list["ROWS"].apply(
                    lambda x: " ".join(x.split(" ")[:-1])
                )
                matrix_list["COLUMNS"] = matrix_list["COLUMNS"].apply(
                    lambda x: " ".join(x.split(" ")[:-1])
                )
            return matrix_list

        if self.params.analysis_unit == AnalysisUnit.DOC:
            matrix_list = remove_counters(matrix_list)
            return matrix_list

        matrix_list = self._expand_matrix_list(matrix_list)
        matrix_list = remove_counters(matrix_list)
        return matrix_list

    def _compute_document_bibliographic_coupling(self):

        df = load_filtered_main_csv_zip(params=self.params)
        df = df.dropna(subset=[GCR])

        #
        _, gcs_digits = get_zero_digits(root_directory=self.params.root_directory)
        fmt = "{} 1:{:0" + str(gcs_digits) + "d}"
        df[DOC] = [fmt.format(row[DOC], row[GCS]) for _, row in df.iterrows()]
        #

        df = df[[DOC, GCR]]

        df[GCR] = df[GCR].str.split("; ")
        df = df.explode(GCR)
        df[GCR] = df[GCR].str.strip()

        df = df.groupby([GCR], as_index=True).agg({DOC: list})
        df = df.loc[df[DOC].apply(len) > 1, :]

        rows = []
        columns = []
        values = []

        for _, data in df.iterrows():

            docs = data[DOC]
            for i, doc1 in enumerate(docs):
                for j, doc2 in enumerate(docs):

                    if i < j:

                        rows.append(doc1)
                        columns.append(doc2)
                        values.append(1)

                        rows.append(doc2)
                        columns.append(doc1)
                        values.append(1)

        matrix_list = pd.DataFrame(
            {
                "ROWS": rows,
                "COLUMNS": columns,
                "OCC": values,
            }
        )

        matrix_list = matrix_list.groupby(["ROWS", "COLUMNS"], as_index=False).agg(
            {"OCC": "sum"}
        )

        matrix_list = matrix_list.sort_values(
            ["OCC", "ROWS", "COLUMNS"], ascending=[False, True, True]
        )

        matrix_list = matrix_list.reset_index(drop=True)

        return matrix_list

    def _expand_matrix_list(self, matrix_list):

        # remove counters
        matrix_list = matrix_list.copy()
        matrix_list["ROWS"] = matrix_list["ROWS"].apply(
            lambda x: " ".join(x.split(" ")[:-1])
        )
        matrix_list["COLUMNS"] = matrix_list["COLUMNS"].apply(
            lambda x: " ".join(x.split(" ")[:-1])
        )
        #

        coupling_unit = self.params.analysis_unit

        df = load_filtered_main_csv_zip(params=self.params)
        mapping = dict(zip(df[DOC].to_list(), df[coupling_unit.value].to_list()))

        matrix_list["ROWS"] = matrix_list["ROWS"].map(mapping)
        matrix_list["COLUMNS"] = matrix_list["COLUMNS"].map(mapping)

        if coupling_unit == AnalysisUnit.AUTH:
            source_field = Field.AUTH_FULL_NAME
        elif coupling_unit == AnalysisUnit.CTRY:
            source_field = Field.CTRY_ISO3
        elif coupling_unit == AnalysisUnit.ORG:
            source_field = Field.ORG
        elif coupling_unit == AnalysisUnit.SRC:
            source_field = Field.SRC_ISO4
        else:
            raise ValueError("Invalid coupling unit")

        items = (
            Metrics()
            .update(**self.params.__dict__)
            .with_source_field(source_field)
            .run()
        )

        matrix_list = matrix_list.loc[
            matrix_list["ROWS"].isin(items.index.to_list()), :
        ]
        matrix_list = matrix_list.loc[
            matrix_list["COLUMNS"].isin(items.index.to_list()), :
        ]

        # add counters
        mapping = dict(zip(items.index.to_list(), items["COUNTERS"].to_list()))
        matrix_list["ROWS"] = matrix_list["ROWS"].map(mapping)
        matrix_list["COLUMNS"] = matrix_list["COLUMNS"].map(mapping)
        #

        matrix_list = matrix_list.groupby(["ROWS", "COLUMNS"], as_index=False).agg(
            {"OCC": "sum"}
        )

        matrix_list = matrix_list.loc[
            matrix_list["ROWS"].map(lambda x: not x.startswith("[UNKNOWN]"))
        ]
        matrix_list = matrix_list.loc[
            matrix_list["COLUMNS"].map(lambda x: not x.startswith("[UNKNOWN]"))
        ]

        matrix_list = matrix_list.sort_values(
            ["OCC", "ROWS", "COLUMNS"], ascending=[False, True, True]
        )
        matrix_list = matrix_list.reset_index(drop=True)
        return matrix_list
