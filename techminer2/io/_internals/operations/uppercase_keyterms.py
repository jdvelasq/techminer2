import re

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2 import CorpusField
from techminer2._internals import stdout_to_stderr
from techminer2._internals.package_data.text_processing import (
    load_text_processing_terms,
)

from ._file_dispatch import get_file_operations
from .data_file import DataFile
from .helpers import (
    extract_urls,
    join_consecutive_descriptors,
    mark_abstract_headings,
    mark_connectors,
    mark_copyright,
    mark_discursive_patterns,
    repair_abstract_headings,
    repair_apostrophes,
    repair_emails,
    repair_et_al,
    repair_lowercase_text,
    repair_measurement_units,
    repair_roman_numbers,
    repair_strange_cases,
    repair_urls,
)

_COMPILED_PATTERNS: list[tuple[str, re.Pattern]] = []


# ----------------------------------------------------------------------------
def _get_project_noun_phrases(dataframe: pd.DataFrame) -> set[str]:

    noun_phrases = set()

    for column in ["noun_phrases_textblob", "noun_phrases_spacy"]:
        if column in dataframe.columns:
            for entry in dataframe[column].dropna():
                phrases = [phrase.strip() for phrase in entry.split(";")]
                noun_phrases.update(phrases)

    return noun_phrases


# ----------------------------------------------------------------------------
def _get_system_noun_phrases() -> set[str]:
    noun_phrases = load_text_processing_terms("noun_phrases.txt")
    noun_phrases = [
        phrase.strip().lower().replace("_", " ")
        for phrase in noun_phrases
        if phrase.strip()
    ]
    return set(noun_phrases)


# ----------------------------------------------------------------------------
def _get_acronyms(dataframe: pd.DataFrame) -> set[str]:

    acronyms = set()

    if "acronyms" in dataframe.columns:
        for entry in dataframe["acronyms"].dropna():
            phrases = [phrase.strip() for phrase in entry.split(";")]
            acronyms.update(phrases)

    return acronyms


# ----------------------------------------------------------------------------
def _clean_terms(terms: set[str]) -> set[str]:

    stopwords = load_text_processing_terms("technical_stopwords.txt")
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


# ----------------------------------------------------------------------------
def _get_project_keywords(dataframe: pd.DataFrame) -> set[str]:

    keywords = set()

    for column in [
        "author_keywords_raw",
        "index_keywords_raw",
    ]:
        if column in dataframe.columns:
            for entry in dataframe[column].dropna():
                phrases = [phrase.strip() for phrase in entry.split(";")]
                keywords.update(phrases)

    #     terms = terms.str.translate(str.maketrans("", "", "\"'#!"))
    #     terms = terms.str.replace(re.compile(r"\(.*\)"), "", regex=True)
    #     terms = terms.str.replace(re.compile(r"\[.*\]"), "", regex=True)
    #     terms = terms.str.translate(str.maketrans("-", " "))  # added
    #     terms = terms.str.translate(str.maketrans("_", " "))
    #     terms = terms.str.lower()
    #     terms = terms.str.split("; ")
    #     terms = terms.explode()
    #     terms = terms.str.strip()
    #     terms = terms[terms.str.len() > 2]
    #     terms = terms[~terms.str.contains(r"\d", regex=True)]

    return keywords


# ----------------------------------------------------------------------------
def _get_compiled_patterns(dataframe: pd.DataFrame) -> list[tuple[str, re.Pattern]]:

    if not _COMPILED_PATTERNS:

        patterns = _get_project_noun_phrases(dataframe)
        patterns.update(_get_system_noun_phrases())
        patterns.update(_get_acronyms(dataframe))
        patterns = _clean_terms(patterns)
        patterns.update(_get_project_keywords(dataframe))

        patterns_list = sorted(
            patterns,
            key=lambda x: (len(x.split(" ")), x),
            reverse=True,
        )

        _COMPILED_PATTERNS.extend(
            (pattern, re.compile(r"\b" + re.escape(pattern) + r"\b"))
            for pattern in patterns_list
        )

        _COMPILED_PATTERNS.sort(
            key=lambda x: (len(x[0].split(" ")), x[0]), reverse=True
        )

    return _COMPILED_PATTERNS


# ----------------------------------------------------------------------------
def _highlight_patterns(text):

    if pd.isna(text):
        return text

    text = str(text)
    for phrase, pattern in _COMPILED_PATTERNS:
        if phrase in text:
            text = pattern.sub(lambda m: m.group().upper().replace(" ", "_"), text)

    return text


# ----------------------------------------------------------------------------
def _normalize(text):

    if pd.isna(text):
        return None

    url_matches = extract_urls(text)
    text = mark_copyright(text)
    text = mark_abstract_headings(text)
    text = mark_discursive_patterns(text)
    text = mark_connectors(text)
    #
    text = _highlight_patterns(text)
    #
    text = repair_apostrophes(text)
    text = join_consecutive_descriptors(text)
    text = repair_measurement_units(text)
    text = repair_urls(text, url_matches)
    text = repair_lowercase_text(text)
    text = repair_abstract_headings(text)
    text = repair_et_al(text)
    text = mark_connectors(text)
    text = repair_roman_numbers(text)
    text = repair_emails(text)
    text = repair_strange_cases(text)

    return text


# ----------------------------------------------------------------------------


def uppercase_keyterms(
    source: CorpusField,
    target: CorpusField,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    _get_compiled_patterns(dataframe)

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        dataframe[target.value] = dataframe[source.value].parallel_apply(_normalize)

    save_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[target.value].notna().sum())
