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

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ...internals.stopwords.load_package_stopwords import load_package_stopwords


def transformations__extract_meaningful_words(
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
        data[dest] = data[dest].map(
            lambda phrases: [
                phrase for phrase in phrases if not phrase.startswith("//")
            ],
            na_action="ignore",
        )
        data[dest] = data[dest].map(
            lambda phrases: [phrase.replace("'", "") for phrase in phrases],
            na_action="ignore",
        )
        data[dest] = data[dest].map(
            lambda phrases: [
                phrase for phrase in phrases if not re.search(r"[^\w\s]", phrase)
            ],
            na_action="ignore",
        )
        data[dest] = data[dest].map(
            lambda phrases: [phrase for phrase in phrases if phrase != ""],
            na_action="ignore",
        )
        #
        #
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
