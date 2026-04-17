from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.helpers.get_zero_digits import get_zero_digits
from tm2p.enum import AnalysisUnit, Field
from tm2p.portfolio.performance_metrics.item_metrics import Metrics

GCS = Field.GCS.value
LCS = Field.LCS.value
YEAR = Field.YEAR.value
REC_ID = Field.REC_ID.value
LCR = Field.LCR_WOS_FORMAT.value
OCC = "OCC"

CITING_UNIT = "CITING_UNIT"
CITED_UNIT = "CITED_UNIT"


class OtherMatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = self._get_records()
        df = self._explode_local_cited_references(df)
        df = self._explode_citation_units(df)
        df = df.loc[df[CITING_UNIT] != "[UNKNOWN]", :]
        df = df.loc[df[CITED_UNIT] != "[UNKNOWN]", :]
        df = self._add_counters_to_citation_units(df)
        df = self._count_citations_per_citing_cited_pair(df)
        df = self._sort_matrix_list(df)

        return df

    def _sort_matrix_list(self, df):
        df = df.copy()
        df["CITING_OCC"] = df[CITING_UNIT].apply(
            lambda x: int(x.split(" ")[-1].split(":")[0])
        )
        df["CITING_GCS"] = df[CITING_UNIT].apply(
            lambda x: int(x.split(" ")[-1].split(":")[0])
        )
        df["CITED_OCC"] = df[CITED_UNIT].apply(
            lambda x: int(x.split(" ")[-1].split(":")[0])
        )
        df["CITED_GCS"] = df[CITED_UNIT].apply(
            lambda x: int(x.split(" ")[-1].split(":")[0])
        )

        df = df.sort_values(
            by=[
                "OCC",
                "CITING_OCC",
                "CITING_GCS",
                CITING_UNIT,
                "CITED_OCC",
                "CITED_GCS",
                CITED_UNIT,
            ],
            ascending=[False, False, False, True, False, False, True],
        )

        df = df.drop(columns=["CITING_OCC", "CITING_GCS", "CITED_OCC", "CITED_GCS"])
        df = df.reset_index(drop=True)

        return df

    def _count_citations_per_citing_cited_pair(self, df):
        df = df.groupby(
            [CITING_UNIT, CITED_UNIT],
            as_index=False,
        ).size()
        df = df.rename(columns={"size": "OCC"})
        return df

    def _add_counters_to_citation_units(self, df):

        # if self.params.analysis_unit == AnalysisUnit.AUTH:
        #     source_field = Field.AUTH_FULL_NAME
        # elif self.params.analysis_unit == AnalysisUnit.CTRY:
        #     source_field = Field.CTRY_ISO3
        # elif self.params.analysis_unit == AnalysisUnit.ORG:
        #     source_field = Field.ORG
        # elif self.params.analysis_unit == AnalysisUnit.SRC:
        #     source_field = Field.SRC_ISO4
        # else:
        #     raise ValueError("Invalid citation unit")

        metrics = (
            Metrics().update(**self.params.__dict__)
            # .with_source_field(source_field)
            .run()
        )

        df = df.loc[df[CITING_UNIT].isin(metrics.index.to_list()), :]
        df = df.loc[df[CITED_UNIT].isin(metrics.index.to_list()), :]

        #
        # Adds citations and occurrences to items
        occ_digits, gcs_digits = get_zero_digits(
            root_directory=self.params.root_directory
        )

        fmt_occ = "{:0" + str(occ_digits) + "d}"
        fmt_citations = "{:0" + str(gcs_digits) + "d}"

        rename_dict = {
            key: value
            for key, value in zip(
                metrics.index.to_list(),
                (
                    metrics.index
                    + " "
                    + metrics[OCC].map(fmt_occ.format)
                    + ":"
                    + metrics[GCS].map(fmt_citations.format)
                ).to_list(),
            )
        }

        df[CITING_UNIT] = df[CITING_UNIT].map(rename_dict)
        df[CITED_UNIT] = df[CITED_UNIT].map(rename_dict)
        return df

    def _explode_citation_units(self, df):

        article2unit = {
            row[REC_ID]: row[CITING_UNIT]
            for _, row in df[[REC_ID, CITING_UNIT]].iterrows()
        }
        df[CITED_UNIT] = df[CITED_UNIT].map(article2unit)

        df[CITING_UNIT] = df[CITING_UNIT].str.split(";")
        df = df.explode(CITING_UNIT)  # type: ignore
        df[CITING_UNIT] = df[CITING_UNIT].str.strip()

        df[CITED_UNIT] = df[CITED_UNIT].str.split(";")
        df = df.explode(CITED_UNIT)  # type: ignore
        df[CITED_UNIT] = df[CITED_UNIT].str.strip()

        selected_rows = [
            row[CITED_UNIT] != row[CITING_UNIT] for _, row in df.iterrows()
        ]
        df = df.loc[selected_rows, :]

        return df

    def _explode_local_cited_references(self, df):
        df[LCR] = df[LCR].str.split(";")
        df = df.explode(LCR)  # type: ignore
        df[LCR] = df[LCR].str.strip()
        df = df.rename(
            columns={
                LCR: "CITED_UNIT",
                self.params.analysis_unit: "CITING_UNIT",
            }
        )
        df.index = df[REC_ID].copy()
        return df

    def _get_records(self):
        df = load_filtered_main_csv_zip(self.params)
        df = df[[REC_ID, self.params.analysis_unit, LCR]].copy()
        df = df.dropna()
        return df
