import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field

GCS = Field.GCS.value
LCS = Field.LCS.value
YEAR = Field.YEAR.value
RID = Field.REC_ID.value
LCR = Field.LCR_WOS_FORMAT.value
GCR = Field.GCR_WOS_FORMAT.value


def matrix_list(
    params: Params,
) -> pd.DataFrame:

    records = load_filtered_main_csv_zip(params=params)
    records = records.sort_values(
        [GCS, LCS, YEAR, RID],
        ascending=[False, False, False, True],
    )
    records = records[[RID, LCR, GCS]]

    records.loc[:, LCR] = records[LCR].str.split("; ")
    records = records.explode(LCR)
    records[LCR] = records[LCR].str.strip()

    data_frame_with_links = records[
        records[LCR].map(lambda x: x in records[RID].to_list())
    ]
