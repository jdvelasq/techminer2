import re
from pathlib import Path

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr
from techminer2._internals.package_data.text_processing import (
    load_text_processing_terms,
)

with stdout_to_stderr():
    pandarallel.initialize(progress_bar=True)


_COMPILED_PATTERNS: list[tuple[str, re.Pattern]] = []


def _get_project_noun_phrases(root_directory: str) -> set[str]:
    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    noun_phrases = set()

    for column in ["raw_textblob_phrases", "raw_spacy_phrases"]:
        if column in dataframe.columns:
            for entry in dataframe[column].dropna():
                phrases = [phrase.strip() for phrase in entry.split(";")]
                noun_phrases.update(phrases)

    return noun_phrases


def _get_system_noun_phrases() -> set[str]:
    noun_phrases = load_text_processing_terms("known_noun_phrases.txt")
    noun_phrases = [
        phrase.strip().lower().replace("_", " ")
        for phrase in noun_phrases
        if phrase.strip()
    ]
    return set(noun_phrases)


def _get_acronyms(root_directory: str) -> set[str]:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    acronyms = set()

    if "acronyms" in dataframe.columns:
        for entry in dataframe["acronyms"].dropna():
            phrases = [phrase.strip() for phrase in entry.split(";")]
            acronyms.update(phrases)

    return acronyms


def _clean_terms(terms: set[str]) -> set[str]:

    stopwords = load_text_processing_terms("stopwords.txt")
    cleaned_terms = set()
    for term in terms:
        term_lower = term.lower()
        if (
            term_lower not in stopwords
            and len(term_lower) > 1
            and "(" not in term_lower
            and "," not in term_lower
            and not any(char.isdigit() for char in term)
        ):
            cleaned_terms.add(term)
    return cleaned_terms


def _get_project_keywords(root_directory: str) -> set[str]:
    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    keywords = set()

    for column in ["raw_author_keywords", "raw_index_keywords"]:
        if column in dataframe.columns:
            for entry in dataframe[column].dropna():
                phrases = [phrase.strip() for phrase in entry.split(";")]
                keywords.update(phrases)

    return keywords


def _get_compiled_patterns(root_directory: str) -> list[tuple[str, re.Pattern]]:

    if not _COMPILED_PATTERNS:

        patterns = _get_project_noun_phrases(root_directory)
        patterns.update(_get_system_noun_phrases())
        patterns.update(_get_acronyms(root_directory))
        patterns = _clean_terms(patterns)
        patterns.update(_get_project_keywords(root_directory))

        patterns_list = sorted(
            patterns,
            key=lambda x: (len(x.split(" ")), x),
            reverse=True,
        )

        _COMPILED_PATTERNS.extend(
            (pattern, re.compile(r"\b" + re.escape(pattern) + r"\b"))
            for pattern in patterns_list
        )
    return _COMPILED_PATTERNS


def normalize_descriptors(text):

    if pd.isna(text):
        return text

    text = str(text)
    for phrase, pattern in _get_compiled_patterns(root_directory):
        if phrase in text:
            text = pattern.sub(lambda m: m.group().upper().replace(" ", "_"), text)

    return text
