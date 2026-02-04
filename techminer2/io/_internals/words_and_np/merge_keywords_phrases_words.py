from pathlib import Path

from techminer2 import Field
from techminer2._internals.data_access import load_main_data
from techminer2.io._internals.operations import copy_column, merge_columns


def _create_thesaurus(root_directory: str) -> None:

    dataframe = load_main_data(
        root_directory=root_directory, usecols=[Field.ALL_KEY_NP_WORD_NORM.value]
    )
    dataframe = dataframe.dropna()
    series = dataframe[Field.ALL_KEY_NP_WORD_NORM.value]
    series = series.str.split("; ")
    series = series.explode()
    series = series.str.strip()
    series = series.drop_duplicates()
    terms = series.to_list()

    filepath = Path(root_directory) / "data" / "thesaurus" / "terms.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for term in terms:
            file.write(f"{term}\n")
            file.write(f"    {term}\n")


def merge_keywords_phrases_words(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            Field.ALL_KEY_RAW,
            Field.ALL_NP_RAW,
            Field.ALL_WORD_RAW,
        ],
        target=Field.ALL_KEY_NP_WORD_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=Field.ALL_KEY_NP_WORD_RAW,
        target=Field.ALL_KEY_NP_WORD_NORM,
        root_directory=root_directory,
    )

    _create_thesaurus(root_directory=root_directory)

    return result
