from pathlib import Path

from techminer2 import CorpusField
from techminer2._internals.data_access import load_main_data
from techminer2.ingest.sources._internals.operations import copy_column, merge_columns


def _create_thesaurus(root_directory: str) -> None:

    dataframe = load_main_data(
        root_directory=root_directory, usecols=[CorpusField.FULL_KEY_NORM.value]
    )
    dataframe = dataframe.dropna()
    series = dataframe[CorpusField.FULL_KEY_NORM.value]
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


def merge_keywords_phrases_words(root_directory: str) -> int:

    result = merge_columns(
        sources=(
            CorpusField.KEY_TOK,
            CorpusField.NP_TOK,
            CorpusField.WORD_TOK,
        ),
        target=CorpusField.FULL_KEY_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.FULL_KEY_TOK,
        target=CorpusField.FULL_KEY_NORM,
        root_directory=root_directory,
    )

    _create_thesaurus(root_directory=root_directory)

    return result
