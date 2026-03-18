import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.ingest.datab._intern.phases.get_datab_marker import get_datab_marker


def s01_affil(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": None,
        "Scopus": None,
        "WoS": _wos,
    }[marker]

    if function:
        return function(root_directory)

    return 0


def _wos(root_directory: str) -> int:

    def _format(row):

        affil = row[Field.AFFIL.value]

        if pd.isna(affil):
            return affil

        affil = affil[1:] if affil.startswith("[") else affil
        affil = affil.split("; [")
        affil = [x.split("] ")[1] for x in affil]
        affil = [x[:-1] if x.endswith(".") else x for x in affil]
        affil = "; ".join(affil)

        return affil

    df = load_main_csv_zip(root_directory)
    df[Field.AFFIL.value] = df.apply(_format, axis=1)
    save_main_csv_zip(df, root_directory)

    return int(df[Field.AFFIL.value].notna().sum())
