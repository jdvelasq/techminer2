import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.phases.get_datab_marker import get_datab_marker

REC_ID = Field.REC_ID.value
GCR_WOS_FORMAT = Field.GCR_WOS_FORMAT_NORM.value
LCR_WOS_FORMAT = Field.LCR_WOS_FORMAT.value


def s02_lcr_wos_format(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": None,
        "Scopus": _scopus,
        "WoS": _scopus,
    }[marker]

    if function:
        return function(root_directory=root_directory)

    return 0


def _scopus(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory=root_directory)
    rec_id = df[REC_ID].dropna().drop_duplicates().to_list()

    if GCR_WOS_FORMAT not in df.columns:
        return 0

    def extract(row):
        if pd.isna(row[GCR_WOS_FORMAT]):
            return pd.NA
        gcr = row[GCR_WOS_FORMAT]
        gcr = gcr.split("; ")
        gcr = [g.strip() for g in gcr]
        lcr = [g for g in gcr if g in rec_id]
        lcr = "; ".join(lcr)
        return lcr

    df[LCR_WOS_FORMAT] = df.apply(extract, axis=1)
    save_main_csv_zip(df=df, root_directory=root_directory)

    return df[LCR_WOS_FORMAT].notna().sum()
