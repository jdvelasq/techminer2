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

NOUN_PHRASES = load_builtin_word_list("noun_phrases.txt")


def s08_np_known(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory=root_directory)

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        df[Field.NP_KNOWN.value] = df.parallel_apply(  # type: ignore
            _process_row,
            axis=1,
        )
        sys.stderr.write("\n")

    save_main_csv_zip(df=df, root_directory=root_directory)

    phrases = df[Field.NP_KNOWN.value].dropna()
    phrases = phrases.str.split("; ").explode()
    phrases = phrases.drop_duplicates()
    n_phrases = len(phrases)

    return n_phrases


def _process_row(row: pd.Series) -> Optional[str]:

    title = Field.ABSTR_TOK.value
    abstr = Field.TITLE_TOK.value

    phrases: list[str] = []

    import sys

    if not pd.isna(row[abstr]):
        terms = [t for t in NOUN_PHRASES if t in row[abstr].lower()]
        phrases.extend(terms)

    if not pd.isna(row[title]):
        terms = [t for t in NOUN_PHRASES if t in row[title].lower()]
        phrases.extend(terms)

    if not phrases:
        return None

    phrases_str = "; ".join(sorted(phrases))

    return phrases_str
