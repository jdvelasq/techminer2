"""
MatrixList
===============================================================================

* **CouplingUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import CouplingUnit, ItemOrderBy
    >>> from tm2p.portfolio.intellectual_structure.coupling_network import MatrixList
    >>> df = (
    ...     MatrixList()
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


    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
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
                    ROWS            COLUMNS  OCC
    0   von Solms J 2021  von Solms J 2021a   52
    1  von Solms J 2021a   von Solms J 2021   52
    2   El Khoury R 2025      Grassi L 2022   24
    3      Grassi L 2022   El Khoury R 2025   24
    4  Bagherifam N 2025   El Khoury R 2025   19
    5   El Khoury R 2025  Bagherifam N 2025   19
    6      Arsyad I 2025   Kharisma DB 2025   17
    7   Kharisma DB 2025      Arsyad I 2025   17
    8     Sangwan V 2019      Takeda A 2021   17
    9      Takeda A 2021     Sangwan V 2019   17


* **CouplingUnit.AUTH**

Smoke tests:
    >>> df = (
    ...     MatrixList()
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


    >>> df = (
    ...     MatrixList()
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
                          ROWS                  COLUMNS  OCC
    0          Johan von Solms          Johan von Solms  104
    1        Andrea Miglionico         Saule T. Omarova    5
    2         Saule T. Omarova        Andrea Miglionico    5
    3        Andrea Miglionico  Ioannis Anagnostopoulos    4
    4  Ioannis Anagnostopoulos        Andrea Miglionico    4
    5    Joseph Jye-Cherng Lyu    Joseph Jye-Cherng Lyu    4
    6        Andrea Miglionico          Johan von Solms    2
    7        Andrea Miglionico               Joseph Lee    2
    8  Ioannis Anagnostopoulos          Johan von Solms    2
    9          Johan von Solms        Andrea Miglionico    2



* **CouplingUnit.CTRY**

Smoke tests:
    >>> df = (
    ...     MatrixList()
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
                ROWS        COLUMNS  OCC
    0  CHN 046:01426  CHN 046:01426  190
    1  GBR 026:01562  GBR 026:01562   84
    2  CHN 046:01426  GBR 026:01562   71
    3  GBR 026:01562  CHN 046:01426   71
    4  CHN 046:01426  DEU 014:00785   70
    5  DEU 014:00785  CHN 046:01426   70
    6  DEU 014:00785  DEU 014:00785   60
    7  AUS 024:01072  CHN 046:01426   59
    8  CHN 046:01426  AUS 024:01072   59
    9  DEU 014:00785  GBR 026:01562   53


* **CouplingUnit.ORG**

Smoke tests:
    >>> df = (
    ...     MatrixList()
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
                              ROWS                      COLUMNS  OCC
    0          R RD UNIV 003:00024          R RD UNIV 003:00024   14
    1  JIANGSU NORM UNIV 004:00008  JIANGSU NORM UNIV 004:00008    8
    2  JIANGSU NORM UNIV 004:00008         UNIV MACAU 003:00019    7
    3         UNIV MACAU 003:00019  JIANGSU NORM UNIV 004:00008    7
    4         UNIV MACAU 003:00019         UNIV MACAU 003:00019    4
    5  JIANGSU NORM UNIV 004:00008        MONASH UNIV 003:00006    1
    6        MONASH UNIV 003:00006  JIANGSU NORM UNIV 004:00008    1


* **CouplingUnit.SRC**

Smoke tests:
    >>> df = (
    ...     MatrixList()
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
                                      ROWS                              COLUMNS  OCC
    0               J BANK REGUL 005:00094               J BANK REGUL 005:00094  110
    1      EUR BUS ORGAN LAW REV 005:00506      EUR BUS ORGAN LAW REV 005:00506   28
    2      EUR BUS ORGAN LAW REV 005:00506             J FINANC REGUL 004:00298   28
    3             J FINANC REGUL 004:00298      EUR BUS ORGAN LAW REV 005:00506   28
    4             J FINANC REGUL 004:00298             J FINANC REGUL 004:00298   22
    5                  J TECHNOL 004:00110                  J TECHNOL 004:00110   22
    6      EUR BUS ORGAN LAW REV 005:00506               J BANK REGUL 005:00094   20
    7               J BANK REGUL 005:00094      EUR BUS ORGAN LAW REV 005:00506   20
    8               J BANK REGUL 005:00094  J FINANC REGUL COMPLIANCE 005:00014   16
    9  J FINANC REGUL COMPLIANCE 005:00014               J BANK REGUL 005:00094   16


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.helpers.get_zero_digits import get_zero_digits
from tm2p.enum import CouplingUnit, Field
from tm2p.portfolio.performance_metrics.item_metrics.metrics import Metrics

GCR = Field.GCR_WOS_FORMAT.value
DOC = Field.REC_SHORT_NAME.value
GCS = Field.GCS.value


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True

        matrix_list = self._compute_document_bibliographic_coupling()

        def remove_counters(matrix_list):
            if use_counters is False:
                self.params.counters = False
                matrix_list["ROWS"] = matrix_list["ROWS"].apply(
                    lambda x: " ".join(x.split(" ")[:-1])
                )
                matrix_list["COLUMNS"] = matrix_list["COLUMNS"].apply(
                    lambda x: " ".join(x.split(" ")[:-1])
                )
            return matrix_list

        if self.params.coupling_unit == CouplingUnit.DOC:
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

        coupling_unit = self.params.coupling_unit

        df = load_filtered_main_csv_zip(params=self.params)
        mapping = dict(zip(df[DOC].to_list(), df[coupling_unit.value].to_list()))

        matrix_list["ROWS"] = matrix_list["ROWS"].map(mapping)
        matrix_list["COLUMNS"] = matrix_list["COLUMNS"].map(mapping)

        if coupling_unit == CouplingUnit.AUTH:
            source_field = Field.AUTH_FULL_NAME
        elif coupling_unit == CouplingUnit.CTRY:
            source_field = Field.CTRY_ISO3
        elif coupling_unit == CouplingUnit.ORG:
            source_field = Field.ORG
        elif coupling_unit == CouplingUnit.SRC:
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
