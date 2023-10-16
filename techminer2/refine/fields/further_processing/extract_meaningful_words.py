# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os.path
import re

import pandas as pd
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from tqdm import tqdm

from ...._stopwords import load_package_stopwords
from ..protected_fields import PROTECTED_FIELDS

#
# A lemmatizer is defined to use in each cell of the dataframe
lemmatizer = WordNetLemmatizer()


def to_lemma(tag):
    if tag[0] == tag[0].upper():
        return tag
    if tag[1][:2] == "NN":
        return (lemmatizer.lemmatize(tag[0], pos="n"), tag[1])
    if tag[1][:2] == "VB":
        return (lemmatizer.lemmatize(tag[0], pos="v"), tag[1])
    if tag[1][:2] == "RB":
        return (lemmatizer.lemmatize(tag[0], pos="r"), tag[1])
    if tag[1][:2] == "JJ":
        return (lemmatizer.lemmatize(tag[0], pos="a"), tag[1])
    return None


#
#


def extract_meaningful_words(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _extract_meaningful_words(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _extract_meaningful_words(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    # Register tqdm pandas progress bar
    tqdm.pandas()

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if source not in data.columns:
            continue

        data[dest] = data[source].copy()
        data[dest] = data[dest].str.lower()
        data[dest] = data[dest].map(
            lambda paragraph: TextBlob(paragraph).sentences, na_action="ignore"
        )
        data[dest] = data[dest].map(
            lambda sentences: [sentence.tags for sentence in sentences],
            na_action="ignore",
        )
        data[dest] = data[dest].map(
            lambda tagged_sentences: [
                tag
                for tagged_sentence in tagged_sentences
                for tag in tagged_sentence
                if tag[1][:2] in ["NN", "VB", "RB", "JJ"]
            ]
        )
        data[dest] = data[dest].map(
            lambda tagged_words: [to_lemma(tag) for tag in tagged_words],
            na_action="ignore",
        )
        data[dest] = data[dest].map(
            lambda tagged_words: [tag[0] for tag in tagged_words], na_action="ignore"
        )
        data[dest] = data[dest].map(set, na_action="ignore")
        data[dest] = data[dest].map(sorted, na_action="ignore")
        stopwords = [word.lower() for word in load_package_stopwords()]
        data[dest] = data[dest].map(
            lambda terms: [term for term in terms if term.lower() not in stopwords],
            na_action="ignore",
        )
        data[dest] = data[dest].str.join("; ")
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
