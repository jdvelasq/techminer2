import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s02_auth_with_affil_pubmed(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    for text in [
        "Bernard J. Tyson",
        "Fl. No.",
        "Harvard T. H. Chan",
        "Inc.",
        "Joseph J. Zilber",
        "L. V. Prasad Eye Institute",
        "Lawrence S. Bloomberg",
        "P.O. Box",
        "Robert H. Lurie",
        "St.",
        "L. V. Prasad Eye Institute",
        "Grigore T. Popa",
        "Carl E. Ravin",
    ]:
        df[Field.AFFIL.value] = df[Field.AFFIL.value].str.replace(
            f" {text} ", f" {text.replace('.', '')} ", regex=False
        )

    df[Field.AFFIL.value] = df.apply(_process, axis=1)
    save_main_csv_zip(df, root_directory)

    return len(df)


def _process(row):

    if pd.isna(row[Field.AFFIL.value]):
        return row[Field.AFFIL.value]

    n_auth = row[Field.AUTH_RAW.value]
    n_auth = n_auth.split("; ")
    n_auth = len(n_auth)

    affil = row[Field.AFFIL.value]
    affil = affil.split(". ")
    affil = [af for af in affil if "@" not in af]
    n_affil = len(affil)

    if n_auth != n_affil:
        import sys

        sys.stderr.write(f"{row[Field.AUTH_RAW.value]}\n")
        for af in affil:
            sys.stderr.write(f"{af}\n")
        sys.stderr.write("\n")
        sys.stderr.flush()

    return row[Field.AFFIL.value]
