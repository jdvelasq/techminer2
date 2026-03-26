"""
Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine._intern.match import BaseBiGramMatch
    >>> (
    ...     BaseBiGramMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_RAW)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    '917 synonym groups found'

"""

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import ParamsMixin

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


class BaseBiGramMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> str:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _bigrams(thesaurus_df=thesaurus_df)

        matches = compute_matches(thesaurus_df=thesaurus_df, params=self.params)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        return f"{len(matches)} synonym groups found"


def _bigrams(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    def _generate(text: str) -> list[str]:
        bigrams = ["".join(text[i : i + 2]) for i in range(len(text) - 1)]
        return bigrams

    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(r" ", "", regex=False)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(_generate)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(set)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join("")

    return thesaurus_df
