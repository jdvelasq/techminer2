from pathlib import Path

import pandas as pd

from techminer2._internals.package_data.word_lists import (
    load_builtin_word_list,
    save_text_processing_terms,
)


def _load_dataframe(root_directory: str) -> pd.DataFrame:

    database_file = Path(root_directory) / "ingest" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    return pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )


def _extract_raw_noun_phrases(dataframe: pd.DataFrame) -> set:

    noun_phrases = set()

    if "raw_noun_phrases" in dataframe.columns:
        series = (
            dataframe["raw_noun_phrases"]
            .dropna()
            .str.split("; ")
            .explode()
            .str.strip()
            .drop_duplicates()
        )
        noun_phrases.update(series.to_list())

    return noun_phrases


def _extract_frequent_raw_keywords(dataframe: pd.DataFrame) -> set:

    keywords = set()

    for col in ["author_keywords_raw", "index_keywords_raw"]:

        if col in dataframe.columns:

            df = dataframe[[col]].copy()
            df = df.dropna()
            df = df.groupby(col).size().reset_index().rename(columns={0: "count"})
            df = df[df["count"] >= 2]
            series = df[col]
            keywords.update(series.to_list())

    return keywords


def _load_builtin_noun_phrases() -> set:
    buildin_noun_phrases = load_builtin_word_list("noun_phrases.txt")
    return set(buildin_noun_phrases)


def update_builtin_noun_phrases(root_directory: str) -> int:

    dataframe = _load_dataframe(root_directory)
    builtin_noun_phrases = _load_builtin_noun_phrases()
    user_noun_phrases = _extract_raw_noun_phrases(dataframe)
    keywords = _extract_frequent_raw_keywords(dataframe)
    keywords = keywords - user_noun_phrases
    builtin_noun_phrases.update(keywords)
    save_text_processing_terms("noun_phrases.txt", sorted(builtin_noun_phrases))

    return len(keywords)
