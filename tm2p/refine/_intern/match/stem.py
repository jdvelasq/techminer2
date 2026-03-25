"""
Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine._intern.match import BaseStemMatch
    >>> (
    ...     BaseStemMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.CONCEPT_RAW)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    1

"""

from functools import lru_cache

import pandas as pd  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore

from tm2p import ThField
from tm2p._intern import ParamsMixin

from ._report_matches import report_matches
from .wordorder import (
    _add_padding,
    _compute_matches,
    _load_thesaurus,
    _remove_builtin_stopwords,
    _remove_thesaurus_stopwords,
    _string_to_words,
    _words_to_string,
)

stemmer = PorterStemmer()


SIGNATURE = ThField.SIGNATURE.value


class BaseStemMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        thesaurus_df = _load_thesaurus(params=self.params)
        thesaurus_df = _add_padding(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _string_to_words(thesaurus_df=thesaurus_df)
        thesaurus_df = _words_to_stems(thesaurus_df=thesaurus_df)
        thesaurus_df = _words_to_string(thesaurus_df=thesaurus_df)

        matches = _compute_matches(thesaurus_df=thesaurus_df)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        return 1


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
