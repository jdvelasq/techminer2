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
from typing import Dict, List, Optional, Tuple

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ....internals import load_package_stopwords


def internal__extract_meaningful_words(
    source_field,
    dest_field,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    record_years_range: Tuple[Optional[int], Optional[int]],
    record_citations_range: Tuple[Optional[int], Optional[int]],
    records_order_by: Optional[str],
    records_match: Optional[Dict[str, List[str]]],
):
    # Register tqdm pandas progress bar
    tqdm.pandas()

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if source_field not in data.columns:
            continue

        data[dest_field] = data[source_field].copy()
        data[dest_field] = data[dest_field].str.lower()
        data[dest_field] = data[dest_field].map(
            lambda paragraph: TextBlob(paragraph).sentences, na_action="ignore"
        )
        data[dest_field] = data[dest_field].map(
            lambda sentences: [sentence.tags for sentence in sentences],
            na_action="ignore",
        )
        data[dest_field] = data[dest_field].map(
            lambda tagged_sentences: [
                tag
                for tagged_sentence in tagged_sentences
                for tag in tagged_sentence
                if tag[1][:2] in ["NN", "VB", "RB", "JJ"]
            ]
        )
        data[dest_field] = data[dest_field].map(
            lambda tagged_words: [to_lemma(tag) for tag in tagged_words],
            na_action="ignore",
        )
        data[dest_field] = data[dest_field].map(
            lambda tagged_words: [tag[0] for tag in tagged_words], na_action="ignore"
        )
        data[dest_field] = data[dest_field].map(
            lambda phrases: [
                phrase for phrase in phrases if not phrase.startswith("//")
            ],
            na_action="ignore",
        )
        data[dest_field] = data[dest_field].map(
            lambda phrases: [phrase.replace("'", "") for phrase in phrases],
            na_action="ignore",
        )
        data[dest_field] = data[dest_field].map(
            lambda phrases: [
                phrase for phrase in phrases if not re.search(r"[^\w\s]", phrase)
            ],
            na_action="ignore",
        )
        data[dest_field] = data[dest_field].map(
            lambda phrases: [phrase for phrase in phrases if phrase != ""],
            na_action="ignore",
        )
        #
        #
        data[dest_field] = data[dest_field].map(set, na_action="ignore")
        data[dest_field] = data[dest_field].map(sorted, na_action="ignore")
        stopwords = [word.lower() for word in load_package_stopwords()]
        data[dest_field] = data[dest_field].map(
            lambda terms: [term for term in terms if term.lower() not in stopwords],
            na_action="ignore",
        )
        data[dest_field] = data[dest_field].str.join("; ")
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
