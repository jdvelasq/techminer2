import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.enum import Field
from tm2p.ingest.data_source._intern.phases.get_datab_marker import get_datab_marker


def s01_auth_full_name_wos(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _openalex,
        "PubMed": _pubmed,
        "Scopus": _scopus,
        "WoS": _wos,
    }[marker]

    df = load_main_csv_zip(root_directory)
    df[Field.AUTH_FULL_NAME.value] = df.apply(function, axis=1)
    save_main_csv_zip(df, root_directory)
    return len(df)


def _openalex(row):

    auth_full_name = row[Field.AUTH_FULL_NAME.value]

    if pd.isna(auth_full_name):
        return auth_full_name

    auth = auth_full_name.split("; ")
    min_words = min(len(au.split(" ")) for au in auth)
    if min_words < 2:
        return pd.NA

    auth_full_name = auth_full_name.title()
    return auth_full_name


def _pubmed(row):

    auth_full_name = row[Field.AUTH_FULL_NAME.value]

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

    auth_full_name = row[Field.AUTH_FULL_NAME.value]

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

    auth_full_name = row[Field.AUTH_FULL_NAME.value]
    auth_full_name = auth_full_name.split("; ")

    auth_full_name = [
        au.split(", ")[1] + " " + au.split(", ")[0]
        for au in auth_full_name
        if "," in au
    ]
    auth_full_name = "; ".join(auth_full_name)

    return auth_full_name
