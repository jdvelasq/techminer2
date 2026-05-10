import string
import sys
from typing import Optional

import pandas as pd  # type: ignore
import spacy
import yake
from pandarallel import pandarallel  # type: ignore

from tm2p._intern import stdout_to_stderr
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import Field

spacy_nlp = spacy.load("en_core_web_lg")

DETERMINERS = load_builtin_word_list("determiners.txt")
DISCOURSE_CONNECTORS = load_builtin_word_list("discourse_connectors.txt")
STOPWORDS = load_builtin_word_list("stopwords.txt")

YAKE_EXTRACTOR = yake.KeywordExtractor(
    lan="en",
    n=4,
    dedupLim=0.9,
    top=10,
    features=None,
)


def s07_np_yake(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory=root_directory)

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        df[Field.NP_YAKE.value] = df.parallel_apply(  # type: ignore
            _process_row,
            axis=1,
        )
        sys.stderr.write("\n")

    save_main_csv_zip(df=df, root_directory=root_directory)

    phrases = df[Field.NP_YAKE.value].dropna()
    phrases = phrases.str.split("; ").explode()
    phrases = phrases.drop_duplicates()
    n_phrases = len(phrases)

    return n_phrases


def _process_row(row: pd.Series) -> Optional[str]:

    title = Field.ABSTR_RAW.value
    abstr = Field.TITLE_RAW.value

    phrases: list[str] = []

    import sys

    if not pd.isna(row[abstr]):
        terms = YAKE_EXTRACTOR.extract_keywords(row[abstr])
        phrases.extend(term for term, _ in terms if len(term) > 3)

    if not pd.isna(row[title]):
        terms = YAKE_EXTRACTOR.extract_keywords(row[title])
        phrases.extend(term for term, _ in terms if len(term) > 3)

    if not phrases:
        return None

    phrases = [phrase.strip().lower() for phrase in phrases]

    for determiner in DETERMINERS:
        phrases = [
            term[len(determiner) + 1 :] if term.startswith(determiner + " ") else term
            for term in phrases
        ]

    for connector in DISCOURSE_CONNECTORS:
        phrases = [
            term[len(connector) + 1 :] if term.startswith(connector + " ") else term
            for term in phrases
        ]

    for stopword in STOPWORDS:
        phrases = [
            term[len(stopword) + 1 :] if term.startswith(stopword + " ") else term
            for term in phrases
        ]

    punctuation = set(string.punctuation.replace("_", ""))
    phrases = [
        term for term in phrases if not any(char in term for char in punctuation)
    ]

    vowels = set("aeiou")
    phrases = [term for term in phrases if any(char in vowels for char in term)]

    phrases = list(dict.fromkeys(phrases))
    phrases_str = "; ".join(sorted(phrases))

    return phrases_str
