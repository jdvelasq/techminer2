from pathlib import Path

from techminer2 import CorpusField
from techminer2._internals.data_access import load_main_data


def create_descriptor_thesaurus(root_directory: str) -> int:

    dataframe = load_main_data(
        root_directory=root_directory, usecols=[CorpusField.DESCRIPTOR_NORM.value]
    )
    dataframe = dataframe.dropna()
    series = dataframe[CorpusField.DESCRIPTOR_NORM.value]
    series = series.str.split("; ")
    series = series.explode()
    series = series.str.strip()
    series = series.drop_duplicates()
    terms = series.to_list()
    terms = sorted(terms)

    filepath = Path(root_directory) / "refine" / "thesaurus" / "descriptors.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for term in terms:
            file.write(f"{term}\n")
            file.write(f"    {term}\n")

    return len(terms)
