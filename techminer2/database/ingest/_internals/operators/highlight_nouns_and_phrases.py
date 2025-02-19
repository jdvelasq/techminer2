# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Replace descriptors in abstracts and titles"""

import pathlib
import re

import pandas as pd  # type: ignore
import spacy
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ....._internals.log_message import internal__log_message
from .....package_data.text_processing import internal__load_text_processing_terms


def internal__highlight_nouns_and_phrases(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    """:meta private:"""

    internal__log_message(f"Highlighting tokens in '{source}' field.", prompt_flag=True)

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    if source not in dataframe.columns:
        return

    dataframe[dest] = (
        dataframe[source].str.lower().str.replace("_", " ").str.replace(" / ", " ")
    )

    author_and_index_keywords = collect_author_and_index_keywords(root_dir)
    author_and_index_keywords = clean_author_and_index_keywords(
        author_and_index_keywords
    )

    known_noun_phrases = internal__load_text_processing_terms("known_noun_phrases.txt")

    spacy_nlp = spacy.load("en_core_web_sm")

    stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
    connectors = internal__load_text_processing_terms("connectors.txt")
    determiners = internal__load_text_processing_terms("determiners.txt")
    determiners = (
        "(" + "|".join(["^" + determiner + r"\s" for determiner in determiners]) + ")"
    )
    determiners = re.compile(determiners)

    for index, row in tqdm(
        dataframe.iterrows(), total=len(dataframe), desc="         "
    ):

        if pd.isna(row[dest]):
            continue

        text = row[dest]

        #
        # Step 1: Collect noun phrases using different packages
        #
        key_terms = []

        # TextBlob
        key_terms += [str(phrase) for phrase in TextBlob(text).noun_phrases]

        # spaCy
        spacy_key_terms = [chunk.text for chunk in spacy_nlp(text).noun_chunks]
        # spacy_key_terms = [
        #     re.sub(determiners, "", term).strip() for term in spacy_key_terms
        # ]
        key_terms += spacy_key_terms

        #
        # Step 2: Remove stopwords and phrases with numbers
        #
        key_terms = list(set(key_terms))
        key_terms = [term for term in key_terms if term not in stopwords]
        key_terms = [term for term in key_terms if "(" not in term]
        key_terms = [term for term in key_terms if "," not in term]
        key_terms = [
            term for term in key_terms if not any(char.isdigit() for char in term)
        ]

        #
        # Step 3: Adds author and index keywords / known noun phrases
        #
        key_terms += [k for k in author_and_index_keywords if k in row[dest]]
        key_terms += [k for k in known_noun_phrases if k in row[dest]]

        #
        # Step 4: Replace noun phrases and authors and index keywords in the text
        #
        key_terms = sorted(
            key_terms,
            key=lambda x: (len(x.split(" ")), x),
            reverse=True,
        )

        current_connectors = [t for t in connectors if t in row[dest]]
        if len(current_connectors) > 0:
            regex = "|".join([re.escape(phrase) for phrase in current_connectors])
            regex = re.compile(r"\b(" + regex + r")\b")
            text = re.sub(regex, lambda z: z.group().lower().replace(" ", "_"), text)

        if len(key_terms) > 0:
            regex = "|".join([re.escape(phrase) for phrase in key_terms])
            regex = re.compile(r"\b(" + regex + r")\b")
            text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

        #
        #
        # Step 5: Replace THE_AUTHOR in copyright phrase
        #
        # YYYY THE_AUTHOR ( s ) .
        pattern = re.compile(r"\b\d{4} THE_AUTHOR \( s \) \.", re.IGNORECASE)
        text = re.sub(pattern, lambda z: z.group().lower().replace("_", " "), text)
        #
        # THE_AUTHOR ( s ) YYYY.
        pattern = re.compile(r"THE_AUTHOR \( s \) \d{4} \.", re.IGNORECASE)
        text = re.sub(pattern, lambda z: z.group().lower().replace("_", " "), text)

        dataframe.loc[index, dest] = text

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def collect_author_and_index_keywords(root_dir):

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"
    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
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
    ## terms = [term for term in terms if len(term.split(" ")) > 1]
    terms = sorted(terms, key=lambda x: (len(x.split(" ")), x), reverse=True)
    assert "it" not in terms
    return terms
