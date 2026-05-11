from pathlib import Path

import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.phases.get_datab_marker import get_datab_marker

AUTH_FULL_NAME = Field.AUTH_FULL_NAME.value
AUTH_WITH_AFFIL = Field.AUTH_WITH_AFFIL.value


def s01_auth_full_name_wos(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _openalex,
        "PubMed": _pubmed,
        "Scopus": _scopus,
        "WoS": _wos,
    }[marker]

    df = load_main_csv_zip(root_directory)
    df[AUTH_FULL_NAME] = df.apply(function, axis=1)
    save_main_csv_zip(df, root_directory)

    auth = df[AUTH_FULL_NAME].copy().dropna()
    auth = auth.str.split("; ").explode()
    auth = auth.str.strip()
    auth = auth.drop_duplicates()

    mapping = {a: [a] for a in sorted(auth.to_list())}

    _save_thesaurus_file(mapping, root_directory)

    if marker == "Scopus":
        _save_scopus_aff(root_directory)

    return len(df)


def _save_scopus_aff(root_directory: str) -> None:

    df = load_main_csv_zip(root_directory)
    aff = df[AUTH_WITH_AFFIL].dropna().str.split("; ").explode()
    aff = aff.str.strip()
    aff = aff.drop_duplicates()
    aff = sorted(aff.to_list())

    filepath = Path(root_directory) / "refine" / "thesaurus" / "aff.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for a in aff:
            if "," in a:
                name = a.split(", ")[0]
                org = a.split(", ")[1]
                file.write(f"{name}\n    {org}\n")


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


def _save_thesaurus_file(mapping: dict[str, list[str]], root_directory: str) -> None:

    filepath1 = Path(root_directory) / "refine" / "thesaurus" / "auth.the.txt"
    filepath2 = Path(root_directory) / "refine" / "thesaurus" / "auth.the.bak"

    for filepath in [filepath1, filepath2]:

        with open(filepath, "w", encoding="utf-8") as file:
            for key, values in mapping.items():
                file.write(f"{key}\n")
                for value in values:
                    file.write(f"    {value}\n")


def _openalex(row):

    auth_full_name = row[AUTH_FULL_NAME]

    if pd.isna(auth_full_name):
        return auth_full_name

    auth = auth_full_name.split("; ")
    min_words = min(len(au.split(" ")) for au in auth)
    if min_words < 2:
        return pd.NA

    auth_full_name = auth_full_name.title()
    return auth_full_name


def _pubmed(row):

    auth_full_name = row[AUTH_FULL_NAME]

    if pd.isna(auth_full_name):
        return auth_full_name

    auth_full_name = auth_full_name.split("; ")
    min_words = min(len(au.split(" ")) for au in auth_full_name)
    if min_words < 2:
        return pd.NA

    auth_full_name = [
        au.split(", ")[1] + " " + au.split(", ")[0]
        for au in auth_full_name
        if "," in au
    ]
    auth_full_name = "; ".join(auth_full_name)

    auth_full_name = auth_full_name.title()
    return auth_full_name


def _scopus(row):

    auth_full_name = row[AUTH_FULL_NAME]

    if pd.isna(auth_full_name):
        return auth_full_name

    auth_full_name = auth_full_name.split("; ")
    auth_full_name = [au.split(" (")[0] for au in auth_full_name]

    min_words = min(len(au.split(" ")) for au in auth_full_name)
    if min_words < 2:
        return pd.NA

    auth_full_name = [
        au.split(", ")[1] + " " + au.split(", ")[0]
        for au in auth_full_name
        if "," in au
    ]
    auth_full_name = "; ".join(auth_full_name)
    auth_full_name = auth_full_name.title()

    return auth_full_name


def _wos(row):

    auth_full_name = row[AUTH_FULL_NAME]
    auth_full_name = auth_full_name.split("; ")

    auth_full_name = [
        au.split(", ")[1] + " " + au.split(", ")[0]
        for au in auth_full_name
        if "," in au
    ]
    auth_full_name = "; ".join(auth_full_name)

    return auth_full_name
