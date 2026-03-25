"""
Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine._intern.match import BaseWordOrderMatch
    >>> (
    ...     BaseWordOrderMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.CONCEPT_RAW)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    1

"""

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data import load_builtin_word_list
from tm2p.refine._intern.data_access import load_thesaurus_as_dataframe

from ..oper import sort_thesaurus_df_by_occ
from ._report_matches import report_matches

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
OLD = ThField.OLD.value


class BaseWordOrderMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        thesaurus_df = _load_thesaurus(params=self.params)
        thesaurus_df = _add_padding(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _string_to_words(thesaurus_df=thesaurus_df)
        thesaurus_df = _words_to_string(thesaurus_df=thesaurus_df)

        matches = _compute_matches(thesaurus_df=thesaurus_df)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        return 1


def _load_thesaurus(params):

    thesaurus_df = load_thesaurus_as_dataframe(params=params)

    thesaurus_df = sort_thesaurus_df_by_occ(
        params=params,
        thesaurus_df=thesaurus_df,
    )

    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED].str.lower()

    return thesaurus_df


def _add_padding(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[SIGNATURE] = " " + thesaurus_df[SIGNATURE] + " "

    return thesaurus_df


def _remove_padding(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()

    return thesaurus_df


def _remove_thesaurus_stopwords(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    return thesaurus_df[~thesaurus_df[PREFERRED].str.startswith("#").values].copy()  # type: ignore


def _remove_builtin_stopwords(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()

    stopwords = load_builtin_word_list("stopwords.txt")
    for stopword in stopwords:
        thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
            f" {stopword} ", " "
        )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
        r"\s+", " ", regex=True
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df = thesaurus_df[thesaurus_df[SIGNATURE].str.len() > 0]  # type: ignore

    return thesaurus_df


def _string_to_words(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split(" ")

    return thesaurus_df


def _words_to_string(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(set)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")
    return thesaurus_df


def _compute_matches(thesaurus_df: pd.DataFrame) -> dict[str, list[str]]:

    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates()
    grouped = mapping_df.groupby(SIGNATURE, as_index=False).agg({PREFERRED: list})
    matches = {
        pref[0]: pref[1:]
        for sign, pref in zip(grouped[SIGNATURE].values, grouped[PREFERRED].values)
        if len(pref) > 1
    }
    return matches
