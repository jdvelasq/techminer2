import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s09_format_pubmed_orcid(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.ORCID.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return 0


def _process(row):
    if pd.isna(row[Field.ORCID.value]):
        return "[UNKNOWN]"
    authors = row[Field.AUTH_FULL_NAME.value].split("; ")
    orcids = row[Field.ORCID.value].split("; ")
    result = []
    if len(authors) != len(orcids):
        return "[UNKNOWN]"
    for author, orcid in zip(authors, orcids):
        author = author.split(", ")
        full_name = f"{author[1]} {author[0]}"
        orcid = orcid.replace("ORCID: ", "")
        result.append(f"{full_name}/{orcid}")

    if not result:
        return "[UNKNOWN]"
    return "; ".join(result)
