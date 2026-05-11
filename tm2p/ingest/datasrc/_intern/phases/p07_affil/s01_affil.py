from pathlib import Path

import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.phases.get_datab_marker import get_datab_marker

AUTH_WITH_AFFIL = Field.AUTH_WITH_AFFIL.value


def s01_affil(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": _pubmed,
        "Scopus": None,
        "WoS": _wos,
    }[marker]

    if function:
        return function(root_directory)

    return 0


def _pubmed(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    df[Field.AFFIL.value] = df[Field.AFFIL.value].str.replace(".;", ";", regex=False)
    df[Field.AFFIL.value] = df[Field.AFFIL.value].str.replace(".$", "", regex=True)
    df[Field.AFFIL.value] = df[Field.AFFIL.value].str.replace(r"\s+", " ", regex=True)
    df[Field.AFFIL.value] = df[Field.AFFIL.value].str.replace(
        ", Inc.", " Inc.", regex=False
    )

    save_main_csv_zip(df, root_directory)

    return int(df[Field.AFFIL.value].notna().sum())


def _wos(root_directory: str) -> int:

    def _format(row):

        affil = row[Field.AFFIL.value]

        if pd.isna(affil):
            return affil

        affil = affil[1:] if affil.startswith("[") else affil
        affil = affil.split("; [")
        affil = [x.split("] ")[1] if "] " in x else x for x in affil]
        affil = [x[:-1] if x.endswith(".") else x for x in affil]
        affil = "; ".join(affil)

        return affil

    df = load_main_csv_zip(root_directory)
    df[Field.AFFIL.value] = df.apply(_format, axis=1)
    save_main_csv_zip(df, root_directory)

    _save_wos_aff(root_directory)

    return int(df[Field.AFFIL.value].notna().sum())


def _save_wos_aff(root_directory: str) -> None:

    df = load_main_csv_zip(root_directory)
    aff = df[AUTH_WITH_AFFIL].dropna().str.split("; ").explode()
    aff = aff.str.strip()
    aff = aff.drop_duplicates()
    aff = sorted(aff.to_list())

    filepath = Path(root_directory) / "refine" / "thesaurus" / "aff.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for a in aff:
            name = a.split("] ")[0]
            org = a.split("] ")[1]
            file.write(f"{name[1:]}\n    {org}\n")
