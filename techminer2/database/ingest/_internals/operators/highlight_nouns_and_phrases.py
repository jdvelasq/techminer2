# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Replace descriptors in abstracts and titles"""

import pathlib
import re
import sys

import pandas as pd  # type: ignore
import spacy
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ....._internals import Params
from ....._internals.log_message import internal__log_message
from .....package_data.text_processing import internal__load_text_processing_terms
from ...._internals.io import (
    internal__load_all_records_from_database,
    internal__write_records_to_database,
)


# ------------------------------------------------------------------------------
def notify_process_start(source):
    sys.stderr.write(f"Highlighting tokens in '{source}' field\n")
    sys.stderr.flush()


# ------------------------------------------------------------------------------
def load_all_records_from_database(root_directory):
    params = Params(root_directory=root_directory)
    records = internal__load_all_records_from_database(params)
    return records


# ------------------------------------------------------------------------------
def write_records_to_database(dataframe, root_directory):
    params = Params(root_directory=root_directory)
    internal__write_records_to_database(params=params, records=dataframe)


# ------------------------------------------------------------------------------
def prepare_dest_field(dataframe, source, dest):

    dataframe = dataframe.copy()
    dataframe[dest] = (
        dataframe[source].str.lower().str.replace("_", " ").str.replace(" / ", " ")
    )
    return dataframe


# ------------------------------------------------------------------------------
def collect_author_and_index_keywords(root_directory):

    database_file = pathlib.Path(root_directory) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    terms = []
    for column in [
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        if column in dataframe.columns:
            terms.append(dataframe[column].dropna().copy())

    terms = pd.concat(terms)
    terms = terms.reset_index(drop=True)

    return terms


# ------------------------------------------------------------------------------
def clean_author_and_index_keywords(terms):

    terms = terms.str.translate(str.maketrans("", "", "\"'#!"))
    terms = terms.str.replace(re.compile(r"\(.*\)"), "", regex=True)
    terms = terms.str.replace(re.compile(r"\[.*\]"), "", regex=True)
    terms = terms.str.translate(str.maketrans("_", " "))
    terms = terms.str.lower()
    terms = terms.str.split("; ")
    terms = terms.explode()
    terms = terms.str.strip()
    terms = terms.drop_duplicates()
    terms = terms.to_list()
    terms = [term for term in terms if len(term) > 2]
    terms = [term for term in terms if not any(char.isdigit() for char in term)]
    terms = sorted(terms, key=lambda x: (len(x.split(" ")), x), reverse=True)
    assert "it" not in terms
    return terms


# ------------------------------------------------------------------------------
def internal__highlight_nouns_and_phrases(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_directory,
):
    """:meta private:"""

    notify_process_start(source)
    dataframe = load_all_records_from_database(root_directory)

    if source not in dataframe.columns:
        return

    dataframe = prepare_dest_field(dataframe, source, dest)

    author_and_index_keywords = collect_author_and_index_keywords(root_directory)
    author_and_index_keywords = clean_author_and_index_keywords(
        author_and_index_keywords
    )

    known_noun_phrases = internal__load_text_processing_terms("known_noun_phrases.txt")
    known_noun_phrases = [
        phrase.lower().replace("_", " ") for phrase in known_noun_phrases
    ]

    spacy_nlp = spacy.load("en_core_web_sm")

    connectors = internal__load_text_processing_terms("connectors.txt")
    copyright_regex = internal__load_text_processing_terms("copyright_regex.txt")
    stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
    discursive_patterns = internal__load_text_processing_terms(
        "discursive_patterns.txt"
    )

    determiners = internal__load_text_processing_terms("determiners.txt")
    determiners = (
        "(" + "|".join(["^" + determiner + r"\s" for determiner in determiners]) + ")"
    )
    determiners = re.compile(determiners)

    for index, row in tqdm(
        dataframe.iterrows(),
        total=len(dataframe),
        desc=f"  Progress",
        ncols=80,
    ):

        if pd.isna(row[dest]):
            continue

        text = row[dest]

        key_terms = []

        #
        # Step 1: Extract all texts between parentheses and then, add them to the key_terms
        #
        abbreviations = re.findall(r"\((.*?)\)", text)
        abbreviations = [t.strip() for t in abbreviations]
        abbreviations = [t for t in abbreviations if all(c.isalnum() for c in t)]
        abbreviations = list(set(abbreviations))
        key_terms += abbreviations

        #
        # Step 2: Collect noun phrases using TextBlob
        #
        key_terms += [str(phrase) for phrase in TextBlob(text).noun_phrases]

        #
        # Step 3: Collect noun phrases using spaCy
        #
        spacy_key_terms = [chunk.text for chunk in spacy_nlp(text).noun_chunks]
        spacy_key_terms = [term for term in spacy_key_terms if "." not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "(" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if ")" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "[" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "]" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "%" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "&" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "!" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "'" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if '"' not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "+" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "<" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if ">" not in term]
        spacy_key_terms = [term for term in spacy_key_terms if "=" not in term]

        spacy_key_terms = [
            term
            for term in spacy_key_terms
            if "a" in term or "e" in term or "i" in term or "o" in term or "u" in term
        ]
        key_terms += spacy_key_terms

        #
        # Step 4: Remove stopwords and phrases with numbers from key_terms
        #
        key_terms = list(set(key_terms))
        key_terms = [term for term in key_terms if term not in stopwords]
        key_terms = [term for term in key_terms if "(" not in term]
        key_terms = [term for term in key_terms if "," not in term]
        key_terms = [
            term for term in key_terms if not any(char.isdigit() for char in term)
        ]

        #
        # Step 5: Adds author and index keywords / known noun phrases
        #
        key_terms += [k for k in author_and_index_keywords if k in row[dest]]
        key_terms += [k for k in known_noun_phrases if k in row[dest]]

        #
        # Step 6: Mark copyright text
        #
        for regex in copyright_regex:
            regex = r"(" + regex + r")"
            regex = re.compile(regex)
            text = re.sub(regex, lambda z: z.group().replace(" ", "_"), text)

        #
        # Step 7: Mark template abstract compound markers
        #
        for regex in [
            "? academic practical relevance :",
            "? data visualization tools :",
            "? design methodology approach :",
            "? implications of the_study :",
            "? managerial implications :",
            "? methodological quality assessment tools include :",
            "? methodology results :",
            "? originality value :",
            "? practical implications :",
            "? problem definition :",
            "? research limitations :",
            "? research limitations implications :",
            "? research methodology :",
            ". academic practical relevance :",
            ". data visualization tools :",
            ". design methodology approach :",
            ". implications of the study :",
            ". managerial implications :",
            ". methodological quality assessment tools include :",
            ". methodology results :",
            ". originality value :",
            ". practical implications :",
            ". problem definition :",
            ". reporting quality assessment tool :",
            ". research limitations :",
            ". research limitations implications :",
            ". research methodology :",
        ]:
            regex = re.escape(regex)
            regex = r"(" + regex + r")"
            regex = re.compile(regex)
            text = re.sub(regex, lambda z: z.group().replace(" ", "_"), text)

        #
        # Step 8: Mark discursive patterns
        #
        pattern = [t for t in discursive_patterns if t in row[dest]]
        if len(pattern) > 0:
            regex = "|".join([re.escape(phrase) for phrase in pattern])
            regex = re.compile(r"\b(" + regex + r")\b")
            text = re.sub(regex, lambda z: z.group().lower().replace(" ", "_"), text)

        #
        # Step 9: Mark connectors
        #
        current_connectors = [t for t in connectors if t in row[dest]]
        if len(current_connectors) > 0:
            regex = "|".join([re.escape(phrase) for phrase in current_connectors])
            regex = re.compile(r"\b(" + regex + r")\b")
            text = re.sub(regex, lambda z: z.group().lower().replace(" ", "_"), text)

        #
        # Step 10: Highlight key terms
        #
        key_terms = sorted(
            key_terms,
            key=lambda x: (len(x.split(" ")), x),
            reverse=True,
        )
        if len(key_terms) > 0:
            for term in key_terms:
                regex = re.compile(r"\b" + re.escape(term) + r"\b")
                text = re.sub(
                    regex, lambda z: z.group().upper().replace(" ", "_"), text
                )

        #
        # Step 10: Mark consequtive separate terms in uppercase
        #
        for n_terms in range(1, 5):

            pattern = r"\b[A-Z][A-Z_]+" + " [A-Z][A-Z_]+" * n_terms
            matches = re.findall(pattern, text)

            if len(matches) > 0:
                for match in matches:
                    regex = re.compile(r"\b" + re.escape(match) + r"\b")
                    text = re.sub(
                        regex, lambda z: z.group().upper().replace(" ", "_"), text
                    )

        #
        # Step 11: Unmark lowercase text with "_" including abstract markers
        #
        regex = re.compile(r"\b([a-z_\(\)\d])+\b")
        text = re.sub(regex, lambda z: z.group().replace("_", " "), text)

        regex = re.compile(r"\b\._([a-z_\(\)\d])+_:\b")
        text = re.sub(regex, lambda z: z.group().replace("_", " "), text)

        #
        # Step 12: Mark connectors
        #
        current_connectors = [t for t in connectors if t in row[dest]]
        if len(current_connectors) > 0:
            regex = "|".join([re.escape(phrase) for phrase in current_connectors])
            regex = re.compile(r"\b(" + regex + r")\b")
            text = re.sub(regex, lambda z: z.group().lower().replace(" ", "_"), text)

        #
        # Step 13: Remove roman numbers
        #
        roman_numbers = [
            "i",
            "ii",
            "iii",
            "iv",
            "v",
            "vi",
            "vii",
            "viii",
            "ix",
            "x",
        ]
        for roman_number in roman_numbers:
            regex = r"(\( {roman_number.upper()} )\)"
            regex = re.compile(regex, re.IGNORECASE)
            text = re.sub(regex, lambda z: z.group().lower(), text)

        #
        # Step 14: Remove abstract marker words
        #
        for regex in [
            ". APPROACH :",
            ". FINDINGS :",
            ". LIMITATIONS :",
            ". METHOD :",
            ". METHODOLOGY :",
            ". ORIGINALITY :",
            ". RESULT :",
            ". RESULTS :",
            ". UNIQUENESS :",
            "? APPROACH :",
            "? FINDINGS :",
            "? LIMITATIONS :",
            "? METHOD :",
            "? METHODOLOGY :",
            "? ORIGINALITY :",
            "? RESULT :",
            "? RESULTS :",
            "? UNIQUENESS :",
        ]:
            text = text.replace(regex, regex.lower())

        if text.startswith("AIM :"):
            text = text.replace("AIM :", "aim :")
        if text.startswith("PURPOSE :"):
            text = text.replace("PURPOSE :", "purpose :")
        if text.startswith("PROBLEM_DEFINITION :"):
            text = text.replace("PROBLEM_DEFINITION :", "problem definition :")

        #
        # Step 14: Corrections
        #
        # text = text.replace("_,_", "_")
        # text = text.replace("_._", "_")

        dataframe.loc[index, dest] = text

    write_records_to_database(dataframe, root_directory)
