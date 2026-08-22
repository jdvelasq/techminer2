import re
import sys
from typing import Optional

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from tm2p._intern import stdout_to_stderr
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import Field

from ._file_dispatch import get_file_operations
from .helpers import (
    extract_urls,
    join_consecutive_descriptors,
    mark_abstract_headings,
    mark_copyright,
    mark_discursive_patterns,
    mark_scaffolding,
    remove_single_word_noise,
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

_PATTERNS: list[str] = []


def _prepare_patterns(df: pd.DataFrame) -> None:

    def _update_with_project_noun_phrases(patterns: set[str]) -> set[str]:
        for column in [
            Field.NP_SPACY.value,
            Field.NP_TEXTBLOB.value,
            # -----------------------
            # Field.NP_GENSIM.value,
            # Field.NP_YAKE.value,
            # -----------------------
            Field.NP_KNOWN.value,
        ]:
            if column in df.columns:
                for entry in df[column].dropna():
                    phrases = [phrase.strip() for phrase in entry.split(";")]
                    patterns.update(phrases)
        return patterns

    def _update_with_acronyms(patterns: set[str]) -> set[str]:
        if Field.ACRONYM.value in df.columns:
            for entry in df[Field.ACRONYM.value].dropna():
                phrases = [phrase.strip() for phrase in entry.split(";")]
                patterns.update(phrases)
        return patterns

    def _update_with_project_keywords(patterns: set[str]) -> set[str]:
        for column in [
            Field.AUTHKW_TOK.value,
            Field.IDXKW_TOK.value,
        ]:
            if column in df.columns:
                series = df[column].dropna()
                series = series.str.replace(r"[\"'#!]", "", regex=True)
                series = series.str.replace(r"\(.*\)", "", regex=True)
                series = series.str.replace(r"\[.*\]", "", regex=True)
                series = series.str.replace("-", " ", regex=False)
                series = series.str.lower()
                series = series.str.split("; ")
                series = series.explode()
                series = series.str.strip()  # type: ignore
                series = series[series.str.len() > 2]
                series = series[~series.str.contains(r"\d", regex=True)]
                series = series.str.strip()
                patterns.update(series)
        return patterns

    def _update_with_builtin_noun_phrases(patterns: set[str]) -> set[str]:
        patterns.update(
            phrase.strip().lower().replace("_", " ").strip()
            for phrase in load_builtin_word_list("noun_phrases.txt")
            if phrase.strip()
        )
        return patterns

    def _clean_patterns(patterns: set[str]) -> set[str]:

        stopwords = load_builtin_word_list("stopwords.txt")
        patterns = patterns - set(
            t.strip()
            for t in patterns
            if t in stopwords or len(t) <= 1 or "(" in t or "," in t
            # or any(char.isdigit() for char in t)
        )

        return patterns

    patterns: set[str] = set()

    patterns = _update_with_project_noun_phrases(patterns)
    patterns = _update_with_acronyms(patterns)
    patterns = _update_with_project_keywords(patterns)
    patterns = _update_with_builtin_noun_phrases(patterns)
    patterns = _clean_patterns(patterns)

    patterns_list = sorted(
        patterns,
        key=lambda x: (len(x.split(" ")), x),
        reverse=True,
    )

    patterns_list = [pattern.replace("-", " ") for pattern in patterns_list]

    _PATTERNS.extend(patterns_list)


# ----------------------------------------------------------------------------
def _highlight_meaningful_terms(text):

    if pd.isna(text):
        return text
    text = str(text)
    for pattern in _PATTERNS:
        if pattern in text:
            text = text.replace(
                f" {pattern} ", f" {pattern.upper().replace(' ', '_')} "
            )

            if "co2" in pattern:
                print()
                print("----- co2 -----")
                print()
                print(text)
                print()
                print()

    return text


def _repair_meaningful_terms(text):

    def _repair_parenthetical_terms(text):
        text = re.sub(
            r"\( ([a-z][a-z]+) \)",
            lambda m: f"( {m.group(1).upper()} )",
            text,
        )
        return text

    def _propagate_parenthetical_terms(text):

        pat = r"\( ([A-Z][A-Z0-9]{0,4}) \)"

        terms = list({match.lower() for match in re.findall(pat, text)})
        terms = [
            t for t in terms if len(t) > 1 and t.lower() not in ("is", "the", "it")
        ]
        for term in terms:
            pattern_word = rf" {re.escape(term)} "
            text = re.sub(pattern_word, f" {term.upper()} ", text, flags=re.IGNORECASE)

        return text

    def _repair_mixed_case_terms(text):

        pat = r" (?=[A-Za-z_]*[a-z])(?=[A-Za-z_]*[A-Z])[A-Za-z]+(?:_[A-Za-z]+)* "

        text = re.sub(
            pat,
            lambda m: m.group(0).upper(),
            text,
        )

        return text

    text = _repair_parenthetical_terms(text)
    text = _propagate_parenthetical_terms(text)
    text = _repair_mixed_case_terms(text)

    return text


# ----------------------------------------------------------------------------
def _normalize(text):

    if pd.isna(text):
        return None

    try:
        url_matches = extract_urls(text)
        text = mark_copyright(text)
        text = mark_abstract_headings(text)
        text = mark_discursive_patterns(text)
        text = mark_scaffolding(text)
        #
        text = _highlight_meaningful_terms(text)
        #
        text = repair_apostrophes(text)
        text = join_consecutive_descriptors(text)
        text = repair_measurement_units(text)
        text = repair_urls(text, url_matches)
        text = repair_lowercase_text(text)
        text = repair_abstract_headings(text)
        text = repair_et_al(text)
        text = mark_scaffolding(text)
        text = repair_roman_numbers(text)
        text = repair_emails(text)
        text = repair_strange_cases(text)
        text = remove_single_word_noise(text)

        text = mark_copyright(text)
        text = _repair_meaningful_terms(text)

    except Exception as e:
        sys.stderr.write(f"Error processing text: {e}\n")
        sys.stderr.flush()
        raise e

    return text


# ----------------------------------------------------------------------------


def uppercase_keyterms(
    source: Field,
    target: Field,
    root_directory: str,
    na_action: Optional[str] = None,
) -> int:

    load_data, save_data, get_path = get_file_operations()

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        if na_action == "ignore":
            return 0
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    _prepare_patterns(dataframe)

    dataframe[target.value] = dataframe[source.value].copy()

    dataframe[target.value] = dataframe[target.value].map(
        lambda x: f" {x} " if pd.notna(x) else x
    )

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        dataframe[target.value] = dataframe[target.value].parallel_apply(_normalize)
        sys.stderr.write("\n")

    dataframe[target.value] = dataframe[target.value].str.strip()

    save_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[target.value].notna().sum())
