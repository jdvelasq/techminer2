"""
Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine._intern.match import BaseBeiderMorseMatch
    >>> (
    ...     BaseBeiderMorseMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_RAW)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    '892 synonym groups found'

"""

import pandas as pd  # type: ignore
from abydos.phonetic import BeiderMorse  # type: ignore

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

bm = BeiderMorse()


PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
OLD = ThField.OLD.value


class BaseBeiderMorseMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _beider_morse(thesaurus_df=thesaurus_df)

        matches = compute_matches(thesaurus_df=thesaurus_df, params=self.params)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        return f"{len(matches)} synonym groups found"


def _beider_morse(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split(" ")
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda words: ["".join(bm.encode(word)) for word in words]
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(set)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")

    return thesaurus_df
