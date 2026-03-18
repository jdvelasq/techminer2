import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.sequ_gener import sequ_gener
from tm2p.ingest.datab._intern.oper.copy_col import copy_column


def s04_authid_wos(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.AUTHID.value] = df.apply(_repair, axis=1)
    save_main_csv_zip(df, root_directory)

    return int(df[Field.AUTHID.value].notna().sum())


def _repair(row):

    authid = row[Field.AUTHID.value]
    if pd.isna(authid):
        return _repair_full_row(row)
    return _repair_partial_row(row)


def _repair_full_row(row):
    auth = row[Field.AUTH_FULL_NAME.value]
    auth = auth.split("; ")
    auth = [au.split(", ")[1] + " " + au.split(", ")[0] for au in auth]
    authid = [au.strip() + sequ_gener() for au in auth]
    authid = "; ".join(authid)

    return authid


def _repair_partial_row(row):

    auth = row[Field.AUTH_FULL_NAME.value]
    auth = auth.split("; ")
    auth = [au.strip() for au in auth]

    authid = row[Field.AUTHID.value]
    authid = authid.lower()
    authid = authid.split("; ")

    result = []
    for au in auth:
        au_short = au.split(" ")[0].lower()
        found = False
        for x in authid:
            if au_short in x:
                result.append(x.title())
                found = True
                continue
        if found is False:
            au = au.split(", ")
            if len(au) == 2:
                au = au[1].strip() + " " + au[0].strip()
            elif len(au) == 1:
                au = au[0].strip()
            else:
                raise ValueError(f"Unexpected author name format for row {row.name}")
            result.append(au + sequ_gener())

    if len(result) != len(auth):
        raise ValueError(f"Could not match all authors to their IDs for row {row.name}")

    authid = "; ".join(result)

    return authid
