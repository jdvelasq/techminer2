import textwrap
from pathlib import Path

from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field


def s06_plain_abstracts(root_directory: str) -> None:

    df = load_main_csv_zip(root_directory=root_directory)
    df = df[[Field.ABSTR_UPPER.value]]
    df = df.dropna().head(300)

    filename = Path(root_directory) / "report" / "abstracts-upper.txt"

    with open(filename, "w", encoding="utf-8") as txt_file:
        for abstract in df[Field.ABSTR_UPPER.value].tolist():
            wrapped_abstract = textwrap.fill(abstract, width=90)
            txt_file.write(wrapped_abstract + "\n\n\n")
