from pathlib import Path

from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.data_source._intern.phases.get_datab_marker import get_datab_marker

from ._intern.extract_country_name import extract_country_name_from_string

AFFIL = Field.AFFIL.value
CTRY = "CTRY"


def s02_ctry_thesaurus(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": _process,
        "Scopus": _process,
        "WoS": _process,
    }[marker]

    if function:
        return function(root_directory)
    return 0


def _process(root_directory: str) -> int:
    df = load_main_csv_zip(root_directory)
    df = df[[AFFIL]]
    df = df.dropna().drop_duplicates()
    df[AFFIL] = df[AFFIL].str.split("; ")
    df = df.explode(AFFIL)  # type: ignore
    df = df.dropna().drop_duplicates()
    df[CTRY] = df[AFFIL].map(extract_country_name_from_string)
    grouped_df = df.groupby(CTRY, as_index=False)[AFFIL].apply(list)  # type: ignore

    filepath = Path(root_directory) / "refine" / "thesaurus" / "ctry.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:

        for _, row in grouped_df.iterrows():
            org = row[CTRY]
            file.write(f"{org}\n")
            for affil in sorted(row[AFFIL]):
                file.write(f"    {affil}\n")

    filepath_bak = filepath.with_suffix(".bak")
    filepath_bak.write_text(filepath.read_text(encoding="utf-8"), encoding="utf-8")

    return 1
