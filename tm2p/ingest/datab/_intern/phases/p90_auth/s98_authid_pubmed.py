import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.sequ_gener import sequ_gener
from tm2p.ingest.datab._intern.oper.copy_col import copy_column


def s04_authid_pubmed(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.ORCID.value] = df[Field.ORCID.value].str.replace(
        "ORCID: ", "", regex=False
    )
    save_main_csv_zip(df, root_directory)

    copy_column(
        source=Field.ORCID,
        target=Field.AUTHID,
        root_directory=root_directory,
    )

    df = load_main_csv_zip(root_directory)
    df[Field.AUTHID.value] = df.apply(_repair, axis=1)
    save_main_csv_zip(df, root_directory)

    return int(df[Field.AUTHID.value].notna().sum())


def _repair(row):

    authid = row[Field.AUTHID.value]
    if pd.isna(authid):
        return _repair_na_row(row)
    return _repair_sequ(row)


def _repair_na_row(row):
    auth = row[Field.AUTH_NORM.value]
    if pd.isna(auth):
        return pd.NA
    auth = auth.split("; ")
    authid = [au.strip() + sequ_gener() for au in auth]
    return "; ".join(authid)


def _repair_sequ(row):

    auth = row[Field.AUTH_NORM.value]
    if pd.isna(auth):
        return pd.NA

    auth = auth.split("; ")
    auth = [au.strip() for au in auth]

    authid = row[Field.AUTH_NORM.value]
    authid = authid.split("; ")
    authid = [au.strip() for au in authid]

    result = []
    for au, auid in zip(auth, authid):
        if pd.isna(auid):
            result.append(au.strip() + sequ_gener())
        else:
            result.append(auid.strip())

    return "; ".join(result)
