import re
import string
import sys
from typing import Optional

import pandas as pd  # type: ignore
import spacy
from gensim.models import Phrases
from gensim.models.phrases import ENGLISH_CONNECTOR_WORDS, Phraser, Phrases
from pandarallel import pandarallel  # type: ignore

from tm2p._intern import stdout_to_stderr
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.packag_data.word_lists import load_builtin_word_list
from tm2p.enum import Field

spacy_nlp = spacy.load("en_core_web_lg")

determiners = load_builtin_word_list("determiners.txt")
discourse_connectors = load_builtin_word_list("discourse_connectors.txt")
stopwords = load_builtin_word_list("stopwords.txt")

MIN_COUNT = 5
THRESHOLD = 10.0

COLLOCATIONS = set()


def s06_np_gensim(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory=root_directory)

    collocations = _extract_collocations(df)

    COLLOCATIONS.update(collocations)

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        df[Field.NP_GENSIM.value] = df.parallel_apply(  # type: ignore
            _process_row,
            axis=1,
        )
        sys.stderr.write("\n")

    save_main_csv_zip(df=df, root_directory=root_directory)

    phrases = df[Field.NP_GENSIM.value].dropna()
    phrases = phrases.str.split("; ").explode()
    phrases = phrases.drop_duplicates()
    n_phrases = len(phrases)

    return n_phrases


def _extract_collocations(df: pd.DataFrame) -> set[str]:

    abstracts = df[Field.ABSTR_TOK.value].dropna().to_list()
    abstracts = [abstract.split(" ") for abstract in abstracts]

    bigram_model = Phrases(
        abstracts,
        min_count=MIN_COUNT,
        threshold=THRESHOLD,
        connector_words=ENGLISH_CONNECTOR_WORDS,  # type: ignore
    )
    bigram_phraser = Phraser(bigram_model)

    bigram_corpus = [bigram_phraser[tokens] for tokens in abstracts]
    trigram_model = Phrases(
        bigram_corpus,
        min_count=MIN_COUNT,
        threshold=THRESHOLD,
    )
    trigram_phraser = Phraser(trigram_model)

    collocations = set()
    for tokens in trigram_phraser[bigram_corpus]:
        for token in tokens:
            if "_" in token and len(token) > 4:
                collocations.add(token)

    phrases = set(text.replace("_", " ") for text in collocations)

    for determiner in determiners:
        phrases = [
            term[len(determiner) + 1 :] if term.startswith(determiner + " ") else term
            for term in phrases
        ]

    for connector in discourse_connectors:
        phrases = [
            term[len(connector) + 1 :] if term.startswith(connector + " ") else term
            for term in phrases
        ]

    for stopword in stopwords:
        phrases = [
            term[len(stopword) + 1 :] if term.startswith(stopword + " ") else term
            for term in phrases
        ]

    punctuation = set(string.punctuation.replace("_", ""))
    phrases = set(
        term for term in phrases if not any(char in term for char in punctuation)
    )

    # sys.stderr.write(f"Extracted {len(phrases)} collocations\n")
    # sys.stderr.write("\n".join(phrases))

    return phrases


def _process_row(row: pd.Series) -> Optional[str]:

    title = Field.ABSTR_TOK.value
    abstr = Field.TITLE_TOK.value

    phrases: list[str] = []

    import sys

    if not pd.isna(row[abstr]):
        phrases.extend(
            collocation for collocation in COLLOCATIONS if collocation in row[abstr]
        )

    if not pd.isna(row[title]):
        phrases.extend(
            collocation for collocation in COLLOCATIONS if collocation in row[title]
        )

    if not phrases:
        return None

    phrases_str = "; ".join(sorted(phrases))

    return phrases_str
