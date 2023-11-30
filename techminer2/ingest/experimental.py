# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
>>> from techminer2.ingest import experimental
>>> experimental(root_dir="example/")

"""


import glob
import os.path
import re

import pandas as pd
from textblob import TextBlob  # type: ignore
from tqdm import tqdm

from ..fields.merge_fields import _merge_fields


def experimental(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # STEP 1:
    # Generates a new field with noun phrases in upper case and underscore

    # _mark_noun_phrases(
    #     source="document_title",
    #     dest="raw_title_nlp_phrases",
    #     root_dir=root_dir,
    # )

    # _mark_noun_phrases(
    #     source="abstract",
    #     dest="raw_abstract_nlp_phrases",
    #     root_dir=root_dir,
    # )

    # STEP 2:
    # mark keywords perserving noun phrases

    _mark_keywords(
        column="raw_author_keywords",
        source="document_title",
        dest="raw_title_nlp_phrases",
        root_dir=root_dir,
    )

    # _mark_keywords(
    #     column="raw_index_keywords",
    #     source="raw_title_nlp_phrases",
    #     dest="raw_title_nlp_phrases",
    #     root_dir=root_dir,
    # )

    _mark_keywords(
        column="raw_author_keywords",
        source="abstract",
        dest="raw_abstract_nlp_phrases",
        root_dir=root_dir,
    )

    # _mark_keywords(
    #     column="raw_index_keywords",
    #     source="raw_abstract_nlp_phrases",
    #     dest="raw_abstract_nlp_phrases",
    #     root_dir=root_dir,
    # )

    # STEP 3:
    # extract nouns
    _extract_nouns(
        source="raw_title_nlp_phrases",
        dest="raw_title_nlp_phrases",
        root_dir=root_dir,
    )

    _extract_nouns(
        source="raw_abstract_nlp_phrases",
        dest="raw_abstract_nlp_phrases",
        root_dir=root_dir,
    )

    # STEP 4:
    # Merge nouns
    _merge_fields(
        sources=["raw_title_nlp_phrases", "raw_abstract_nlp_phrases"],
        dest="raw_nlp_phrases",
        root_dir=root_dir,
    )

    ## ------------------------------------------------------------------------------------------
    ## Ignore thesaurus creation for testing new cleaning process

    # file = os.path.join(root_dir, "databases/_main.csv.zip")
    # data_frame = pd.read_csv(file, encoding="utf-8", compression="zip")
    # words = (
    #     data_frame["raw_nlp_phrases"]
    #     .dropna()
    #     .str.split("; ", expand=False)
    #     .explode()
    #     .str.strip()
    #     .drop_duplicates()
    #     .sort_values()
    #     .to_list()
    # )

    # thesaurus_file = os.path.join(root_dir, "thesauri/nlp_phrases.the.txt")
    # with open(thesaurus_file, "w", encoding="utf-8") as f:
    #     for word in words:
    #         f.write(word + "\n")
    #         f.write("    " + word + "\n")

    ## ------------------------------------------------------------------------------------------


def _mark_noun_phrases(
    source,
    dest,
    root_dir,
):
    tqdm.pandas()

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if source not in data.columns:
            continue
        data[dest] = data[source].progress_apply(_extract_noun_phrases)
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def _extract_noun_phrases(text):
    #
    if not isinstance(text, str):
        return pd.NA

    text = text.lower().replace("_", " ")

    noun_phrases = [str(phrase) for phrase in TextBlob(text.lower()).noun_phrases]
    #
    noun_phrases = [phrase for phrase in noun_phrases if not phrase.startswith("//")]
    # noun_phrases = [phrase.replace("'", "") for phrase in noun_phrases]
    noun_phrases = [
        phrase for phrase in noun_phrases if not re.search(r"[^\w\s]", phrase)
    ]
    noun_phrases = [phrase for phrase in noun_phrases if phrase not in ""]

    #
    # MODIFICACION:
    ## noun_phrases = [phrase.upper() for phrase in noun_phrases]
    noun_phrases = [phrase.replace(" ", "_") for phrase in noun_phrases]
    ## return "; ".join(set(noun_phrases))

    #
    # transform noun phrases to upper cases and replace space with underscore
    if len(noun_phrases) > 0:
        regex = "|".join(
            [re.escape(phrase.replace("_", " ")) for phrase in noun_phrases]
        )
        regex = re.compile(r"\b(" + regex + r")\b")
        text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

    return text


def _mark_keywords(
    column,
    source,
    dest,
    root_dir,
):
    tqdm.pandas()

    keywords = _collect_keywords(root_dir=root_dir, column=column)
    regex = "|".join(
        [re.escape(keyword.lower().replace("_", " ")) for keyword in keywords]
    )
    regex = re.compile(r"\b(" + regex + r")\b")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if source not in data.columns:
            continue
        data[dest] = (
            data[source]
            .str.lower()
            .str.replace("_", " ")
            .str.replace(
                regex, lambda z: z.group().upper().replace(" ", "_"), regex=True
            )
        )
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def _collect_keywords(
    column,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    keywords = []
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if column in data.columns:
            keywords.append(data[column].dropna())
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    keywords = pd.concat(keywords)
    keywords = (
        keywords.str.split(";")
        .explode()
        .str.strip()
        .str.lower()
        .dropna()
        .drop_duplicates()
    )
    keywords = keywords[~keywords.str.contains(r"[^\w\s]", regex=True)]
    keywords = keywords.to_list()
    keywords = sorted(keywords, key=len, reverse=True)

    return keywords


def _extract_nouns(
    source,
    dest,
    root_dir,
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if source not in data.columns:
            continue
        data[dest] = data[source].progress_apply(_process_text)
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def _process_text(text):
    if not isinstance(text, str):
        return pd.NA

    words = TextBlob(text).words
    words = [str(word) for word in words]
    words = [word for word in words if not re.search(r"^\d+$", word)]
    words = [word for word in words if not re.search(r"^\d", word)]
    words = [word.replace("'", "") for word in words]
    words = [word for word in words if word == word.upper()]
    words = "; ".join(set(words))

    return words

    # tags = TextBlob(text).tags
    # noun_phrases = sorted(set(tag[0].upper() for tag in tags if tag[1][:2] == "NN"))
    # #
    # #
    # noun_phrases = [phrase for phrase in noun_phrases if not phrase.startswith("//")]
    # noun_phrases = [phrase.replace("'", "") for phrase in noun_phrases]
    # noun_phrases = [
    #     phrase for phrase in noun_phrases if not re.search(r"[^\w\s]", phrase)
    # ]
    # noun_phrases = [phrase for phrase in noun_phrases if phrase not in ""]
    # #
    # #
    # noun_phrases = "; ".join(set(noun_phrases))

    # return noun_phrases
