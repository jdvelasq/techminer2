import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s04_orcid_pubmed(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.ORCID.value] = df[Field.ORCID.value].str.replace(
        "ORCID: ", "", regex=False
    )
    df[Field.ORCID.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return 0


def _process(row):

    if pd.isna(row[Field.ORCID.value]):
        return pd.NA

    authors = row[Field.AUTH_FULL_NAME.value].split("; ")
    orcids = row[Field.ORCID.value].split("; ")

    if len(authors) != len(orcids):
        return pd.NA

    result = []
    for author, orcid in zip(authors, orcids):
        result.append(f"{author}/{orcid}")

    if not result:
        return pd.NA
    return "; ".join(result)
