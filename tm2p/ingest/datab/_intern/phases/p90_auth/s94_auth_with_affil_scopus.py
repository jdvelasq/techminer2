import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s02_auth_with_affil_scopus(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.AUTH_WITH_AFFIL.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return len(df)


def _process(row):

    if pd.isna(row[Field.AFFIL.value]):
        return row[Field.AFFIL.value]

    auth_full_name = row[Field.AUTH_FULL_NAME.value]
    auth_full_name = auth_full_name.split("; ")

    affil_raw = row[Field.AFFIL.value]
    affil_raw = affil_raw.split("; ")

    affils = [au + "/" + af for au, af in zip(auth_full_name, affil_raw)]
    affils = "; ".join(affils)

    return affils
