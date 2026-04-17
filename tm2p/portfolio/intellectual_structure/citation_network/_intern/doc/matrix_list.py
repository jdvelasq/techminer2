from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.helpers.get_zero_digits import get_zero_digits
from tm2p.enum import Field

GCS = Field.GCS.value
LCS = Field.LCS.value
YEAR = Field.YEAR.value
RID = Field.REC_ID.value
LCR = Field.LCR_WOS_FORMAT.value
GCR = Field.GCR_WOS_FORMAT.value
OCC = "OCC"
SHORT_NAME = Field.REC_SHORT_NAME.value


class DocMatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.use_counters
        self.params.use_counters = True

        df_full = _get_records(self.params)

        df_with_links = _explode_local_cited_references(df_full)
        df_with_links = _add_counters_to_records(self.params, df_full, df_with_links)
        df_with_links = _remove_records_without_local_cited_references(df_with_links)

        df_with_links = df_with_links[[LCR, RID]]
        df_with_links.loc[:, OCC] = 1

        if use_counters is False:
            self.params.use_counters = False
            df_with_links.loc[:, LCR] = df_with_links[LCR].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )
            df_with_links.loc[:, RID] = df_with_links[RID].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )

        df_with_links = df_with_links.rename(
            columns={
                LCR: "CITED_UNIT",
                RID: "CITING_UNIT",
            }
        )

        df_with_links = df_with_links.reset_index(drop=True)

        # ----------
        _, gcs_digits = get_zero_digits(root_directory=self.params.root_directory)

        fmt = " 1:{:0" + str(gcs_digits) + "d}"

        rename_dict = {
            key: value
            for key, value in zip(
                df_full[RID].to_list(),
                (df_full[RID] + df_full[GCS].map(fmt.format)).to_list(),
            )
        }
        df_full.loc[:, RID] = df_full[RID].map(rename_dict)

        # ----------

        rename_dict = {
            key: value
            for key, value in zip(
                df_full[SHORT_NAME].to_list(),
                (df_full[SHORT_NAME] + df_full[GCS].map(fmt.format)).to_list(),
            )
        }
        df_full.loc[:, SHORT_NAME] = df_full[SHORT_NAME].map(rename_dict)

        # ----------

        mapping = dict(zip(df_full[RID].to_list(), df_full[SHORT_NAME].to_list()))
        df_with_links.loc[:, "CITING_UNIT"] = df_with_links["CITING_UNIT"].map(mapping)
        df_with_links.loc[:, "CITED_UNIT"] = df_with_links["CITED_UNIT"].map(mapping)

        return df_with_links


def _remove_records_without_local_cited_references(data_frame_with_links):
    data_frame_with_links = data_frame_with_links.dropna()
    return data_frame_with_links


def _add_counters_to_records(params, df_full, df_with_links):

    _, gcs_digits = get_zero_digits(root_directory=params.root_directory)

    fmt = " 1:{:0" + str(gcs_digits) + "d}"

    rename_dict = {
        key: value
        for key, value in zip(
            df_full[RID].to_list(),
            (df_full[RID] + df_full[GCS].map(fmt.format)).to_list(),
        )
    }

    df_with_links.loc[:, RID] = df_with_links[RID].map(rename_dict)
    df_with_links.loc[:, LCR] = df_with_links[LCR].map(rename_dict)
    return df_with_links


def _explode_local_cited_references(df_full):

    df_full.loc[:, LCR] = df_full[LCR].str.split("; ")
    df_full = df_full.explode(LCR)
    df_full[LCR] = df_full[LCR].str.strip()

    df_with_links = df_full[df_full[LCR].map(lambda x: x in df_full[RID].to_list())]

    return df_with_links


def _get_records(params):
    records = load_filtered_main_csv_zip(params=params)
    records = records.sort_values(
        [GCS, LCS, YEAR, RID, SHORT_NAME],
        ascending=[False, False, False, True, True],
    )
    records = records[[RID, LCR, GCS, SHORT_NAME]]
    return records
