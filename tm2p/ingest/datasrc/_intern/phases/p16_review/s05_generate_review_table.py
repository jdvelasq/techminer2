from pathlib import Path

from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field

SIZE = 30


def s05_generate_review_table(root_directory: str) -> None:

    df = load_main_csv_zip(root_directory=root_directory).head(100)

    for col in df.columns:
        if df[col].dtype == "object":
            max_size = df[col].str.len().max()
            if col in (Field.REC_ID.value,):
                df[col] = df[col].str[:50]
            elif col in (
                Field.ORCID.value,
                Field.AFFIL.value,
                Field.AUTH_WITH_AFFIL.value,
                Field.AUTHID.value,
                Field.ORG.value,
                "AD",
            ):
                df[col] = df[col].str[:80]
            elif max_size > SIZE:
                df[col] = df[col].str[:SIZE]

    filename = Path(root_directory) / "refine" / "review_table.txt"

    df = df.head(40)

    with open(filename, "w", encoding="utf-8") as txt_file:
        txt_file.write(df.to_markdown(index=False))
