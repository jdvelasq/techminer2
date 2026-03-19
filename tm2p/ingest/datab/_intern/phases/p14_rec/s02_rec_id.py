import numpy as np
import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.discov.assoc.authkw import dataframe
from tm2p.ingest.datab._intern.phases.get_datab_marker import get_datab_marker


def s02_rec_id(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _scopus,
        "PubMed": _scopus,
        "Scopus": _scopus,
        "WoS": _wos,
    }[marker]

    if function:
        return function(root_directory)

    return 0


def _wos(root_directory: str) -> int:

    def get_cited_refs_list():
        cited_refs = df[Field.GCR_WOS_FORMAT.value].copy()
        cited_refs = cited_refs.dropna().str.split("; ")
        cited_refs = cited_refs.explode().str.strip()
        cited_refs = cited_refs.drop_duplicates().to_list()
        return cited_refs

    def select_wos_id(row):
        doi = row[Field.DOI.value]
        if pd.isna(doi):
            return None
        wos = [r for r in cited_refs if doi in r]
        if len(wos) > 0:
            return wos[0]
        return None

    df = load_main_csv_zip(root_directory)
    cited_refs = get_cited_refs_list()
    df[Field.REC_ID.value] = df.apply(select_wos_id, axis=1)
    df[Field.REC_ID.value] = df.apply(_build_rec_id, axis=1)
    save_main_csv_zip(df, root_directory)

    return 1


def _build_rec_id(row):

    def get_author(row):
        auth_first = row[Field.AUTH_FIRST.value]
        if pd.isna(auth_first):
            return "[Anonymous]"
        return auth_first

    def get_year(row):
        year = row[Field.YEAR.value]
        return ", " + str(year).replace(".0", "")

    def get_source_iso4(row):
        if Field.SRC_ISO4.value not in row:
            return ""
        if pd.isna(row[Field.SRC_ISO4.value]):
            return ""
        return ", " + row[Field.SRC_ISO4.value]

    def get_volume(row):
        if Field.VOL.value not in row:
            return ""
        vol = row[Field.VOL.value]
        if pd.isna(vol):
            return ""
        return ", V" + str(vol).replace(".0", "")

    def get_page_start(row):
        if Field.PG_FIRST.value not in row:
            return ""
        pg_first = row[Field.PG_FIRST.value]
        if pd.isna(pg_first):
            return ""
        return ", P" + str(pg_first).replace(".0", "")

    def get_doi(row):
        if Field.DOI.value not in row:
            return ""
        doi = row[Field.DOI.value]
        if pd.isna(doi):
            return ""
        return ", DOI " + str(doi)

    if Field.REC_ID.value in row:
        rec_id = row[Field.REC_ID.value]
        if not pd.isna(rec_id):
            return rec_id

    return (
        get_author(row)
        + get_year(row)
        + get_source_iso4(row)
        + get_volume(row)
        + get_page_start(row)
        + get_doi(row)
    )


def _scopus(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.REC_ID.value] = df.apply(_build_rec_id, axis=1)
    save_main_csv_zip(df, root_directory)

    return int(df[Field.REC_ID.value].notna().sum())
