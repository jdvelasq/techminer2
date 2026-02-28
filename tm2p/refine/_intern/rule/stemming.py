from functools import lru_cache

import pandas as pd  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore

from tm2p import ThesaurusField
from tm2p._intern import Params

from ._pre_process import _pre_process
from .fuzzy_cutoff_0_word import _report_mergings
from .wordorder import (
    _compute_matches,
    _remove_stopwords,
    _string_to_words,
    _words_to_string,
)

stemmer = PorterStemmer()

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def apply_stemming_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)

    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED]

    thesaurus_df = _remove_stopwords(thesaurus_df=thesaurus_df)
    thesaurus_df = _string_to_words(thesaurus_df=thesaurus_df)
    thesaurus_df = _words_to_stems(thesaurus_df=thesaurus_df)
    thesaurus_df = _words_to_string(thesaurus_df=thesaurus_df)

    matches = _compute_matches(thesaurus_df=thesaurus_df)

    _report_mergings(
        params=params,
        mapping=matches,
        filename="candidate_mergings.txt",
    )

    return thesaurus_df


@lru_cache(maxsize=None)
def stem(word: str) -> str:
    """Apply Porter stemming algorithm with caching."""
    return stemmer.stem(word)


def _words_to_stems(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda x: [stem(word) for word in x]
    )
    return thesaurus_df
