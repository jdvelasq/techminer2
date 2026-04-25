"""
Smoke tests:
    >>> from tm2p.enum import ThFile, AnalysisUnit
    >>> from tm2p.refine._intern.match import BaseColognePhoneticsMatch
    >>> (
    ...     BaseColognePhoneticsMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )



"""

import sys

import cologne_phonetics  # type: ignore
import pandas as pd  # type: ignore

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
)

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
OLD = ThField.OLD.value


class BaseColognePhoneticsMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)  # type: ignore
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _cologne(thesaurus_df=thesaurus_df)

        matches = compute_matches(thesaurus_df=thesaurus_df, params=self.params)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def _cologne(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split(" ")
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda words: [cologne_phonetics.encode(word)[0][1] for word in words]
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(set)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")

    return thesaurus_df
