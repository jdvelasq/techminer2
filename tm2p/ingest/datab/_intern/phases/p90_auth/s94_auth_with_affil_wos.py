import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s02_auth_with_affil_wos(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.AUTH_WITH_AFFIL.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return len(df)


def _process(row):

    affils = row[Field.AFFIL.value]
    if pd.isna(affils):
        return affils

    affils = affils[1:] if affils.startswith("[") else affils
    affils = affils.split("; [")
    affils = [affil.strip() for affil in affils]
    affils = [afill[:-1] if afill.endswith(".") else afill for afill in affils]
    affils = [(affil.split("] ")[0], affil.split("] ")[1]) for affil in affils]

    affils = [af for af in affils if len(af) == 2]
    affils = [(a, af) for au, af in affils for a in au.split("; ")]
    affils = [(au, af) for au, af in affils if "," in au]
    affils = [(f"{au.split(', ')[1]} {au.split(', ')[0]}", af) for au, af in affils]

    affils = [au + "/" + af for au, af in affils]
    affils = "; ".join(affils)

    return affils
