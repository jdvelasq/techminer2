"""
CountMatrixList
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore 
    >>> from tm2p.portfolio.intellect_struct.coupling.direct import CountMatrixList  # type: ignore
    >>> df = (
    ...     CountMatrixList()
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
                                                            ROWS                                                    COLUMNS  OCC
    0   Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAG 1:00030  Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAGa 1:00018   43
    1  Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAGa 1:00018   Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAG 1:00030   43
    2   Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAG 1:00030             Hussain M, 2012, INT J LOGIST-RES APPL 1:00017   35
    3             Hussain M, 2012, INT J LOGIST-RES APPL 1:00017   Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAG 1:00030   35
    4  Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAGa 1:00018             Hussain M, 2012, INT J LOGIST-RES APPL 1:00017   34
    5             Hussain M, 2012, INT J LOGIST-RES APPL 1:00017  Hussain M, 2011, INT J PHYS DISTRIB LOGIST MANAGa 1:00018   34
    6                      Orji IJ, 2015, COMPUT IND ENG 1:00125               Orji IJ, 2015, J MANUF TECHNOL MANAG 1:00020   25
    7               Orji IJ, 2015, J MANUF TECHNOL MANAG 1:00020                      Orji IJ, 2015, COMPUT IND ENG 1:00125   25
    8                            Dale M, 2012, ECOL ECON 1:00023                           Dale M, 2012, ECOL ECONa 1:00050   16
    9                           Dale M, 2012, ECOL ECONa 1:00050                            Dale M, 2012, ECOL ECON 1:00023   16

    
* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     CountMatrixList()
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
                                 ROWS                         COLUMNS  OCC
    0             T. H. Woo 003:00005            Tae Ho Woo 004:00007    4
    1            Tae Ho Woo 004:00007             T. H. Woo 003:00005    4
    2            Tae Ho Woo 004:00007  Yahia Zare Mehrjerdi 003:00008    3
    3  Yahia Zare Mehrjerdi 003:00008            Tae Ho Woo 004:00007    3
    4            Tae Ho Woo 004:00007            Tae Ho Woo 004:00007    2
    5             T. H. Woo 003:00005  Yahia Zare Mehrjerdi 003:00008    1
    6  Yahia Zare Mehrjerdi 003:00008             T. H. Woo 003:00005    1



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.helpers.get_zero_digit import get_zero_digits
from tm2p.enum import AnalysisUnit, Field
from tm2p.portfolio.perform_metr.unit.metr import Metrics

GCR = Field.GCR_WOS_FORMAT_NORM.value
DOC = Field.REC_SHORT_NAME.value
GCS = Field.GCS.value


class CountMatrixList(
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
