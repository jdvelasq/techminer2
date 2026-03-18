import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.sequ_gener import sequ_gener


def s04_authid_openalex(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    df[Field.AUTHID.value] = df[Field.AUTHID.value].str.replace(
        "https://openalex.org/", "", regex=False
    )
    df[Field.AUTHID.value] = df.apply(_dispatch, axis=1)

    save_main_csv_zip(df, root_directory)

    return int(df[Field.AUTHID.value].notna().sum())


def _dispatch(row):

    authid = row[Field.AUTHID.value]
    if pd.isna(authid):
        return _repair_full_dispatch(row)
    return _repair_partial_row(row)


def _repair_full_dispatch(row):

    auth = row[Field.AUTH_FULL_NAME.value]

    if pd.isna(auth):
        return pd.NA

    auth = auth.split("; ")
    orcid = row[Field.ORCID.value]
    orcid = orcid.split("; ")
    orcid = [o.strip() for o in orcid]

    result = []
    for idx, au in enumerate(auth):

        if idx < len(orcid) and orcid[idx] != "":
            result.append(au.strip() + "/" + orcid[idx].strip())
        else:
            result.append(au.strip() + sequ_gener())

    result = "; ".join(result)

    return result


def _repair_partial_row(row):

    auth = row[Field.AUTH_FULL_NAME.value]
    if pd.isna(auth):
        return pd.NA

    auth = auth.split("; ")
    auth = [au.strip() for au in auth]

    authid = row[Field.AUTH_NORM.value]
    authid = authid.split("; ")
    authid = [au.strip() for au in authid]

    orcid = row[Field.ORCID.value]
    orcid = orcid.split("; ")
    orcid = [o.strip() for o in orcid]

    result = []
    for au, auid, orc in zip(auth, authid, orcid):
        if pd.isna(auid) or auid == "":
            if orc != "":
                result.append(au.strip() + "/" + orc.strip())
            else:
                result.append(au.strip() + sequ_gener())
        else:
            result.append(auid.strip())

    if len(result) < len(auth):
        raise ValueError("Length of result is less than length of auth")

    return "; ".join(result)
