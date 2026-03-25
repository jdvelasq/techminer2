from pathlib import Path

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip


def s03_descriptor_thesaurus(root_directory: str) -> int:

    df = load_main_csv_zip(
        root_directory=root_directory, usecols=[Field.DESCRIPTOR_RAW.value]
    )
    df = df.dropna()
    series = df[Field.DESCRIPTOR_RAW.value].str.split("; ")
    series = series.explode()
    series = series.str.strip()
    series = series.drop_duplicates()
    terms = series.to_list()
    terms = sorted(terms)

    filepath = Path(root_directory) / "refine" / "thesaurus" / "concept.the.txt"
    with open(filepath, "w", encoding="utf-8") as file:
        for term in terms:
            file.write(f"{term}\n")
            file.write(f"    {term}\n")

    filepath_bak = filepath.with_suffix(".bak")
    filepath_bak.write_text(filepath.read_text(encoding="utf-8"), encoding="utf-8")

    return len(terms)
