"""
Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine._intern.match import BaseSeparatorMatch
    >>> (
    ...     BaseSeparatorMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_NORM)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

import sys

import pandas as pd  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField

from ._intern import (
    add_padding,
    compute_matches,
    load_thesaurus,
    remove_builtin_stopwords,
    remove_punctuation,
    remove_thesaurus_stopwords,
    report_matches,
    sort_words,
    string_to_words,
    words_to_string,
)

stemmer = PorterStemmer()


SIGNATURE = ThField.SIGNATURE.value


class BaseSeparatorMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)  # type: ignore
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _separator_to_space(thesaurus_df=thesaurus_df)
        thesaurus_df = string_to_words(thesaurus_df=thesaurus_df)
        thesaurus_df = sort_words(thesaurus_df=thesaurus_df)
        thesaurus_df = words_to_string(thesaurus_df=thesaurus_df)

        matches = compute_matches(thesaurus_df=thesaurus_df, params=self.params)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def _separator_to_space(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()

    for c in "-_/.,;:()":
        thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
            c, " ", regex=False
        )

    return thesaurus_df
