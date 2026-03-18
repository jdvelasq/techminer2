import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s04_orcid_wos(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.ORCID.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return 1


def _process(row):
    if pd.isna(row[Field.ORCID.value]):
        return pd.NA

    orcids = row[Field.ORCID.value].split("; ")
    result = []
    for orcid in orcids:
        parts = orcid.split("/")
        surname, firstname = parts[0].split(", ")
        full_name = f"{firstname.title()} {surname.title()}"
        orcid_id = parts[1]
        result.append(f"{full_name}/{orcid_id}")

    if not result:
        return pd.NA
    result = [x for x in result if x.strip() != ""]
    result = "; ".join(result)
    if result[-1] == ";":
        result = result[:-1]
    return result
