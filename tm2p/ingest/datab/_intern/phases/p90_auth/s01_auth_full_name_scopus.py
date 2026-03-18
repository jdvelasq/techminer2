from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s01_auth_full_name_scopus(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.AUTH_FULL_NAME.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return len(df)


def _process(row):

    auth_full_name = row[Field.AUTH_FULL_NAME.value]
    auth_full_name = auth_full_name.split("; ")
    auth_full_name = [au.split(" (")[0] for au in auth_full_name]
    auth_full_name = [
        au.split(", ")[1] + " " + au.split(", ")[0]
        for au in auth_full_name
        if "," in au
    ]
    auth_full_name = "; ".join(auth_full_name)

    return auth_full_name
